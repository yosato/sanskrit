import re,os,sys,copy,glob,json
from difflib import SequenceMatcher
from collections import defaultdict
#Delims=' ^.'

def main0(FP,OutFP,LemmaDicFP=None,UpTo=None,Debug=0):
    def count_lines(FP):
        for LineCnt,_ in enumerate(open(FP)):
            pass
        return LineCnt

    OutFPTmp=OutFP+'.tmp'
    OutTmp=open(OutFPTmp,'wt')
#    Switched=False
    LineCnt=count_lines(FP)
    for Cntr,LiNe in enumerate(open(FP)):
        if UpTo and Cntr>UpTo:
            break
 #       if OutFP and not Switched and Cntr>LineCnt*0.8:
  #          OutTmp.close()
   #         OutTmp=open(OutFP+'.test','wt')
    #        Switched=True
        if Debug:    sys.stderr.write(str(Cntr+1)+': '+LiNe)
        OrgSeg=LiNe.strip().split('\t')
        if len(OrgSeg)!=3:
            print('something wrong with the line '+LiNe)
            continue
        else:
            (_,Org,Seg)=OrgSeg
            if Seg.endswith(']'):
                Seg=re.sub(r'[/ ]*\[.+?\]$','',Seg)
            tokenise=lambda Str: re.sub(r'(.),',r'\1 ,',re.sub(r'^"','',re.sub(r'[ ,\-]+$','',Str)))
            Seg=tokenise(Seg); Org=tokenise(Org)
            assert(Org[0]==Seg[0])

            WdPairs=align_org_seg(Org,Seg)

        if check_plausibility(WdPairs):
            for (SForm,InfForm) in WdPairs:
                OutTmp.write(SForm+'\t'+InfForm+'\n')
            OutTmp.write('EOS\n')
    
    OutTmp.close()

    if LemmaDicFP:
        add_lemmata(OutFPTmp,OutFP,LemmaDicFP)
    else:
        os.path.rename(OutFPTmp,OutFP)

def add_lemmata(InFP,OutFP,LemmaDicFP):
    # OccurringLemmaDic is a reduced dictionary that only contains occurring items
    OccurringLemmaDic=defaultdict(list)
    FSr=open(InFP)
    # lemma dic consists of 2-tuples with alphabet and dict
    for LiNeJ in open(LemmaDicFP):
        LemmaDic=json.loads(LiNeJ.strip())
        if len(LemmaDic)==2:
            InitChar,LemmaDic=LemmaDic
        InitChar=list(LemmaDic.values())[0][0][0]
        #AA=AStuff.intersection(set(LemmaDic.keys()))
        Successes=0;Failures=0
        for LiNeC in FSr:
            LineC=LiNeC.strip()
            if LineC=='EOS':
                continue
            else:
                InfForm=LineC.split('\t')[-1]
                if InfForm.startswith(InitChar):
                    if InfForm in LemmaDic.keys():
                        OccurringLemmaDic[InfForm]=LemmaDic[InfForm]
                        Successes+=1
                    else:
                        Failures+=1

    FSr.seek(0)
    Out=open(OutFP,'wt')
    for LiNe in FSr:
        Line=LiNe.strip()
        if Line=='EOS':
            Out.write(LiNe)
        else:
            InfForm=Line.split('\t')[-1]
            if InfForm in OccurringLemmaDic.keys():
                LemmaPoS=','.join(OccurringLemmaDic[InfForm][0])
            else:
                LemmaPoS='*,*'

            Out.write(Line+','+LemmaPoS+'\n')
    FSr.close()
                                 
def check_plausibility(WdPairs):
    CumDist=0;CumWdCnt=0
    Plausibility=True
    for WdPair in WdPairs:
        if sum(len(Wd) for Wd in WdPair)/2>3:
            CumWdCnt+=1
            SeqMtchr=SequenceMatcher(None,WdPair[0],WdPair[1])
            ThisDist=SeqMtchr.ratio()
            CumDist+=ThisDist;AvgDist=CumDist/CumWdCnt
            if ThisDist<0.1 or AvgDist<0.6:
                print('Likely wrong seg, '+str(ThisDist)+' '+str(AvgDist))
                print(WdPairs)
                Plausibility=False
                break
    return Plausibility

def align_org_seg(Org,Seg):
    WdsOrg=Seg.replace('^',' ').replace('.',' ').split()
    CurOrg=Org
    Wds=copy.copy(WdsOrg)  

    WdPairs=[]
    # we process it on the original basis
    while Wds and CurOrg:
        Lemma=Wds.pop(0)
        CurLemma=Lemma;CurOrg=CurOrg.lstrip().lstrip("'")
        if CurOrg.startswith(CurLemma):
            WdPairs.append((CurLemma,CurLemma,))
            CurOrg=CurOrg[len(CurLemma):]
        else:
            # then loop over chars of a lemma, which must be equal in charnum or longer
            CurWd='';Cntr=0
            while CurLemma:
                if Cntr==0 and CurOrg[0]!=CurLemma[0]:
                    CurLemma=CurLemma[1:]
                while CurLemma and CurOrg[0]==CurLemma[0]:
                    CurWd+=CurOrg[0]
                    CurOrg=CurOrg[1:]
                    CurLemma=CurLemma[1:]
                if CurLemma:
                    CurWd+=CurOrg[0];CurOrg=CurOrg[1:] if len(CurOrg)>=1 else ''
                    CurLemma=CurLemma[1:]
            WdPairs.append((CurWd,Lemma))
#        print(WdPairs)

    return WdPairs
    
def main():
    import argparse
    Psr=argparse.ArgumentParser()
    Psr.add_argument('parallel_fp')
    Psr.add_argument('--out-fp')
    Psr.add_argument('-l','--lemmadic-fp')
    Psr.add_argument('-u','--up-to',type=int)
    Args=Psr.parse_args()
    if Args.out_fp is None:
        Args.out_fp=os.path.join(os.path.dirname(Args.parallel_fp),os.path.basename(Args.parallel_fp)+'.out')
    if not os.path.dirname(Args.out_fp):
        print('parent of the specified fp '+Args.out_fp+' does not exist')

    if os.path.exists(Args.out_fp):
        LowerAnswer=None
        while not any(LowerAnswer==Ans for Ans in ('yes','y','n','no')):
            LowerAnswer=input('Specified filename exists. Overwrite? (Say y, otherwise it will abort): ').lower()

        if LowerAnswer.startswith('n'):
            sys.exit('rename the file and restart')
        

    if Args.lemmadic_fp and (not os.path.isfile(Args.lemmadic_fp) or not Args.lemmadic_fp.endswith('.json')):
        sys.exit('lemma dic, in json format, has to be there')
        
    
    main0(Args.parallel_fp,OutFP=Args.out_fp,LemmaDicFP=Args.lemmadic_fp,UpTo=Args.up_to)

if __name__=='__main__':
    main()

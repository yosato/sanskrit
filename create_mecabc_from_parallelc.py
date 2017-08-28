import re,os,sys,copy,glob,json
from difflib import SequenceMatcher
from collections import defaultdict
#Delims=' ^.'

def main0(FP,OutFP=None):
    def count_lines(FP):
        for LineCnt,_ in enumerate(open(FP)):
            pass
        return LineCnt
    Out=sys.stdout if OutFP is None else open(OutFP,'wt')
    Switched=False
    LineCnt=count_lines(FP)
    for Cntr,LiNe in enumerate(open(FP)):
        if Cntr>300:
            break
        if OutFP and not Switched and Cntr>LineCnt*0.8:
            Out.close()
            Out=open(OutFP+'.test','wt')
            Switched=True
        sys.stderr.write(str(Cntr+1)+': '+LiNe)
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
                Out.write(SForm+'\t'+InfForm+'\n')
            Out.write('EOS\n')
    if OutFP:
        Out.close()
        ErrorOut=open(OutFP+'.errors','wt')
        LemmaDicFP='/processedData/sanskrit/dictionary_IAST.short_lemmadict.json'
        OccurringLemmaDic=defaultdict(list)
        FSr=open(OutFP)
        AStuff=set()
        for LiNe in FSr:
            if LiNe=='EOS\n' or len(LiNe.strip().split())!=2:
                continue
            IF=LiNe.strip().split('\t')[1]
            if IF!='EOS\n' and IF.startswith('a'):
                AStuff.add(IF)
        FSr.seek(0)
        for LiNeJ in open(LemmaDicFP):
            InitChar,LemmaDic=json.loads(LiNeJ.strip())
            AA=AStuff.intersection(set(LemmaDic.keys()))
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
                            ErrorOut.write(InfForm+'\n')
        ErrorOut.close()
        FSr.seek(0)
        for LiNe in FSr:
            Line=LiNe.strip()
            if Line=='EOS':
                sys.stdout.write(LiNe)
            else:
                InfForm=Line.split('\t')[-1]
                if InfForm in OccurringLemmaDic.keys():
                    Lemma=OccurringLemmaDic[InfForm]
                else:
                    Lemma='*'
                    
                sys.stdout.write(Line+','+Lemma+'\n')
                                 
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
    Psr.add_argument('-o','--out-fp')
    Args=Psr.parse_args()
    if Args.out_fp and not os.path.dirname(Args.out_fp):
        print('parent of the specified fp '+Args.out_fp+' does not exist')
    main0(Args.parallel_fp,OutFP=Args.out_fp)

if __name__=='__main__':
    main()

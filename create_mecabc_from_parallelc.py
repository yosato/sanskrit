import re,os,sys,copy,glob
from difflib import SequenceMatcher
from collections import defaultdict
from pythonlib_ys import main as myModule
#Delims=' ^.'

def main0(FP,OutFP,LemmaDicDir,UpTo=None,Debug=0):
    def count_lines(FP):
        for LineCnt,_ in enumerate(open(FP)):
            pass
        return LineCnt

    OutFPTmp=OutFP+'.tmp'
    OutTmp=open(OutFPTmp,'wt')
#    Switched=False
#    LineCnt=count_lines(FP)
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
        else:
            
    
    OutTmp.close()

    add_lemmata(OutFPTmp,OutFP,LemmaDicDir)
    

def add_lemmata(InFP,OutFP,LemmaDicDir):
    OccurringLemmaDic,NotFounds=make_occurring_lemmadic(InFP,LemmaDicDir)

    FSr=open(InFP)
    Out=open(OutFP,'wt')
    for LiNe in FSr:
        Line=LiNe.strip()
        if Line=='EOS':
            Out.write(LiNe)
        else:
            InfForm=Line.split('\t')[-1]
            if InfForm in OccurringLemmaDic.keys():
                LemmaPoS=','.join(OccurringLemmaDic[InfForm])
            else:
                LemmaPoS='*,*'

            Out.write(Line+','+LemmaPoS+'\n')
    FSr.close()

def make_occurring_lemmadic(InFP,LemmaDicDir):
    def make_occurring_alphinfdic(FP):
        Dict=defaultdict(set)
        with open(FP) as FSr:
            for LiNe in FSr:
                if LiNe!='EOS\n':
                    LineEls=LiNe.strip().split('\t')
                    if len(LineEls)!=2:
                        print('strange line, '+LiNe)
                    else:
                        InfForm=LineEls[1]
                        Dict[InfForm[0]].add(InfForm)
        return Dict
            
    OccurringAlphsInfforms=make_occurring_alphinfdic(InFP)
    LemmaDicFPs=glob.glob(LemmaDicDir+'/*.pickle')
    # OccurringLemmaDic is a reduced dictionary that only contains occurring items
    OccurringLemmaDic=defaultdict(list); NotFounds=[]
    # lemma dic consists of 2-tuples with alphabet and dict
    for LemmaDicFP in LemmaDicFPs:
        Lexs=myModule.load_pickle(LemmaDicFP)
        Alph=Lexs[0].lemma[0]
        OccurringInfs=OccurringAlphsInfforms[Alph]
        for OccurringInf in OccurringInfs:
            Found=False
            PotOccurringLexs=[ Lex for Lex in Lexs if OccurringInf.startswith(Lex.stem)  ]
            for PotOccurringLex in PotOccurringLexs:
                if type(PotOccurringLex).__name__=='NonInfLexeme':
                    if PotOccurringLex.lemma==OccurringInf:
                        Found=True
                        OccurringLemmaDic[OccurringInf]=(PotOccurringLex.lemma,PotOccurringLex.pos,)
                elif OccurringInf in PotOccurringLex.inflect_all(FormOnly=True):
                    OccurringLemmaDic[OccurringInf]=(PotOccurringLex.lemma,PotOccurringLex.pos,)
                    Found=True
            if not Found:
                NotFounds.append(OccurringInf)

    return OccurringLemmaDic,NotFounds
                                 
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
    Psr.add_argument('--out-dir')
    Psr.add_argument('--out-fn')
    Psr.add_argument('-l','--lemmadic-dir',required=True)
    Psr.add_argument('-u','--up-to',type=int)
    Args=Psr.parse_args()
    if Args.out_dir is None:
        Args.out_dir=os.path.dirname(Args.parallel_fp)
    else:
        if not os.path.isdir(Args.out_dir):
            sys.exit('Dir '+Args.out_dir+' does not exist')
    if Args.out_fn is None:
        Args.out_fn=os.path.basename(Args.parallel_fp)

    OutFP=os.path.join(Args.out_dir,Args.out_fn)

    if os.path.exists(Args.out_fp):
        LowerAnswer=None
        while not any(LowerAnswer==Ans for Ans in ('yes','y','n','no')):
            LowerAnswer=input('Specified filename exists. Overwrite? (Say y, otherwise it will abort): ').lower()

        if LowerAnswer.startswith('n'):
            sys.exit('rename the file and restart')
        

    if not glob.glob(Args.lemmadic_dir+'/*.pickle'):
        sys.exit('lemma dics, in pickle, have to be there')
        
    
    main0(Args.parallel_fp,OutFP=Args.out_fp,LemmaDicDir=Args.lemmadic_dir,UpTo=Args.up_to)

if __name__=='__main__':
    main()

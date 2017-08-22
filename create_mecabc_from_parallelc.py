import re,os,sys,copy
from difflib import SequenceMatcher
#Delims=' ^.'

def main0(FP,OutFP=None):
    Out=sys.stdout if OutFP is None else open(OutFP,'wt')
    Switched=False
    for LineCnt,_ in enumerate(open(FP)):
        pass
    for Cntr,LiNe in enumerate(open(FP)):
        if OutFP and not Switched and Cntr>LineCnt*0.8:
            Out.close()
            Out=open(OutFP+'.test','wt')
            Switched=True
        sys.stderr.write(str(Cntr+1)+': '+LiNe)
        OrgSeg=LiNe.strip().split('\t')
        if len(OrgSeg)==3:
            (_,Org,Seg)=OrgSeg
            if Seg.endswith(']'):
                Seg=re.sub(r'[/ ]*\[.+?\]$','',Seg)
            tokenise=lambda Str: re.sub(r'(.),',r'\1 ,',re.sub(r'^"','',re.sub(r'[ ,\-]+$','',Str)))
            Seg=tokenise(Seg); Org=tokenise(Org)
            assert(Org[0]==Seg[0])
        else:
            print('something wrong with the line '+LiNe)
        WdPairs=align_org_seg(Org,Seg)

        if check_plausibility(WdPairs):
            for (Wd,Lemma) in WdPairs:
                Out.write(Wd+'\t'+Lemma+'\n')
            Out.write('EOS\n')
    if OutFP:
        Out.close()

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

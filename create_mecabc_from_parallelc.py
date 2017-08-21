import re,sys
#Delims=' ^.'


def main0(FP):
    for Cntr,LiNe in enumerate(open('parallel.txt')):
        sys.stderr.write(str(Cntr)+': '+LiNe)
        OrgSeg=LiNe.strip().split('\t')
        if len(OrgSeg)==2:
            (Org,Seg)=OrgSeg
            Org=re.sub(r'[ ,-]+$','',Org)
            Seg=re.sub(r'[ ,-]+$','',Seg)
            assert(Org[0]==Seg[0])
        else:
            print('something wrong with the line '+LiNe)
        WdPairs=create_mecabc_from_parallelc(Org,Seg)
        print(WdPairs)
        
def create_mecabc_from_parallelc(Org,Seg):
    Wds=Seg.replace('^',' ').replace('.',' ').split()
    SeqLen=len(Wds)
    WdInd=0;SegWd=''
    SegHd=True
    WdPairs=[]
    for i in range(len(Org)):
        if WdInd+1>=SeqLen:
            break
        if SegHd:
            WdCharInd=0;WdLen=len(Wds[WdInd])
            if Org[i]!=Wds[WdInd][WdCharInd]:
                WdCharInd+=1
            SegHd=False
        if WdCharInd+1<=WdLen and Org[i]==Wds[WdInd][WdCharInd]:
            SegWd+=Org[i]
            WdCharInd+=1
            
        else:
            if not SegHd:
                SegWd+=Org[i]
                WdPairs.append((SegWd.strip(),Wds[WdInd],))
                WdInd+=1;SegWd=''
                SegHd=True
    return WdPairs
    
def main():
    FP='parallel.txt'
    main0(FP)

if __name__=='__main__':
    main()

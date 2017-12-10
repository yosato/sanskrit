import sys,os,re

OurCats=('others','ignore','noun','adj','pron','verb')

def main0(DictFP,CatTSV):
    CatDict=make_catdic(CatTSV)
    divide_into_posdics(DictFP,CatDict)

def make_catdic(CatTSV):
    Dict={}
    with open(CatTSV) as FSr:
        for Cntr,LiNe in enumerate(FSr):
            LineEls=LiNe.split()
            if len(LineEls)<3:
                sys.stderr.write('not processable line, LN '+str(Cntr+1)+', '+LiNe)
                continue
            elif LineEls[2] not in OurCats:
                sys.stderr.write('funny or empty cat, LN '+str(Cntr+1)+', '+LiNe)
                continue
            SurfaceCat,OurCat=LineEls[1],LineEls[2]
            Dict[SurfaceCat]=OurCat
    return Dict

def divide_into_posdics(DictFP,CatDict):
    for OurCat in OurCats+('missed',):
        FP=os.path.basename(DictFP)+'.'+OurCat
        VarN='FSw'+OurCat
        CmdStr=VarN+'=open("'+FP+'","wt")'
        exec(CmdStr)
    DoneLines=set()
    with open(DictFP) as FSr:
        for Cntr,LiNe in enumerate(FSr):
            LineEls=LiNe.strip().split('\t')
            if len(LineEls)<3:
                sys.stderr.write('funny line, LN '+str(Cntr+1)+', '+LiNe)
                continue
            SurfaceCat=LineEls[2]
            SurfaceCat=SurfaceCat.strip().strip('.')
            OurCat=CatDict[SurfaceCat] if SurfaceCat in CatDict.keys() else 'missed'
            RightFSwVar='FSw'+OurCat
            NewLine='\t'.join(LineEls[:3])
            if '{' in NewLine:
                NewLine=re.sub(r' *{(.+?)} *','',NewLine)
            if NewLine in DoneLines:
                #sys.stderr.write('duplicate found\n')
                continue
            else:
                DoneLines.add(NewLine)
            if "'" in NewLine:
                NewLine=NewLine.replace("'",' ')
            CmdStr=RightFSwVar+".write('"+NewLine+"')"
            exec(CmdStr)
            CmdStr=RightFSwVar+".write('\\n')"
            exec(CmdStr)
    
    for OurCat in OurCats+('missed',):
        VarN='FSw'+OurCat
        CmdStr=VarN+'.close()'
        exec(CmdStr)
                                  

def main():
    Args=sys.argv
    if len(Args)!=3:
        sys.exit('2 args, dict and cat name file, necessary')
    Dict,CatTSV=Args[1],Args[2]
    if not os.path.isfile(Dict):
        sys.exit('dict not found: '+Dict)
    if not os.path.isfile(CatTSV):
        sys.exit('cat name file not found: '+CatTSV)
    main0(Dict,CatTSV)

if __name__=='__main__':
    main()

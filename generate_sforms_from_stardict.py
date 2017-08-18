import imp,os,sys
import sanskrit_morph

imp.reload(sanskrit_morph)

def main0(StarDictFP,Delimiter='\t',Debug=False,OutDir=None,UpTo=100):
    if OutDir is None:
        Out=sys.stdout
    else:
        Out=open(OutDir+'/'+os.path.basename(StarDictFP)+'.out','wt')
    for Cntr,LiNe in enumerate(open(StarDictFP)):
        if Debug: Out.write(str(Cntr+1)+' '+LiNe.strip()+'\n')
        if Cntr>UpTo:
            break
        InfWds=lemmaline2wds(LiNe.strip(),Delimiter)
        if not InfWds:
            Out.write('no words for: '+LiNe.strip()+'\n')
        else:
            for Wd in InfWds:
                Out.write(Wd.stringify_featvals()+'\n')
                Out.write(Wd.generate_sandhiforms(Stringify=True)+'\n')
        Out.write('\n\n')

def lemmaline2wds(Line,Delimiter):
    LineEls=Line.split(Delimiter)
    InfCats=['n','m','f','pron','verb','adj']
    CatStr=LineEls[2];CatStrSplit=CatStr.split()
    Lemma=LineEls[1]
    if len(Lemma.split())>1:
        print('compound word? '+Lemma)
        return []
    Cat=(CatStr[:-1] if (len(CatStrSplit)==1 and CatStr.endswith('.')) else CatStr.split()[0])
    print(Lemma+'\t'+Cat)
    if Cat not in InfCats:
        print(Cat+' not found in the taxonomy')
        return []
    else:
        return generate_words(Lemma,Cat)

def generate_words(Lemma,Cat):
    Nouns=['n','m','f']

    if Cat in Nouns:
        NounLex=sanskrit_morph.NounLexeme(Lemma,Cat)
        return NounLex.decline_all()
    elif Cat == 'adj':
        AdjLex=sanskrit_morph.AdjLexeme(Lemma)
        return AdjLex.decline_all()
    elif Cat == 'pron':
        PronLex=sanskrit_morph.PronounLexeme(Lemma)
        return PronLex.decline_all()
    elif Cat == 'verb':
        VLex=sanskrit_morph.VerbLexeme(Lemma)
        return VLex.conjugate_all()
    

def main():
    import argparse
    ArgPsr=argparse.ArgumentParser()
    ArgPsr.add_argument('stardict_fps',nargs='+')
    ArgPsr.add_argument('-u','--up-to',type=int)
    ArgPsr.add_argument('-o','--out-dir')
    ArgPsr.add_argument('--debug',action='store_true')
    Args=ArgPsr.parse_args()
    RepoDir=os.path.join(os.getenv('HOME'),'myProjects/sanskrit')
    RepoSubDir='yo_scripts'
    if not Args.stardict_fps:
        FPs=[os.path.join(RepoDir,RepoSubDir,'dictionary_IAST.txt')]
    else:
        if Args.out_dir:
            if not os.path.isdir(Args.out_dir):
                sys.exit('\ndir for out-dir '+Args.out_dir+' does not exist\n')
        else:
            print('out dir not specified, to output in stdout\n')
        FPs=[]
        for FP in Args.stardict_fps:
            if '/' not in FP:
                FP=os.path.join(RepoDir,RepoSubDir,FP)
            if not os.path.isfile(FP):
                sys.exit('\nfile specified ('+FP+') does not exist\n')
            FPs.append(FP)

        for FP in FPs:
            main0(FP,UpTo=Args.up_to,OutDir=Args.out_dir,Debug=Args.debug)
    
if __name__=='__main__':
    main()

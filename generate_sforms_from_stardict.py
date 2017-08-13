import imp,os,sys
import sanskrit_morph

imp.reload(sanskrit_morph)


def main0(StarDictFP,UpTo=300):
    WdsByLemma=file2wds(StarDictFP,UpTo)
    for WdsPerLemma in WdsByLemma:
        print(WdsPerLemma[0].lexeme.lemma+'\n')
        for Wd in WdsPerLemma:
            print(' '.join([Wd.infform,Wd.lexeme.pos,Wd.lexeme.gender,Wd.case,Wd.number]))
            print(Wd.sandhiforms)
        print()

def file2wds(StarDictFP,UpTo):
    Wds=[]
    InfCats=['n','m','f','pron','v','adj']
    Nouns=['n','m','f']
    for Cntr,LiNe in enumerate(open(StarDictFP)):
        print(LiNe)
        if Cntr>UpTo:
            break
        LineEls=LiNe.strip().split('│')[1:]
        CatStr=LineEls[2]
        Lemma=LineEls[1]; Cat=(CatStr[:-1] if CatStr.endswith('.') else CatStr)
        if Cat not in InfCats:
            continue
        else:
            if Cat in Nouns:
                NounLex=sanskrit_morph.NounLexeme(Lemma,Cat)
                Wds.append(NounLex.decline_all())
            elif Cat == 'adj':
                AdjLex=sanskrit_morph.AdjLexeme(Lemma)
                Wds.append(AdjLex.decline_all())
            elif Cat == 'pron':
                PronLex=sanskrit_morph.PronounLexeme(Lemma)
                Wds.append(PronLex.decline_all())
            elif Cat == 'v':
                VLex=sanskrit_morph.VerbLexeme(Lemma)
                Wds.append(VLex.conjugate_all())
    return Wds

def main():
    import argparse
    ArgPsr=argparse.ArgumentParser()
    ArgPsr.add_argument('stardict_fp',nargs='?')
    Args=ArgPsr.parse_args()
    if Args.stardict_fp is None:
        RepoDir=os.path.join(os.getenv('HOME'),'myProjects/sanskrit/sanskrit_coders')
        RepoSubDir='stardict-sanskrit/sanskrit-db'
        FN='sanskrit.infonly.table'
        Args.stardict_fp=os.path.join(RepoDir,RepoSubDir,FN)
    if not os.path.isfile(Args.stardict_fp):
        sys.exit('\nfile specified ('+Args.stardict_fp+') does not exist\n')
    else:
        main0(Args.stardict_fp)
    
if __name__=='__main__':
    main()

import imp
import sanskrit_morph

imp.reload(sanskrit_morph)

def main0(StarDictFP,UpTo=10000):
    WdsByLemma=file2wds(StarDictFP,UpTo)
    for WdsPerLemma in WdsByLemma:
        print(WdsPerLemma[0].lexeme.lemma+'\n')
        for Wd in WdsPerLemma:
            print(' '.join([Wd.infform,Wd.lexeme.pos,Wd.lexeme.gender,Wd.case,Wd.number]))
            print(Wd.sandhiforms)
        print()

def file2wds(StarDictFP,UpTo):
    Wds=[]
    for Cntr,LiNe in enumerate(open(StarDictFP)):
        if Cntr>UpTo:
            break
        LineEls=LiNe.strip().split('│')[1:]
        Lemma=LineEls[1]; LemmaLstChr=LineEls[1][-1]; Cat=LineEls[2]
        if (Cat in ['n.','m.'] and LemmaLstChr=='a') or (Cat=='f.' and LemmaLstChr=='ā'):
            NounLex=sanskrit_morph.NounLexeme(Lemma,Cat[:-1])
            Wds.append(NounLex.decline_all())
    return Wds

            
                

    
def main():
    import argparse
    ArgPsr=argparse.ArgumentParser()
    ArgPsr.add_argument('stardict_fp')
    Args=ArgPsr.parse_args()
    main0(Args.stardict_fp)
    
if __name__=='__main__':
    main()

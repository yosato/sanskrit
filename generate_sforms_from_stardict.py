import imp,os,sys,re,json
import sanskrit_morph
from collections import defaultdict

imp.reload(sanskrit_morph)

def main0(StarDictFP,Delimiter='\t',Debug=0,OutDir=None,DoLemmaDict=True,AlphCntUpTo=None,ErrorFP=None):
    StarDictFN=os.path.basename(StarDictFP)
    StarDictFNStem='.'.join(StarDictFN.split('.')[:-1])
    if DoLemmaDict:
        if OutDir is None:
            sys.exit('Lemma dict requires out dir\n')
        LemmaDict=defaultdict(set)
        LemmaJFSw=open(os.path.join(OutDir,StarDictFNStem+'_lemmadict.json'),'wt')

    if OutDir is None:
        Out=sys.stdout
    else:
        Out=open(os.path.join(OutDir,StarDictFNStem+'.out'),'wt')
    PrvAlph='';AlphCnt=0

    InfTypeFSw=open(os.path.join(OutDir,StarDictFNStem+'.inftypes'),'wt')
    
    for Cntr,Wds in enumerate(generate_words_perline(StarDictFP,Delimiter,Debug,OutDir,ErrorFP)):
        if DoLemmaDict or AlphCntUpTo:
            CurAlph=Wds[0].infform[0]
            if CurAlph!=PrvAlph:
                AlphCnt+=1
                PrvAlph=Wds[0].infform[0]
                if AlphCnt>=2:
                    LemmaDict=[PrvAlph,{Key:list(Set) for (Key,Set) in LemmaDict.items() }]
                    LemmaDictJ=json.dumps(LemmaDict)
                    LemmaJFSw.write(LemmaDictJ)
                    LemmaJFSw.write('\n')
                    LemmaDict=defaultdict(set)
            
            if AlphCntUpTo and AlphCntUpTo<AlphCnt:
                break
        for Wd in Wds:
            if 'inftype' in Wds[0].__dict__.keys():
                InfTypeFSw.write(' '.join([Wds[0].lexeme.lemma, Wds[0].lexeme.pos, Wds[0].inftype])+'\n')

            if Debug>=2:    sys.stderr.write(Wd.stringify_featvals()+'\n')
            Out.write(Wd.infform+'\t'+Wd.infform+','+Wd.lexeme.lemma+'\n')
            LemmaDict[Wd.infform].add(Wd.lexeme.lemma)
            SandhiFormPair=Wd.generate_sandhiforms()
            (SandhiVForm,SandhiForms)=SandhiFormPair
            if SandhiVForm:
                Out.write(SandhiVForm+'\t'+Wd.infform+Wd.lexeme.lemma+'\n')
            for (SandhiForm,_) in SandhiForms:
                Out.write(SandhiForm+'\t'+Wd.infform+','+Wd.lexeme.lemma+'\n')
    InfTypeFSw.close()
                
                
    if DoLemmaDict:
        LemmaDict=[CurAlph,{Key:list(Set) for (Key,Set) in LemmaDict.items() }]
        LemmaDictJ=json.dumps(LemmaDict)
        LemmaJFSw.write(LemmaDictJ)
        LemmaJFSw.write('\n')
    Size=sys.getsizeof(LemmaDict)
    Len=len(LemmaDict)
    print(Size)
    print(Len)
    if DoLemmaDict:
        LemmaJFSw.close()
        
                

def generate_words_perline(StarDictFP,Delimiter='\t',Debug=0,OutDir=None,ErrorFP=None):
    OutErr=open(ErrorFP,'wt') if ErrorFP else sys.stderr
    Prv=[]
    for Cntr,LiNe in enumerate(open(StarDictFP)):
        LineEls=[ re.sub(r'{.+}$','',El).strip() for El in LiNe.strip().split(Delimiter) if El ][:3]
        if any(not El for El in LineEls) or len(LineEls)<3:
            continue
        if LineEls[2]!='verb' and LineEls[2].startswith('verb'):
            LineEls[2]='verb'
        if LineEls==Prv:
            if Debug:   sys.stderr.write('duplicates, ignoring, '+LiNe)
            continue
        elif len(LineEls[1].split())>1:
            sys.stderr.write('compound word? '+LineEls[1]+'\n')
            continue
        elif LineEls[2]=='phrase':
            continue
        else:
            if Debug:    sys.stderr.write(str(Cntr)+': '+LiNe)
            Prv=LineEls
            Wds=lemmaline2wds(LineEls,Delimiter)
            if not Wds:
                OutErr.write('no results returned from '+LiNe)
                continue
            else:
                yield Wds
    if ErrorFP:
        OutErr.close


def lemmaline2wds(LineEls,Delimiter):
    InfCats=['n','m','f','pron','verb','adj']
    CatStr=LineEls[2];CatStrSplit=CatStr.split()
    Lemma=LineEls[1]
    Cat=(CatStr[:-1] if (len(CatStrSplit)==1 and CatStr.endswith('.')) else CatStr.split()[0])
#    print(Lemma+'\t'+Cat)
    if Cat not in InfCats:
        return [ sanskrit_morph.NonInfWord(Lemma,Cat) ]
    else:
        return get_infl_words(Lemma,Cat)

def get_infl_words(Lemma,Cat):
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
    ArgPsr.add_argument('-u','--alphcnt-up-to',type=int)
    ArgPsr.add_argument('-o','--out-dir')
    ArgPsr.add_argument('--debug',type=int,default=0)
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
            main0(FP,AlphCntUpTo=Args.alphcnt_up_to,OutDir=Args.out_dir,Debug=Args.debug)
    
if __name__=='__main__':
    main()

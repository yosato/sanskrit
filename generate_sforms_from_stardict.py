import imp,os,sys,re,pickle,time,glob,shutil
import sanskrit_morph
from pythonlib_ys import main as myModule 
from collections import defaultdict

imp.reload(sanskrit_morph)

def main0(StarDictFP,Debug=0,Delimiter='\t',OutDir=None,AlphCntUpTo=None,UpTo=None):
    LineCnt=myModule.get_linecount(StarDictFP)
    StarDictFN=os.path.basename(StarDictFP)
    StarDictFNStem='.'.join(StarDictFN.split('.')[:-1])
    InDir=os.path.dirname(StarDictFP)

    if OutDir is None:
        OutDir=os.path.dirname(StarDictFP)
    # PFP=pickle fp
    LemmaDicDir=os.path.join(OutDir,StarDictFNStem+'_lemmadics')
    if not os.path.isdir(LemmaDicDir):
        os.makedirs(LemmaDicDir)

    LemmaDics=glob.glob(LemmaDicDir+'/*.pickle')
    if LemmaDics:
        Message='Lemmadics already exist. Overwrite? ([y]es or [n]o): '
        Ans=input(Message)
        while all(Ans.lower() != RightAns for RightAns in ('y','yes','no', 'n')):
            print('answer yes or no')
            Ans=input(Message)
        if Ans.startswith('y'):
            OW=True
        else:
            OW=False
    else:
        OW=True

    AlphWriteOutDir=LemmaDicDir+'/alph_writeouts'
    if OW:
        for LemmaDic in LemmaDics:
            os.remove(LemmaDic)
        if os.path.isdir(AlphWriteOutDir):
            shutil.rmtree(AlphWriteOutDir)
        sys.stderr.write('Creating lemma dicts for '+StarDictFP+' in '+LemmaDicDir+'\n')
        create_lemmadict(StarDictFNStem,InDir,OutDir,LemmaDicDir,LineCnt,Delimiter,AlphCntUpTo,UpTo,Debug)
        LemmaDics=glob.glob(LemmaDicDir+'/*.pickle')

    if not os.path.isdir(AlphWriteOutDir):
        os.makedirs(AlphWriteOutDir)

    sys.stderr.write('Writing out lemma dicts for '+StarDictFP+' in '+AlphWriteOutDir+'\n')
    writeout_lemmadict(StarDictFNStem,AlphWriteOutDir,LemmaDics,Debug=Debug)

def writeout_lemmadict(StarDictFNStem,OutDir,LemmaDics,Debug=0):
    for PFP in LemmaDics:
        FSrP=open(PFP,'rb')
        Lexs=pickle.load(FSrP)
        Alph=Lexs[0].lemma[0]
        FSrP.close()
        OutFP=os.path.join(OutDir,Alph+'.writeout')
        Out=open(OutFP,'wt')
        sys.stderr.write('doing alphabetical writeout with '+Alph+'\n')

        for Lex in Lexs:
            Wds=Lex.inflect_all()
            for Wd in Wds:
                OutLine=Wd.infform+'\t'+Wd.infform+','.join([Wd.lexeme.lemma,Wd.lexeme.pos,'no_sandhi'])+'\n'
                if Debug>=2:
                    sys.stderr.write(OutLine)
                Out.write(OutLine)
                SandhiFormPair=Wd.generate_sandhiforms()
                (SandhiVForm,SandhiForms)=SandhiFormPair
                if SandhiVForm:
                    Out.write(SandhiVForm+'\t'+','.join([Wd.infform,Wd.lexeme.lemma,Wd.lexeme.pos,'sandhi'])+'\n')
                for (SandhiForm,_) in SandhiForms:
                    Out.write(SandhiForm+'\t'+','.join([Wd.infform,Wd.lexeme.lemma,Wd.lexeme.pos,'sandhi'])+'\n')
        Out.close()
    sys.stderr.write('lemmadict writeouts finished\n\n')

def create_lemmadict(StarDictFNStem,InDir,OutDir,LemmaDicDir,LineCnt,Delimiter,AlphCntUpTo,UpTo,Debug):
    def populate_lemmadict(Wds,LemmaDicDir):
        FstWdAlph=Wds[0].lemma[0]
        LstWdAlph=Wds[-1].lemma[0]
        assert FstWdAlph==LstWdAlph
        LemmaFP=os.path.join(LemmaDicDir,FstWdAlph+'.pickle')
        LemmaFSw=open(LemmaFP,'bw')
        pickle.dump(Wds,LemmaFSw)
        LemmaFSw.close()

    PrvAlph='';AlphCnt=0

    OutFPStem=os.path.join(OutDir,StarDictFNStem)
    #InfTypeFSw=open(OutFPStem+'.inftypes','wt')
    ErrorFSw=open(OutFPStem+'.errors','wt')

    Wds=[]
    for Cntr,Lex in enumerate(generate_words_perline(os.path.join(InDir,StarDictFNStem+'.tsv'),Delimiter,Debug,OutDir,ErrorFSw)):
        WdCnt=Cntr+1
        if WdCnt%10000==0:
            sys.stderr.write(str(WdCnt)+' lexemes done\n')
            time.sleep(2)
        if UpTo and Cntr>UpTo:
            break
        if type(Lex).__name__!='NonInfLexeme' and not Lex.inftype:
            ErrorMsg='no inftype for '+Lex.lemma+'\n'
            if Debug:
                sys.stderr.write(ErrorMsg)
            ErrorFSw.write(ErrorMsg)
            continue
        CurAlph=Lex.lemma[0]
        if CurAlph!=PrvAlph:
            AlphCnt+=1
            if AlphCnt>=2:
                if Wds:
                    populate_lemmadict(Wds,LemmaDicDir)
                else:
                    sys.stderr.write('wds for'+CurAlph+' empty')
                Wds=[]
            PrvAlph=CurAlph
        Wds.append(Lex)
            
        if AlphCntUpTo and AlphCntUpTo<AlphCnt:
            break
                
    populate_lemmadict(Wds,LemmaDicDir)

    sys.stderr.write('Total '+str(WdCnt)+' lexemes done for '+StarDictFNStem+' (out of total '+str(LineCnt)+' lines)'+'\n\n')

def generate_words_perline(StarDictFP,Delimiter='\t',Debug=0,OutDir=None,ErrorFSw=None):
    OutErr=ErrorFSw if ErrorFSw else sys.stderr
    Prv=[]
    for Cntr,LiNe in enumerate(open(StarDictFP)):
        LineEls=[ re.sub(r'{.+}$','',El).strip() for El in LiNe.strip().split(Delimiter) if El ][:3]
        if any(not El for El in LineEls) or len(LineEls)<3:
            continue
        if LineEls[2]!='verb' and LineEls[2].startswith('verb'):
            LineEls[2]='verb'
        if LineEls==Prv:
            if Debug>=2:   sys.stderr.write('duplicates, ignoring, '+LiNe)
            continue
        elif len(LineEls[1].split())>1:
            OutErr.write('compound word? '+LineEls[1]+'\n')
            continue
        elif LineEls[2]=='phrase':
            continue
        elif LineEls[1].startswith('-'):
            continue
        else:
            if Debug:    sys.stderr.write('Line '+str(Cntr)+': '+LiNe.strip()+'\n')
            Prv=LineEls
            try:
                Lex=lemmaline2lexeme(LineEls,Delimiter)
            except ValueError:
                OutErr.write('no inftype identified for '+LiNe)
            if not Lex:
                OutErr.write('no results returned from this line: '+LiNe)
                continue
            else:
                yield Lex

def lemmaline2lexeme(LineEls,Delimiter):
    InfCats=['n','m','f','pron','verb','adj']
    CatStr=LineEls[2];CatStrSplit=CatStr.split()
    Lemma=LineEls[1]
    Cat=(CatStr[:-1] if (len(CatStrSplit)==1 and CatStr.endswith('.')) else CatStr.split()[0])
#    print(Lemma+'\t'+Cat)
    if (Cat not in InfCats) or (Cat=='n' and Lemma.endswith('id')):
        return sanskrit_morph.NonInfLexeme(Lemma,Cat)
    else:
        if Cat in ['n','m','f']:
            return sanskrit_morph.NounLexeme(Lemma,Cat)
        elif Cat == 'adj':
            return sanskrit_morph.AdjLexeme(Lemma)
        elif Cat == 'pron':
            return sanskrit_morph.PronounLexeme(Lemma)
        elif Cat == 'verb':
            return sanskrit_morph.VerbLexeme(Lemma)

def main():
    import argparse
    ArgPsr=argparse.ArgumentParser()
    ArgPsr.add_argument('stardict_fps',nargs='+')
    ArgPsr.add_argument('-u','--alphcnt-up-to',type=int)
    ArgPsr.add_argument('-o','--out-dir')
    ArgPsr.add_argument('--up-to',type=int)
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

        FPs=[]
        for FP in Args.stardict_fps:
            if '/' not in FP:
                FP=os.path.join(RepoDir,RepoSubDir,FP)
            if not os.path.isfile(FP):
                sys.exit('\nfile specified ('+FP+') does not exist\n')
            FPs.append(FP)

        for FP in FPs:
            main0(FP,AlphCntUpTo=Args.alphcnt_up_to,OutDir=Args.out_dir,Debug=Args.debug,UpTo=Args.up_to)
    
if __name__=='__main__':
    main()

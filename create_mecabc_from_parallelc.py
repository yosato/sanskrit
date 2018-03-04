import re,os,sys,copy,glob
from difflib import SequenceMatcher
from collections import defaultdict
from pythonlib_ys import main as myModule
#Delims=' ^.'

def main0(ParallelFP,OutFP,LemmaDicDir,Debug=0):
    OutFPTmp=OutFP+'.tmp'
    align_unseg_seg(ParallelFP,OutFPTmp,Debug=Debug)
    add_lemmata(OutFPTmp,OutFP,LemmaDicDir)
    
def align_unseg_seg(ParallelFP,OutFP,Debug=0):
    def count_lines(FP):
        for LineCnt,_ in enumerate(open(FP)):
            pass
        return LineCnt

    Out=open(OutFP,'wt')
    OutErr=open(OutFP+'.alignerrors','wt')

    AlignFailCnt=0
    for Cntr,LiNe in enumerate(open(ParallelFP)):
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

            WdChunkPairs=align_org_seg_global(Org,Seg)
            #if WdChunkPairs is None:
            #    align_org_seg_global(Org,Seg)

        if WdChunkPairs is not None:
            for WdPairs in WdChunkPairs:
                for (SForm,InfForm) in WdPairs:
                    Out.write(SForm+'\t'+InfForm+'\n')
                Out.write('<sp>'+'\t'+'<sp>'+'\n')
            Out.write('EOS\n')
        else:
            AlignFailCnt+=1
            OutErr.write(LiNe+'\n')
    sys.stderr.write(str(Cntr+1)+' lines done\n')
    sys.stderr.write(str(AlignFailCnt)+' lines failed\n')
    Out.close();OutErr.close()



            
def add_lemmata(InFP,OutFP,LemmaDicDir):
    def disambiguate_pos(PotLemmata):
        OrderedCats=('noun','adj','ind','indec','verb','adverb')
        CatLemmata=defaultdict(set)
        for Lemma,PoS in PotLemmata:
            CatLemmata[Lemma].add((Lemma,PoS))
        MaxCard=max(len(CatLemma) for CatLemma in CatLemmata)
        MaxCardSet=[ len(CatLemma) for CatLemma in CatLemmata ]
        for Cat in OrderedCats:
            for El in MaxCardSet:
                if El[1]==Cat:
                    ChosenEl=El
                    break
            ChosenEl=(OrderedCats[0],MaxCardSet[0][0])
        return ChosenEl
    
    sys.stderr.write('\nWe first make an indexed (concise) dic, this could take a bit of time, unless you reuse it\n')
    OccurringLemmaDic,NotFounds=make_occurring_lemmadic(InFP,LemmaDicDir)

    FSr=open(InFP)
    Out=open(OutFP,'wt')
    for LiNe in FSr:
        Line=LiNe.strip()
        if Line=='EOS':
            Out.write(LiNe)
        else:
            SF,InfForm=Line.split('\t')
            if InfForm=='<sp>':
                LemmaPoS=('<space>','symbol')
            elif InfForm==',':
                LemmaPoS=('<comma>','symbol')
            else:
#                assert((SF,InfForm) in OccurringLemmaDic.keys())
                PotLemmata=OccurringLemmaDic[(SF,InfForm)]
                if PotLemmata(PotLemmata)==1:
                    LemmaPoS=PotLemmata[0]
                else:
                    LemmaPoS=disambiguate_pos(PotLemmata)
            Fts=(InfForm,)+LemmaPoS
            InfFormLemmaPoSLine=','.join(Fts)
            CorpusLine=SF+'\t'+InfFormLemmaPoSLine+'\n'
            Out.write(CorpusLine)

    FSr.close()

                                            

def make_occurring_lemmadic(InFP,LemmaDicDir,InitOccDicP=True):
    def make_occurring_alphinfdic(FP):
        # alphabetical dic
        Dic=defaultdict(set)
        with open(FP) as FSr:
            for LiNe in FSr:
                if LiNe!='EOS\n' and LiNe.strip()!='':
                    LineEls=LiNe.strip().split('\t')
                    SurfForm,InfForm=LineEls[0:2]
                    Alph=InfForm[0]
                    Dic[Alph].add((SurfForm,InfForm,))
        return Dic

    AlphSFsIFs=make_occurring_alphinfdic(InFP)
    
    LemmaDicFPs=glob.glob(LemmaDicDir+'/*.pickle')
    # OccurringLemmaDic is a reduced dictionary that contains only occurring items with only necessary features 
    # its keys are tuples (SurfForm,InfForm)
    OccurringLemmaDic=defaultdict(set); NotFounds=[]
    
    if InitOccDicP:
        InitDicFSw=open(InFP+'.csv','wt')
        val2str=lambda SF,Val:','.join((SF,'0','0','0')+Val)
    # lemma dic consists of 2-tuples with alphabet and dict
    for LemmaDicFP in LemmaDicFPs:
        Lexs=myModule.load_pickle(LemmaDicFP)
        Alph=Lexs[0].lemma[0]
        OccSFsInfs=AlphSFsIFs[Alph]
        for OccSF,OccInf in OccSFsInfs:
            Found=False
            PotOccurringLexs=[ Lex for Lex in Lexs if OccInf.startswith(Lex.stem)  ]
            for PotOccurringLex in PotOccurringLexs:
                # lemma itself is always an inf form
                ValL=(PotOccurringLex.lemma,PotOccurringLex.pos,)
                OccurringLemmaDic[(OccSF,PotOccurringLex.lemma)].add(ValL)
                if InitOccDicP:
                    Str=val2str(OccSF,ValL)
                    InitDicFSw.write(Str)
                Val=(PotOccurringLex.lemma,PotOccurringLex.pos,)
                if type(PotOccurringLex).__name__=='NonInfLexeme':
                    if PotOccurringLex.lemma==OccInf:
                        Found=True
                        OccurringLemmaDic[(OccSF,OccInf)].add(Val)
                elif OccInf in PotOccurringLex.inflect_all(FormOnly=True):
                    OccurringLemmaDic[(OccSF,OccInf)].add(Val)
                    Found=True
                if Found and InitOccDicP:
                    InitDicFSw.write(val2str(OccSF,Val))
            if not Found:
                OccurringLemmaDic[(OccSF,OccInf)]=[('*','*')]
                NotFounds.append(OccInf)
            
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

def samechunk_likely(OrgChunk,SegChunk):
    Bool=False
    if OrgChunk[0]==SegChunk[0] and OrgChunk[-1]==OrgChunk[-1] and len(SegChunk.replace('.','').replace('^',''))-len(OrgChunk)<=round(len(OrgChunk)*0.1):
        Bool=True
    return Bool

def align_org_seg_global(Org,Seg):
    ChunkPairs=[]
    OrgChunks=Org.split()
    SegChunks=Seg.split()
    SegChunks=[Chunk for Chunk in SegChunks if Chunk!='--']
    SegChunks=SegChunks[:-1] if SegChunks[-1] in (',','.','_') else SegChunks
    OrgChunks=OrgChunks[:-1] if OrgChunks[-1] in (',','.','-') else OrgChunks
    if len(OrgChunks)>len(SegChunks):
        Longers=OrgChunks;Shorters=SegChunks
    else:
        Longers,Shorters=SegChunks,OrgChunks
    NewLongers=[];NewShorters=[];i=0;j=0
    while i+1 <= len(Longers) and j+1 <= len(Shorters):
        IncrementI=1
        LChunk=Longers[i]
        SChunk=Shorters[j]
        if LChunk==SChunk:
            NewShorters.append(SChunk)
            NewLongers.append(LChunk)
        else:
            if samechunk_likely(LChunk,SChunk):
                NewShorters.append(SChunk)
                NewLongers.append(LChunk)
            else:
                try:
                    LChunk=Longers[i]+Longers[i+1]
                    if samechunk_likely(LChunk,SChunk):
                        NewLongers.append(LChunk)
                        NewShorters.append(SChunk)
                        IncrementI=2
                 
                    else:
#                        sys.stderr.write('alignment failed for '+LChunk+' '+SChunk+'\n\n')
                        return None
                except:
                    return None
        i+=IncrementI;j+=1
        #print(NewShorters)
        #print(NewLongers)
        #print()
    if len(NewShorters)!=len(NewLongers):
        return None
    else:
        if len(OrgChunks)>len(SegChunks):
            OrgChunks,SegChunks=NewLongers,NewShorters
        else:
            OrgChunks,SegChunks=NewShorters,NewLongers
    
    for OrgChunk,SegChunk in zip(OrgChunks,SegChunks):
        try:
            ChunkPairs.append(align_org_seg(OrgChunk,SegChunk))
        except:
            return None
    return ChunkPairs
        

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
    Args=Psr.parse_args()
    if Args.out_dir is None:
        Args.out_dir=os.path.dirname(Args.parallel_fp)
    else:
        if not os.path.isdir(Args.out_dir):
            sys.exit('Dir '+Args.out_dir+' does not exist')
    if not os.path.isdir(Args.lemmadic_dir):
        sys.exit('Dir '+Args.lemmadic_dir+' does not exist')
    if Args.out_fn is None:
        Args.out_fn=os.path.basename(Args.parallel_fp)+'.mecab'

    OutFP=os.path.join(Args.out_dir,Args.out_fn)

    if os.path.exists(OutFP):
        LowerAnswer=None
        while not any(LowerAnswer==Ans for Ans in ('yes','y','n','no')):
            LowerAnswer=input('Specified filename exists. Overwrite? (Say y, otherwise it will abort): ').lower()

        if LowerAnswer.startswith('n'):
            sys.exit('rename the file and restart')
        
    if not glob.glob(Args.lemmadic_dir+'/*.pickle'):
        sys.exit('lemma dics, in pickle, have to be there')
        
    
    main0(Args.parallel_fp,OutFP,LemmaDicDir=Args.lemmadic_dir)

if __name__=='__main__':
    main()

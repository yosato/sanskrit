import imp,sys,time
from pythonlib_ys import morph_univ

import paradigms,sandhi,sanskrit_phon
imp.reload(paradigms)
imp.reload(sandhi)
imp.reload(sanskrit_phon)

def get_stem_suffix(Str):
    if len(Str)==1:
        return Str,Str
    if any(Str.endswith(End) for End in ('in','at','āt')) or (any(Str.endswith(End) for End in ('ḥ','ṛ')) and Str[-2] in sanskrit_phon.Vowels):
        SplitPoint=-2
    else:
        SplitPoint=-1
    return Str[:SplitPoint],Str[SplitPoint:]

def get_phoncat(Str):
    return ('v' if Str[0] in sanskrit_phon.Vowels else 'c')
CategorisedSandhiRules=sandhi.create_sandhirules()


class Word:
    def __init__(self,Lexeme,InfForm):
        self.lexeme=Lexeme
        self.infform=InfForm
        StemSuffix=get_stem_suffix(self.infform)
        self.stem=StemSuffix[0]
        self.suffix=StemSuffix[1]
        self.suffixphoncat=get_phoncat(self.suffix)
        self.stemphoncat=get_phoncat(self.infform)
    def generate_sandhiforms(self,Stringify=False):
        SandhiResults=[]
        VCats={'vv','vvis'}; CCats=set(CategorisedSandhiRules.keys())-VCats
        for (Cat,SandhiRules) in CategorisedSandhiRules.items():
            if self.suffixphoncat == 'v' and Cat in VCats:
                for RelvSandhiRule in [ SandhiRule for SandhiRule in SandhiRules if SandhiRule.first==self.suffix ]:
                    SandhiResults.append((self.stem+RelvSandhiRule.result,RelvSandhiRule.second))
            elif self.suffixphoncat == 'c' and Cat in CCats:
                for RelvSandhiRule in [ SandhiRule for SandhiRule in SandhiRules if SandhiRule.first==self.suffix ]:
                    SandhiResults.append((self.stem+RelvSandhiRule.result,RelvSandhiRule.second))
        if any(self.infform.startswith(Vowel) for Vowel in sanskrit_phon.Vowels):
            SandhiResults=(self.infform[1:],SandhiResults)
        else:
            SandhiResults=(None,SandhiResults)
        if Stringify:
            Str='\n' if SandhiResults[0] is None else SandhiResults[0]+'\n'
            for (SandhiForm,FollowedBy) in SandhiResults[1]:
                if type(FollowedBy).__name__=='tuple':
                    for FollowedByEl in FollowedBy:
                        Str+='('+SandhiForm+', '+FollowedByEl+'), '
                else:
                    Str+='('+SandhiForm+', '+FollowedBy+'), '
                    
            return Str

        return SandhiResults
    def stringify_featvals(self,Delim=' '):
        StrEls=[]
        for Feat in self.__dict__.keys():
            Val=self.__dict__[Feat]
            if type(Val).__name__=='str':
                StrEls.append(Feat+': '+Val)
        Str=' / '.join(StrEls)
        return Str
    def print_featvals(self):
        print(self.stringify_featvals(self))

class InfLexeme(morph_univ.Lexeme):
    def __init__(self,Lemma,PoS):
        super().__init__(Lemma,PoS)
        StemSuffix=get_stem_suffix(self.lemma)
        self.stem=StemSuffix[0]
        self.suffix=StemSuffix[1]
        #self.paradigm=paradigms.__dict__[PoS]
        
    def determine_inftypes(self):
        if self.pos=='adj':
            InfTypes=paradigms.AdjInfTypes
            EndingsGenders=[ (Suffixes,_) for (Suffixes,_) in InfTypes.keys() if any(self.lemma.endswith(Ending) for Ending in Suffixes) ]
            Types=[InfTypes[EndingGender] for EndingGender in EndingsGenders]
                
        elif self.pos=='pronoun':
            if self.lemma=='adas':
                Type='adas'
            elif self.lemma.endswith('idam'):
                Type='PronIdam'
            elif self.lemma.endswith('ad'):
                Type='PronYadTad'
            elif self.lemma.endswith('im') or self.lemma.endswith('a'):
                Type='PronAorIm'
            elif self.person=='2':
                Type='PPron2p'
            elif self.person=='1':
                Type='PPron1p'
            else:
                Type='others'
            Types=[Type]
        
        elif self.pos=='noun':
            InfTypes=paradigms.NounInfTypes
            EndingsGenders=[ EndingGender for EndingGender in InfTypes.keys() if self.gender in EndingGender[1] and self.lemma.endswith(EndingGender[0]) ]
            Typse=[InfTypes[EndingGender] for EndingGender in EndingsGenders ]                
    #        if len(EndingsGenders)>=2:
  #              sys.stderr.write('\n'+self.lemma+': multiple infcats found, we are taking the first in the list, which is \n')
   #             print(ChosenEndingGender)

        elif self.pos=='verb':
            InfTypes=paradigms.VerbInfTypes
            Endings= [ Ending for Ending in InfTypes.keys() if self.lemma.endswith(Ending) ]
            Types=[InfTypes[Ending] for Ending in Endings]
                
        return Types
    
class NonInfLexeme(morph_univ.Lexeme):
    def __init__(self,Lemma,PoS):
        super().__init__(Lemma,PoS)

class NonInfWord(Word):
    def __init__(self,Lemma,PoS):
        super().__init__(NonInfLexeme(Lemma,PoS),Lemma)
        

        

class VerbLexeme(InfLexeme):
    def __init__(self,Lemma):
        super().__init__(Lemma,'verb')
        PotInfTypes=self.determine_inftypes()
        self.inftype=PotInfTypes[0] if PotInfTypes else None
        if self.inftype:
            self.conjpar=paradigms.verb[self.inftype]

    def inflect_all(self):
        if not self.inftype:
#            sys.stderr.write('no inftype for this verb, lemma: '+self.lemma+'\n')
            return []
        VerbWds=[]
        for (Tense,Table) in self.conjpar.items():
            for ((Pers,Num),Forms) in Table.items():
                for Form in Forms:
                    VerbWds.append(VerbWord(self,self.stem+Form,Pers,Num))
        return VerbWds

class VerbWord(Word):
    def __init__(self,Lexeme,InfForm,Person,Number):
        super().__init__(Lexeme,InfForm)
        self.lastchar=self.infform[-1]
        self.person=Person
        self.number=Number
#        self.sandhiforms=self.generate_sandhiforms()


class NominalLexeme(InfLexeme):
    def __init__(self,Lemma,PoS):
        super().__init__(Lemma,PoS)
        self.person=self.determine_person()
    def determine_person(self):
        if self.pos=='pronoun' and self.lemma=='aham':
            return '1'
        elif self.pos=='pronoun' and self.lemma=='tvam':
            return '2'
        else:
            return '3'
    
class AdjLexeme(NominalLexeme):
    def __init__(self,Lemma):
        super().__init__(Lemma,'adj')
        self.declpar=paradigms.adj
        PotInfTypes=self.determine_inftypes()
        self.inftype=PotInfTypes[0] if PotInfTypes else None
        
    def inflect_all(self):
        AdjWds=[]
        if self.inftype is None:
            return AdjWds
        for (Case,NumVarSets) in self.declpar[self.inftype].items():
            for Cnt,NumVarSet in enumerate(NumVarSets):
                if Cnt==0: Num='sg'
                elif Cnt==1: Num='dl'
                else: Num='pl'
                for NumVar in NumVarSet:
                    for Gender in 'm','f','n':
                        AdjWds.append(AdjWord(self,self.stem+NumVar,Gender,Case,Num,self.person))
        return AdjWds

class PronounLexeme(NominalLexeme):
    def __init__(self,Lemma):
        super().__init__(Lemma,'pronoun')
        PotInfTypes=self.determine_inftypes()
        self.inftype=PotInfTypes[0] if PotInfTypes else None

    def inflect_all(self):
        Wds=[]

        if self.inftype=='others':
            pass
        else:
            for (Gender,CaseNumVarSets) in paradigms.pronoun[self.inftype].items():
                for (Case, NumVarSets) in CaseNumVarSets.items():
                    for Cnt,NumVarSet in enumerate(NumVarSets):
                        if Cnt==0: Num='sg'
                        elif Cnt==1: Num='dl'
                        else: Num='pl'
                        for NumVar in NumVarSet:
                            try:
                                Wds.append(PronounWord(self,self.stem+NumVar,Gender,Case,Num))
                            except:
                                PronounWord(self,self.stem+NumVar,Gender,Case,Num)
                                
        return Wds


class Nominal(Word):
    def __init__(self,Lexeme,InfForm,Gender,Case,Number,Person):
        super().__init__(Lexeme,InfForm)
        self.case=Case
        self.number=Number
        self.person=Person

class PronounWord(Nominal):
    def __init__(self,Lex,InfForm,Gender,Case,Number):
        super().__init__(Lex,InfForm,Gender,Case,Number,Lex.person)
    
class NounLexeme(NominalLexeme):
    def __init__(self,Lemma,Gender):
        super().__init__(Lemma,'noun')
        self.gender=Gender
        PotInfTypes=self.determine_inftypes()
        self.inftype=PotInfTypes[0] if PotInfTypes else None
        if self.inftype:
            self.declpar=paradigms.noun[self.inftype]
    def inflect_all(self):
        NounWds=[]
        if not self.inftype:
            return []
        for (Case,NumVarSets) in self.declpar.items():
            for Cnt,NumVarSet in enumerate(NumVarSets):
                if Cnt==0: Num='sg'
                elif Cnt==1: Num='dl'
                else: Num='pl'
                for NumVar in NumVarSet:
                    NounWds.append(NounWord(self,self.stem+NumVar,self.gender,Case,Num,'3'))
        return NounWds                     


class NounWord(Nominal):
    def __init__(self,Lex,InfForm,Gender,Case,Number,Person):
        super().__init__(Lex,InfForm,Gender,Case,Number,Person)

class AdjWord(Nominal):
    def __init__(self,Lex,InfForm,Gender,Case,Number,Person):
        super().__init__(Lex,InfForm,Gender,Case,Number,Person)



#class Verb(morph_univ.Word):
 #   def __init__(self,Orth,Person,Number):
  #      super.__init__(Orth,'verb')
   #     self.person=Person
    #    self.number=


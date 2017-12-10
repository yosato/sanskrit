import imp,sys,time
from pythonlib_ys import morph_univ

import paradigms,sandhi,sanskrit_phon
imp.reload(paradigms)
imp.reload(sandhi)
imp.reload(sanskrit_phon)

def get_phoncat(Str):
    if not Str:
        return None
    return ('v' if Str[0] in sanskrit_phon.Vowels else 'c')
CategorisedSandhiRules=sandhi.create_sandhirules()


class Word:
    def __init__(self,Lexeme,InfForm):
        self.lexeme=Lexeme
        self.infform=InfForm
        self.stem=self.lexeme.stem
        self.suffix=self.lexeme.suffix
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
    def determine_inftypesuffix(self):
        def typesuffix_pairs(self,EndingsTypes):
            TypeSuffixPairs=[]
            for Endings,Type in EndingsTypes.items():
                for Ending in Endings:
                    if self.lemma.endswith(Ending):
                        TypeSuffixPairs.append((Type,Ending,))
                        break
            return TypeSuffixPairs
        
        if self.pos=='adj':
            InfTypes=paradigms.AdjInfTypes
            EndingsType={Endings:Type for (Endings,Type) in InfTypes.items() }
            TypeSuffixPairs=typesuffix_pairs(self,EndingsType)
                 
        elif self.pos=='pronoun':
            if self.lemma=='adas':
                TypeSuffixPairs=[('adas','adas')]
            elif self.lemma.endswith('idam'):
                TypeSuffixPairs=[('PronIdam','idam')]
            elif self.lemma.endswith('ad'):
                TypeSuffixPairs=[('PronYadTad','ad')]
            elif self.lemma.endswith('im') or self.lemma.endswith('a'):
                TypeSuffixPairs=[('PronAorIm','im')]
            elif self.person=='2':
                TypeSuffixPairs=[('PPron2p','adas')]
            elif self.person=='1':
                TypeSuffixPairs=[('PPron1p','adas')]
            else:
                TypeSuffixPairs=[]
        
        elif self.pos=='noun':
            InfTypes=paradigms.NounInfTypes
            EndingsType={Endings:Type for ((Endings,Genders),Type) in InfTypes.items() if self.gender in Genders }
            TypeSuffixPairs=typesuffix_pairs(self,EndingsType)
            
        elif self.pos=='verb':
            EndingsType=paradigms.VerbInfTypes
            TypeSuffixPairs=typesuffix_pairs(self,EndingsType)
        return TypeSuffixPairs
    
class NonInfLexeme(morph_univ.Lexeme):
    def __init__(self,Lemma,PoS):
        super().__init__(Lemma,PoS)
        self.stem=Lemma
        self.suffix=''
    def inflect_all(self):
        return [ NonInfWord(self.lemma,self.pos) ]

class NonInfWord(Word):
    def __init__(self,Lemma,PoS):
        super().__init__(NonInfLexeme(Lemma,PoS),Lemma)
        

class VerbLexeme(InfLexeme):
    def __init__(self,Lemma):
        super().__init__(Lemma,'verb')
        PotInfTypesSuffixes=self.determine_inftypesuffix()
        if PotInfTypesSuffixes:
            self.inftype,self.suffix=self.pick_right_typesuffix(PotInfTypesSuffixes)
            self.stem=self.lemma[:-len(self.suffix)]
            self.conjpar=paradigms.verb[self.inftype]
        else:
            raise ValueError('no inftype identified')
    def pick_right_typesuffix(self,PotInfTypesSuffixes):
        return PotInfTypesSuffixes[0]

    def inflect_all(self,FormOnly=False):
        if not self.inftype:
#            sys.stderr.write('no inftype for this verb, lemma: '+self.lemma+'\n')
            return []
        VerbWds=[]
        for (Tense,Table) in self.conjpar.items():
            for ((Pers,Num),Forms) in Table.items():
                for Form in Forms:
                    if not FormOnly:
                        VerbWds.append(VerbWord(self,self.stem+Form,Pers,Num))
                    else:
                        VerbWds.append(self.stem+Form)
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
        PotInfTypesSuffixes=self.determine_inftypesuffix()
        if PotInfTypesSuffixes:
            self.inftype,self.suffix=self.pick_right_typesuffix(PotInfTypesSuffixes)
            self.stem=self.lemma[:-len(self.suffix)]
            self.declpar=paradigms.adj[self.inftype]
        else:
            raise ValueError('no inftype identified')
    def pick_right_typesuffix(self,PotInfTypesSuffixes):
        return PotInfTypesSuffixes[0]
        
    def inflect_all(self,FormOnly=False):
        AdjWds=[]
        if self.inftype is None:
            return AdjWds
        for (Case,NumVarSets) in self.declpar.items():
            for Cnt,NumVarSet in enumerate(NumVarSets):
                if Cnt==0: Num='sg'
                elif Cnt==1: Num='dl'
                else: Num='pl'
                for NumVar in NumVarSet:
                    for Gender in 'm','f','n':
                        if not FormOnly:
                            AdjWds.append(AdjWord(self,self.stem+NumVar,Gender,Case,Num,self.person))
                        else:
                            AdjWds.append(self.stem+NumVar)
                    
        return AdjWds

class PronounLexeme(NominalLexeme):
    def __init__(self,Lemma):
        super().__init__(Lemma,'pronoun')
        PotInfTypesSuffixes=self.determine_inftypesuffix()
        if PotInfTypesSuffixes:
            self.inftype,self.suffix=self.pick_right_typesuffix(PotInfTypesSuffixes)
            self.stem=self.lemma[:-len(self.suffix)]
            self.conjpar=paradigms.pronoun[self.inftype]
        else:
            raise ValueError('no inftype identified')
    def pick_right_typesuffix(self,PotInfTypesSuffixes):
        return PotInfTypesSuffixes[0]

    def inflect_all(self,FormOnly=False):
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
                                if not FormOnly:
                                    Wds.append(PronounWord(self,self.stem+NumVar,Gender,Case,Num))
                                else:
                                    Wds.append(self.stem+NumVar)
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
        PotInfTypesSuffixes=self.determine_inftypesuffix()
        if PotInfTypesSuffixes:
            self.inftype,self.suffix=self.pick_right_typesuffix(PotInfTypesSuffixes)
            self.stem=self.lemma[:-len(self.suffix)]
            self.declpar=paradigms.noun[self.inftype]
        else:
            raise ValueError('no inftype identified')
    def pick_right_typesuffix(self,PotInfTypesSuffixes):
        return PotInfTypesSuffixes[0]
        
    def inflect_all(self,FormOnly=False):
        NounWds=[]
        if not self.inftype:
            return []
        for (Case,NumVarSets) in self.declpar.items():
            for Cnt,NumVarSet in enumerate(NumVarSets):
                if Cnt==0: Num='sg'
                elif Cnt==1: Num='dl'
                else: Num='pl'
                for NumVar in NumVarSet:
                    if not FormOnly:
                        NounWds.append(NounWord(self,self.stem+NumVar,self.gender,Case,Num,'3'))
                    else:
                        NounWds.append(self.stem+NumVar)
                    
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


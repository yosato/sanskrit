import imp
from pythonlib_ys import morph_univ

import paradigms,sandhi,sanskrit_phon
imp.reload(paradigms)
imp.reload(sandhi)
imp.reload(sanskrit_phon)

def get_stem_suffix(Str):
    if Str.endswith('at') or Str.endswith('in'):
        SplitPoint=-2
    else:
        SplitPoint=-1
    return Str[:SplitPoint],Str[SplitPoint:]

SandhiRulesIndexed=sandhi.create_indexed_sandhirules()

class Word:
    def __init__(self,Lexeme,InfForm):
        self.lexeme=Lexeme
        self.infform=InfForm
    def generate_sandhiforms(self):
        SandhiForms=[]
        if self.lastchar in SandhiRulesIndexed.keys():
            for SandhiRule in SandhiRulesIndexed[self.lastchar]:
                SandhiForms.append(self.infform[:-1]+SandhiRule.result)
        return SandhiForms
    
class VerbLexeme(morph_univ.Lexeme):
    def __init__(self,Lemma):
        super().__init__(Lemma,'verb')
        self.conjpar=paradigms.Verbs
    def conjugate_all(self):
        VerbWds=[]
        for (ConjType,Table) in self.conjpar:
            for ((Pers,Num),Forms) in Table:
                for Form in Forms:
                    VerbWds.append(VerbWord(self.lexeme,Form,Pers,Num))
        return VerbWds

class VerbWord(Word):
    def __init__(self,Lexeme,InfForm,Person,Number):
        self.lexeme=Lexeme
        self.infform=InfForm
        self.lastchar=self.infform[-1]
        self.person=Person
        self.number=Number
        self.sandhiforms=self.generate_sandhiforms()

        

class AdjLexeme(morph_univ.Lexeme):
    def __init__(self,Lemma):
        super().__init__(Lemma,'adj')
        StemSuffix=get_stem_suffix(self.lemma)
        self.stem=StemSuffix[0]
        self.suffix=StemSuffix[1]
        InfTypes=paradigms.NounAdjInfTypes
        TypeHash=next( (Suffixes,('m','f','n')) for (Suffixes,_) in InfTypes.keys() if self.suffix in Suffixes )
        self.inftype=paradigms.NounAdjInfTypes[TypeHash]
        self.declpar=paradigms.Adjs
    def decline_all(self):
        AdjWds=[]
        for (Case,NumVarSets) in self.declpar[self.inftype].items():
            for Cnt,NumVarSet in enumerate(NumVarSets):
                if Cnt==0: Num='sg'
                elif Cnt==1: Num='dl'
                else: Num='pl'
                for NumVar in NumVarSet:
                    AdjWds.append(AdjWord(self,self.stem+NumVar,Case,Num))
        return AdjWds

class NounLexeme(morph_univ.Lexeme):
    def __init__(self,Lemma,Gender):
        super().__init__(Lemma,'noun')
        self.gender=Gender
        StemSuffix=get_stem_suffix(self.lemma)
        self.stem=StemSuffix[0]
        self.suffix=StemSuffix[1]
        InfTypes=paradigms.NounAdjInfTypes
        self.inftype=InfTypes[next( Type for Type in InfTypes.keys() if Gender in Type[1] )]
        self.declpar=paradigms.Nouns
    def decline_all(self):
        NounWds=[]
        for (Case,NumVarSets) in self.declpar[self.inftype].items():
            for Cnt,NumVarSet in enumerate(NumVarSets):
                if Cnt==0: Num='sg'
                elif Cnt==1: Num='dl'
                else: Num='pl'
                for NumVar in NumVarSet:
                    NounWds.append(NounWord(self,self.stem+NumVar,self.gender,Case,Num))
        return NounWds                     


class NounWord(Word):
    def __init__(self,Lex,InfForm,Gender,Case,Number):
        self.lexeme=Lex
        self.infform=InfForm
        self.lastchar=self.infform[-1]
        self.case=Case
        self.number=Number
        self.sandhiforms=self.generate_sandhiforms()

class AdjWord(Word):
    def __init__(self,Lex,InfForm,Case,Number):
        self.lexeme=Lex
        self.infform=InfForm
        self.lastchar=self.infform[-1]
        self.case=Case
        self.number=Number
        self.sandhiforms=self.generate_sandhiforms()        




#class Verb(morph_univ.Word):
 #   def __init__(self,Orth,Person,Number):
  #      super.__init__(Orth,'verb')
   #     self.person=Person
    #    self.number=


from pythonlib_ys import morph_univ
from collections import defaultdict

SandhiRulesRaw=[
    ('a','u','o'),
    ('a','a','ā'),
        ('ā','a','ā'),
        ('a','ā','ā')
]

NounInfTypes={
    ('a','m'):'AM',
    ('a','n'):'AN',
    ('ā','f'):'AF'
    }

NounParadigms={
 'AM':{'nom':['as','au','ās'],'acc':['am','au','ān'],'inst':['ena','ābhyām','ais'],'dat':['āya','ābhyām','ābhyas'],'abl':['āt','ābhyām','ābhyas'],'gen':['masya','mayos','ānām'],'loc':['e','ayos','eṣu'],'voc':['a','au','ās']},

    'AN':{'nom':['am','ye','āni'],'acc':['am','ye','āni'],'inst':['ena','ābhyām','ais'],'dat':['āya','ābhyām','ābhyas'],'abl':['āt','ābhyām','ābhyas'],'gen':['asya','ayos','ānām'],'loc':['e','ayos','eṣu'],'voc':['a','ye','āni']},

 'AF':{'nom':['ā','e','ās'],'acc':['ām','e','ās'],'inst':['aya','ābhyām','abhis'],'dat':['āyai','ābhyām','ābhyas'],'abl':['ās','ābhyām','ābhyas'],'gen':['ās','ābhyām','ānām'],'loc':['āyam','ayos','āṣu'],'voc':['e','e','ās']}    
 }

class SandhiRule:
    def __init__(self,Fst,Scd,Result):
        self.first=Fst
        self.second=Scd
        self.result=Result

SandhiRulesIndexed=defaultdict(list)
for (Fst,Scd,Result) in SandhiRulesRaw:
    SandhiRulesIndexed[Fst].append(SandhiRule(Fst,Scd,Result))

class NounLexeme(morph_univ.Lexeme):
    def __init__(self,Lemma,Gender):
        super().__init__(Lemma,'noun')
        self.gender=Gender
        self.inftype=NounInfTypes[(self.lemma[-1],self.gender)]
        self.stem=self.lemma[:-1]
        self.declpar=NounParadigms
                     
    def decline_all(self):
        NounWds=[]
        for (Case,NumVars) in self.declpar[self.inftype].items():
            for Cnt,NumVar in enumerate(NumVars):
                if Cnt==0: Num='sg'
                elif Cnt==1: Num='dl'
                else: Num='pl'
                NounWds.append(NounWord(self,self.stem+NumVar,self.gender,Case,Num))
        return NounWds

class NounWord:
    def __init__(self,Lex,InfForm,Gender,Case,Number):
        self.lexeme=Lex
        self.infform=InfForm
        self.lastchar=self.infform[-1]
        self.case=Case
        self.number=Number
        self.sandhiforms=self.generate_sandhiforms()
    def generate_sandhiforms(self):
        SandhiForms=[]
        if self.lastchar in SandhiRulesIndexed.keys():
            for SandhiRule in SandhiRulesIndexed[self.lastchar]:
                SandhiForms.append(self.infform[:-1]+SandhiRule.result)
        return SandhiForms



#class Verb(morph_univ.Word):
 #   def __init__(self,Orth,Person,Number):
  #      super.__init__(Orth,'verb')
   #     self.person=Person
    #    self.number=


from collections import defaultdict
import sanskrit_phon

SandhiRulesVV={
    # a, A, i, ī, u, ū, ṛ, e, ai, o, au
    ('a','ā'): ('ā','ā','e','e','o','o','ar','ai','ai','au','au'),
    ('i','ī'): ('ya','yā','ī','ī','yu','yū','yṛ','ye','yai','yo','yau'),
    ('u','ū'): ('va','vā','vi','vī','ū','ū','vṛ','ve','vai','vo','vau'),
    ('ṛ',): ('ra','rā','ri','rī','rū','rū','ṝ','re','rai','ro','rau'),
    ('e',): ('e','a','a','a','a','a','a','a','a','a','a'),
    ('ai',): ('ā','ā','ā','ā','ā','ā','ā','ā','ā','ā','ā'),
    ('o',): ('o','ava','avi','avī','avū','avū','avṛ','ave','avai','avo','avau'),
    ('au',): ('āva','āvā','āvi','āvī','āvū','āvū','āvṛ','āve','āvai','āvo','āvau')
}

SandhiRulesCV={
    # vowels, l, ś, (y, r,  v, ,ṣ,	s, h)
    'k': ('g','g','g','g'),
    'ṭ': ('ḍ','ḍ','ḍ','ḍ'),
    't': ('d','l','c','d'),
    'p': ('b','b','b','b'),
    'aṅ': ('ṅṅ','','',''),
        'iṅ': ('ṅṅ','','',''),
        'uṅ': ('ṅṅ','','',''),
        'eṅ': ('ṅṅ','','',''),
        'oṅ': ('ṅṅ','','',''),
    'an': ('nn','','',''),
        'in': ('nn','','',''),
        'un': ('nn','','',''),
        'en': ('nn','','',''),
        'on': ('nn','','',''),
    'm': ('','ṃ','ṃ','ṃ')
}

SandhiRulesCC={
    #n/m, c, j, ṭ, d, else
    'k': ('ṅ','','g','','g','g'),
    'ṭ': ('ṅ','','ḍ','','ḍ','ḍ'),
    't': ('ṅ','c','j','ṭ','ḍ','d'),
    'p': ('m','','b','','b','b')
    
}

SandhiRulesNC={
    # c, j, ṭ, d, t, else
    'n':('ṃś','ñ','ṃṣ','ṇ','ṃs',''),
    'm':('ṃ','ṃ','ṃ','ṃ','ṃ','ṃ')
}

SandhiRulesVisarga={
    # vowels,r, (y,l,v,h), c, ṭ, t, (g,j,ḍ,b,n/m)  
    ('aḥ',): ('a','o','o','aś','aṣ','as','o'),
    ('āḥ',): ('ā','ā','ā','āś','āṣ','ās','ā'),
    ('i','e','u','e','ī','ū'): ('r','','r','ś','ṣ','s','r')
    }


class SandhiRule:
    def __init__(self,Fst,Scd,Result):
        self.first=Fst
        self.second=Scd
        self.result=Result

def create_indexed_sandhirules():
    SandhiRulesIndexed=defaultdict(list)
    for (Fsts,Results) in SandhiRulesVV.items():
        for Fst in Fsts:
            for (Scd,Result) in zip(['a','ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'e', 'ai', 'o', 'au'],Results):
                SandhiRulesIndexed[(Fst,Scd)].append(SandhiRule(Fst,Scd,Result))

    for (Fst,Results) in SandhiRulesCV.items():
        for (Scds,Result) in zip([sanskrit_phon.Vowels,('l',),('ś',),('y', 'r', 'v','ṣ','s','h')],Results):
            for Scd in Scds:
                SandhiRulesIndexed[(Fst,Scd)].append(SandhiRule(Fst,Scd,Result))

    for (Fst,Results) in SandhiRulesCC.items():
        for (Scds,Result) in zip([('n','m',),('c',),('j',),('t',),('d',),sanskrit_phon.Consts],Results):
            for Scd in Scds:
                SandhiRulesIndexed[(Fst,Scd)].append(SandhiRule(Fst,Scd,Result))

    for (Fst,Results) in SandhiRulesNC.items():
        for (Scds,Result) in zip([('c',),('j',),('ṭ',),('d',),('t'),sanskrit_phon.Consts],Results):
            for Scd in Scds:
                SandhiRulesIndexed[(Fst,Scd)].append(SandhiRule(Fst,Scd,Result))

    for (Fst,Results) in SandhiRulesVisarga.items():
        for (Scds,Result) in zip([('n','m',),('c',),('j',),('t',),('d',),sanskrit_phon.Consts],Results):
            for Scd in Scds:
                SandhiRulesIndexed[(Fst,Scd)].append(SandhiRule(Fst,Scd,Result))
                
    return SandhiRulesIndexed


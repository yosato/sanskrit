from pdb import set_trace
import sanskrit_phon

CCC=[('n','m',), 'c', 'j', 'ṭ', 'd']
CElseCC=tuple(set(sanskrit_phon.Consts)-set(CCC))
CCC.append(CElseCC)

CNC=['c', 'j', 'ṭ', 'd', 't']
CElseNC=tuple(set(sanskrit_phon.Consts)-set(CNC))
CNC.append(CElseCC)

VVis=[sanskrit_phon.Vowels, 'r', ('y','l','v','h'), 'c', 'ṭ', 't', ('g','j','ḍ','b',('n','m')) ]


SandhiRulesRaw={
'vv':(
    [ 'a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'e', 'ai', 'o', 'au'],
    {
        ('a','ā'): ('ā','ā','e','e','o','o','ar','ai','ai','au','au'),
    ('i','ī'): ('ya','yā','ī','ī','yu','yū','yṛ','ye','yai','yo','yau'),
    ('u','ū'): ('va','vā','vi','vī','ū','ū','vṛ','ve','vai','vo','vau'),
    ('ṛ',): ('ra','rā','ri','rī','ru','rū','ṝ','re','rai','ro','rau'),
    ('e',): ('e \'','a ā','a i','a ī','a u','a ū','a ṛ','a e','a ai','a o','a au'),
    ('ai',): ('ā a','ā ā' ,'ā i','ā ī','ā u','ā ū','ā ṛ','ā e','ā ai','ā o','ā au'),
    ('o',): ('o \'','avā','avi','avī','avu','avū','avṛ','ave','avai','avo','avau'),
    ('au',): ('āva','āvā','āvi','āvī','āvū','āvū','āvṛ','āve','āvai','āvo','āvau')
}
    ),

'cv':(
    
    [ sanskrit_phon.Vowels,'l', 'ś', ('y', 'r',  'v', 'ṣ','s', 'h',)],

    {
    ('k',): ('g','g','g','g'),
    ('ṭ',): ('ḍ','ḍ','ḍ','ḍ'),
    ('t',): ('d','l','c','d'),
    ('p',): ('b','b','b','b'),
    ('aṅ',): ('ṅṅ','','',''),
        ('iṅ',): ('ṅṅ','','',''),
        ('uṅ',): ('ṅṅ','','',''),
        ('eṅ',): ('ṅṅ','','',''),
        ('oṅ',): ('ṅṅ','','',''),
    ('an',): ('nn','','',''),
        ('in',): ('nn','','',''),
        ('un',): ('nn','','',''),
        ('en',): ('nn','','',''),
        ('on',): ('nn','','',''),
    ('m',): ('','ṃ','ṃ','ṃ')
}
    ),

'cc':(
    [('n','m',), 'c', 'j', 'ṭ', 'd'],
    {
    ('k',): ('ṅ','','g','','g','g'),
    ('ṭ',): ('ṅ','','ḍ','','ḍ','ḍ'),
    ('t',): ('ṅ','c','j','ṭ','ḍ','d'),
    ('p',): ('m','','b','','b','b')
    
}
    ),
    
'nc':(
['c', 'j', 'ṭ', 'd', 't'],
#        CNC,

{
    ('n',):('ṃś','ñ','ṃṣ','ṇ','ṃs',''),
    ('m',):('ṃ','ṃ','ṃ','ṃ','ṃ','ṃ')
},
    ),

'vvis':(   
[sanskrit_phon.Vowels, 'r', ('y','l','v','h'), 'c', 'ṭ', 't', ('g','j','ḍ','b',('n','m')) ],
{
    ('aḥ',): ('a','o','o','aś','aṣ','as','o'),
    ('āḥ',): ('ā','ā','ā','āś','āṣ','ās','ā'),
    ('i','e','u','e','ī','ū'): ('r','','r','ś','ṣ','s','r')
    },
)
}

class SandhiRule:
    def __init__(self,Fst,Scd,Result):
        self.first=Fst
        self.second=Scd
        self.result=Result

def create_sandhirules():
#    set_trace()
    SandhiRules={'vv':[],'cv':[],'cc':[],'nc':[],'vvis':[]}
    for (Pat,PhonPairs) in SandhiRulesRaw.items():
        ScdSets,FstsResults=PhonPairs
        for Fsts,Results in FstsResults.items():
            assert(len(ScdSets)==len(Results))
            for Fst in Fsts:
                for (Scds,Resul
                        SandhiRules[Pat].append(SandhiRule(Fst,Scd,Result))

    return SandhiRules


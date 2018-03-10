from pdb import set_trace
import sanskrit_phon
# i (Ligeia) do not understand why we have CCC & CNC and why they are partly overlapping
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
    ('e',): ("e '",'a ā','a i','a ī','a u','a ū','a ṛ','a e','a ai','a o','a au'),
    ('ai',): ('ā a','ā ā' ,'ā i','ā ī','ā u','ā ū','ā ṛ','ā e','ā ai','ā o','ā au'),
    ('o',): ("o '",'avā','avi','avī','avu','avū','avṛ','ave','avai','avo','avau'),
    ('au',): ('āva','āvā','āvi','āvī','āvū','āvū','āvṛ','āve','āvai','āvo','āvau')
}
    ),

'cv':(
    
    [ sanskrit_phon.Vowels,('k', 'g', ('c','ch'), ('j', 'jh'), ('ṭ', 'ṭh'), ('ḍ','ḍh'), ('t', 'th'), ('d','dh'), ('p','ph'), ('b', 'bh'), ('m','n'), ('y', 'v'), 'r', 'l', 'ś', ('ṣ','s'), 'h'],

    {
    ('k',): ('k' 'k','g','k','g','k', 'g','k', 'g', 'k', 'g', 'ṅ', 'g', 'g', 'k', 'g','k','k', ('gg h', 'g gh')),
    ('ṭ',): ('ṭ', 'ṭ', 'ḍ', 'ṭ', 'ḍ', 'ṭ', 'ḍ', 'ṭ', 'ḍ', 'ṭ', 'ḍ', 'ṇ', 'ḍ','ḍ', 'ḍ', 'ṭ', 'ṭ', ('ḍḍ h', 'ḍ ḍh')),
    ('t',): ('t', 't', 'd', 't', 'd', 't', 'd', 't', 'd', 't', 'd', 'n', 'd','d', 'l', ' cch', 't', ('dd h', 'd dh')),
    ('p',): ('p', 'p', 'b', 'p', 'b','p', 'b','p', 'b', 'p', 'b', 'm', 'b', 'b', 'b', 'p', 'p', ('bb h', 'b bh')),
    ('ṅ',): ('ṅṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ', 'ṅ'),
       
    ('n',): ('nn','n','n','ṃś', 'ñ', 'ṃṣ', 'ṇ', 'ṃs', 'n', 'n', 'n', 'n', 'n', 'n', 'n', 'ḷ', ('ś','ch'), 'n', 'n'),
    ('m',): ('m','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ','ṃ'),
    ('āḥ'): ('ā', 'āḥ', 'ā', 'āś', 'ā', 'āṣ', 'ā', 'ās' , 'ā', 'āḥ', 'ā', 'ā', 'ā', 'ā', 'ā', 'ā', 'aḥ','ā' ),
    ('aḥ'): (('a', 'o \''), 'aḥ', 'o', 'aś', 'o', 'aṣ', 'o', 'as', 'o', 'aḥ', 'o', 'o', 'o', 'o', 'o', 'o', 'aḥ', 'o'),
    ('ḥ', 'r'): ('r', 'ḥ', 'r', 'ś', 'r', 'ṣ', 'r', 's', 'r', 'ḥ', 'r', 'r', 'r', ' ', 'r', 'r', 'ḥ', 'r')
                            
}
    ),

'cc':(
    CCC,
    {
    ('k',): ('ṅ','','g','','g','g'),
    ('ṭ',): ('ṅ','','ḍ','','ḍ','ḍ'),
    ('t',): ('ṅ','c','j','ṭ','ḍ','d'),
    ('p',): ('m','','b','','b','b')
    
}
    ),
    
'nc':(
        CNC,

{
    ('n',):('ṃś','ñ','ṃṣ','ṇ','ṃs',''),
    ('m',):('ṃ','ṃ','ṃ','ṃ','ṃ','ṃ')
},
    ),

'vvis':(   VVis,
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
                for (Scds,Result) in zip(ScdSets,Results):
                    for Scd in Scds:
                        SandhiRules[Pat].append(SandhiRule(Fst,Scd,Result))

    return SandhiRules


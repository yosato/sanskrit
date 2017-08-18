#from pdb import set_trace
import copy

###===== pronouns and adjectives ==============

pronoun={
#yad/tad-replace ad wit:{
'PronYadTad':{
    'm':{
        'Nom':(['ah', 'o'],[ 'au' ],['e', 'āni'],),
        'Voc':([''],[''],[''],),
        'Acc':(['am'],['au'],['ān'],),
        'Inst':([ 'ena'], [ 'ābhyām'], ['aiḥ',  'air'],),
        'Dat':([ 'asmai'], [ 'ābhyām'], ['ebhyaḥ',  'ebhyo'],),
        'Abl':(['asmāt',  'asmād',  'asmādd'],[ 'ābhyām'], ['ebhyaḥ',  'ebhyo'],),
        'Gen':([ 'asya'], ['ayoḥ',  'ayor'],['eṣām',  'eṣāṃ'],),
        'Loc':(['asmin', 'asmim', 'asmiṃ'], ['ayoḥ', 'ayor'],['eṣu'],),
    },
    'f':{
        'Nom':(['ā'],['e'], ['āḥ'],),
        'Voc':[''],
        'Acc':(['ām'],['e'],['āḥ'],),
        'Inst':([ 'ayā'], [ 'ābhyām'], ['ābhiḥ',  'ābhir'],),
        'Dat':([ 'syai'], [ 'ābhyām'], ['ābhyaḥ',  'ābhyo'],),
        'Abl':([ 'asyāḥ'],[ 'ābhyām'], ['ābhyaḥ',  'ābhyo'],),
        'Gen':([ 'asyāḥ'], ['ayoḥ',  'ayor'],['āṣām',  'āṣāṃ'],),
        'Loc':([ 'asyām'], ['ayoḥ', 'ayor'],['āsu'],),
    },
    'n':{
        'Nom':(['ad', 'at'],['e'], [ 'āni'],),
        'Voc':([''],[''],[''],),
        'Acc':(['ad', 'at'],['e'],['āni'],),
        'Inst':([ 'ena'], [ 'ābhyām'], ['aiḥ',  'air'],),
        'Dat':([ 'asmai'], [ 'ābhyām'], ['ebhyaḥ',  'ebhyo'],),
        'Abl':(['asmāt',  'asmād',  'asmādd'],[ 'ābhyām'], ['ebhyaḥ',  'ebhyo'],),
        'Gen':([ 'asya'], ['ayoḥ',  'ayor'],['eṣām',  'eṣāṃ'],),
        'Loc':(['asmin', 'asmim', 'asmiṃ'], ['ayoḥ', 'ayor'],['eṣu'],),
    },
},
#idam replace the whole word idam with:{
'PronIdam':{
    'm':{
        'Nom':(['ayam'], ['imau'], ['ime'],),
        'Voc':([''],[''],[''],),
        'Acc':(['imam'],['imau'], ['imān'],),
        'Inst':(['anena'], ['ābhyām'],['ebhiḥ', 'ebhir'],),
        'Dat':(['asmai'], ['ābhyām'],['ebhyaḥ', 'ebhyo'],),
        'Abl':(['asmāt'], ['ābhyām'],['ebhyaḥ', 'ebhyo'],),
        'Gen':(['asya'], ['anayoḥ', 'anayor'], ['eṣām']),
        'Loc':(['asmin', 'asmim', 'asmiṃ'], ['anayoḥ', 'anayor'],['eṣu'],),
    },
    'f':{
        'Nom':(['iyam'],['ime'], ['imāḥ'],),
    'Voc':([''],[''],[''],),
        'Acc':(['imām'],['ime'],['imāḥ'],),
        'Inst':([ 'anayā'], [ 'ābhyām'], ['ābhiḥ',  'ābhir'],),
        'Dat':([ 'asyai'], [ 'ābhyām'], ['ābhyaḥ',  'ābhyo'],),
        'Abl':([ 'asyāḥ'],[ 'ābhyām'], ['ābhyaḥ',  'ābhyo'],),
        'Gen':([ 'asyāḥ'], ['ayoḥ',  'ayor'],['āṣām',  'āṣāṃ'],),
        'Loc':([ 'asyām'], ['ayoḥ', 'ayor'],['āsu'],),
    },


    'n':{

        'Nom':(['idam'],['ime'], [ 'imāni'],),
        'Voc':([''],[''],[''],),
        'Acc':(['idam'],['ime'],['imāni'],),
        'Inst':([ 'anena'], [ 'ābhyām'], ['aiḥ',  'air'],),
        'Dat':([ 'asmai'], [ 'ābhyām'], ['ebhyaḥ',  'ebhyo'],),
        'Abl':(['asmāt',  'asmād',  'asmādd'],[ 'ābhyām'], ['ebhyaḥ',  'ebhyo'],),
        'Gen':([ 'asya'], ['ayoḥ',  'ayor'],['eṣām',  'eṣāṃ'],),
        'Loc':(['asmin', 'asmim', 'asmiṃ'], ['ayoḥ', 'ayor'],['eṣu'],),
    },
},
# for the words :'sarva', 'anya', 'para', 'katama', 'viśva', 'sva', 'eka', 'itara', 'antara', uttara. 'adhara', pūrva
# replace final a 'with', for the pronoun 'kim', replace im with:
'PronAorIm' :{
    'm':{
        'Nom':(['a'], ['au'], ['e'],),
        'Voc':(['a'], ['au'], ['e'],),
        'Acc':(['am'],['au'], ['ān'],),
        'Inst':(['ena'], ['ābhyām'],['ebhiḥ', 'ebhir'],),
        'Dat':(['ai'], ['ābhyām'],['ebhyaḥ', 'ebhyo'],),
        'Abl':(['āt'], ['ābhyām'],['ebhyaḥ', 'ebhyo'],),
        'Gen':(['asya'], ['anayoḥ', 'anayor'], ['eṣām'],),
        'Loc':(['im', 'asmin', 'asmim', 'asmiṃ'], ['anayoḥ', 'anayor'],['eṣu'],),
    },
    'f':{
        'Nom':(['ā'],['e'], ['āḥ'],),
        'Voc':([''],[''],[''],),
        'Acc':(['ām'],['e'],['āḥ'],),
        'Inst':([ 'ayā'], [ 'ābhyām'], ['ābhiḥ',  'ābhir'],),
        'Dat':([ 'ayai'], [ 'ābhyām'], ['ābhyaḥ',  'ābhyo'],),
        'Abl':([ 'ayāḥ'],[ 'ābhyām'], ['ābhyaḥ',  'ābhyo'],),
        'Gen':([ 'ayāḥ'], ['ayoḥ',  'ayor'],['āṣām',  'āṣāṃ'],),
        'Loc':([ 'ayām'], ['ayoḥ', 'ayor'],['āsu'],),
    },


    'n':{

        'Nom':(['am'],['e'], [ 'āni'],),
        'Voc':(['am'],['e'], [ 'āni'],),
        'Acc':(['am'],['e'], [ 'āni'],),
        'Inst':([ 'ena'], [ 'ābhyām'], ['aiḥ',  'air'],),
        'Dat':([ 'ai'], [ 'ābhyām'], ['ebhyaḥ',  'ebhyo'],),
        'Abl':(['āt',  'asmād',  'asmādd'],[ 'ābhyām'], ['ebhyaḥ',  'ebhyo'],),
        'Gen':([ 'asya'], ['ayoḥ',  'ayor'],['eṣām',  'eṣāṃ'],),
        'Loc':(['im', 'asmin', 'asmim', 'asmiṃ'], ['ayoḥ', 'ayor'],['eṣu'],)
    },
},

#For the pronoun 'adas', replace entire word with:
    'adas' :{
        '':{

            'Nom':(['asau'], ['amū'], ['amī'],),
            'Voc':([''],[''],[''],),
            'Acc':(['amum'], ['amū'], ['amūn'],),
            'Inst':(['amunā'], ['amūbhyām'],['amībhiḥ', 'amībhir'],),
            'Dat':(['amuṣmai'], ['amūbhyām'],['amībhyaḥ', 'amībhyo'],),
            'Abl':(['amuñmāt'], ['amūbhyām'],['amībhyaḥ', 'amībhyo'],),
            'Gen':(['amuṣya'], ['amuyoḥ', 'amuyor'], ['amīṣām'],),
            'Loc':(['amuṣsmiṃ'], ['amuyoḥ', 'amuyor'],['amīṣu'],),
        }
        },

#personal pronouns
    'PPron1p':{
        '':{
        'Nom':(['aham', 'ahaṃ'],['āvām', 'nau'],['vayam', 'nah', 'no'],),
        'Acc':(['mām', 'mā'],['māvām', 'nau'],['asmān', 'asmāṃ', 'naḥ', 'no'],),
        'Inst':(['mayā'],['āvābhyām'],['asmābhiḥ', 'asmābhir'],),
        'Dat':(['me', 'mahyam', 'mahyaṃ'],['āvābhyām'],['naḥ', 'asmābhyām'],),
        'Abl':(['mat', 'me'],['āvābhyām', 'nau'],['asmat', 'naḥ', 'no'],),
        'Gen':(['mama', 'me'],['āvayoḥ', 'āvayor', 'nau'],['asmākam', 'naḥ', 'no'],),
        'loc':(['mayi'],['āvayoḥ', 'āvayor'],['asmāsu'],),
        }
    },

    'PPron2p':{
        '':{
            'Nom':(['tvam', 'tvaṃ'],['yuvām', 'vām'],['yūyam', 'vah', 'vo'],),
            'Acc':(['tvām', 'tvā'],['yuvām', 'vām'],['yūṣmān', 'asmāṃ', 'vaḥ', 'vo'],),
            'Inst':(['tvayā'],['yuvābhyām'],['yūṣmābhiḥ', 'asmābhir'],),
            'Dat':(['te', 'tubhyam', 'tubhyaṃ'],['yuvābhyām'],['naḥ', 'yūṣmābhyām'],),
            'Abl':(['tvat', 'tvat'],['yuvābhyām','vām'],['yūṣmat', 'vaḥ', 'vo'],),
            'Gen':(['tava', 'te'],['yuvayoḥ', 'yuvayor', 'vām'],['yūṣmākam', 'vaḥ', 'vo'],),
            'loc':(['tvayi'],['yuvayoḥ', 'yuvayor'],['yūṣmāsu'],),
        },
        },
    }


#====== Nouns ===========================

    
#The first form listed in each category is the classical 'suffix', and probably the most 'frequent'],
# All n can also be 'ṇ', all m can be ṃ (this is a general orthography 'rule', not only for suffixes but for words in general)
# The division in Gender is very artificial. It may not work with non-classical texts.
# format: AM:{nom:(['form1','form2','form3'],['dualform'],['pluralform'],),

NounAdjInfTypes={
    (('a',),('m',)):'AM',
    (('a',),('f','n')):'A',
        (('a',),('m','f','n')):'AAllGender',
    (('i','ī'),('m','f','n')):'i/īAllGender',
        (('u','ū'),('m','f','n')):'u/ūAllGender',
        (('s',),('m','f','n')):'sAllGender',
        (('n',),('m','f','n')):'nAllGender',
            (('at',),('m','f','n')):'atAllGender',
            (('in',),('m','f','n')):'inAllGender',
                (('ṛ',),('m','f','n')):'ṛAllGender'
}


noun={
'AM':{
'Nom':(['aḥ','o', 'u', 'ū', 'ā', 'e', 'aṃ' ],['au'],['āh', 'ā', 'ām', 'ām', 'ān', 'āni', 'e', 'aḥ', 'o', 'āyo', 'āya'],),
'Voc': (['a','ā', 'o', 'u', 'e'],['au'],['āh', 'ā', 'āho', 'āvo'],),
'Acc':(['am', 'u', 'a', 'o', 'e', 'ā', 'āṃ'], ['au'],['ān', 'āṃ', 'am', 'an', 'ā', 'ās', 'āḥ', 'a', 'e', 'i', 'u', 'āni', 'āna'],),
'Inst':(['ena', 'enā', 'inā', 'asā', 'ayā', 'āya', 'ā', 'a'], ['ābhyām'],['aiḥ', 'ai', 'ehi', 'ehī', 'ebhiḥ', 'ebhis', 'ebhī', 'abhiḥ', 'abhis', 'ābhi', 'ibhi'],),
'Dat': (['āya', 'aya', 'aye', 'ayā'],['ābhyām'], ['ebhyaḥ'],),
'Abl': (['āt', 'ā', 'a', 'āta', 'āto', 'ātu', 'ato', 'atu', 'atta', 'attaḥ', 'asmā'],['ābhyām'],[ 'ebhyaḥ'],),
'Gen':(['asya', 'asyā'], ['ayoḥ'], ['ānām', 'āna', 'ānam','ana', 'an', 'ān', 'ānu'],),
'Loc': (['e', 'i', 'aṃhi', 'aṃṣe', 'asmin', 'asmiṃ', 'asmi', 'esmiṃ', 'esmin', 'esmi'], ['ayoḥ'], ['eṣu', 'iṣu', 'asu', 'eṣū'],),
},
'A':{
'Nom': (['am', 'u', 'o', 'a', 'e', 'ā', 'āṃ'], ['e'], ['āni', 'a', 'ām', 'e', 'i', 'u', 'aṃṣi', 'ānī'],),
'Voc':(['am'],['e'], ['āni'],),
'Acc':(['am', 'u', 'o', 'a', 'e', 'ā', 'āṃ'], ['e'], ['āni', 'a', 'ām', 'e', 'i', 'u', 'aṃṣi', 'ānī'],),
'Inst': (['ena', 'enā', 'inā', 'asā', 'ayā', 'āya', 'ā', 'a'], ['ābhyām'],['aiḥ', 'ai', 'ehi', 'ehī', 'ebhiḥ', 'ebhis', 'ebhī', 'abhiḥ', 'abhis', 'ābhi', 'ibhi'],),
'Dat': (['āya', 'aya', 'aye', 'ayā'],['ābhyām'], ['ebhyaḥ'],),
'Abl': (['āt', 'ā', 'a', 'āta', 'āto', 'ātu', 'ato', 'atu', 'atta', 'attaḥ', 'asmā'],['ābhyām'],[ 'ebhyaḥ'],),
'Gen':(['asya', 'asyā'], ['ayoḥ'], ['ānām', 'āna', 'ānam','ana', 'an', 'ān', 'ānu']),
'Loc': (['e', 'i', 'aṃhi', 'aṃṣe', 'asmin', 'asmiṃ', 'asmi', 'esmiṃ', 'esmin', 'esmi'], ['ayoḥ'], ['eṣu', 'iṣu', 'asu', 'eṣū'],),
},
'Ā':{
'Nom': (['ā', 'a', 'as', 'ām', 'u', 'ī'],[ 'e'], ['āḥ', 'ā', 'a', 'āyo', 'āyā', 'āye','āvo', 'e', 'o', 'āni'],),
'Voc':(['e', 'i', 'a'], ['e'], ['āḥ', 'āho'],),
'Acc': (['ām', 'am', 'aṃ', 'a', 'ā', 'u', 'ān', 'āram'], ['e'],['āḥ',  'ā', 'a', 'āyo', 'āyā', 'āye','āvo', 'e', 'o', 'āni','ān', 'āṃ'],),
'Inst': (['ayā', 'ena', 'ayena', 'ayāye', 'āe', 'āyi', 'aye', 'āyai', 'āye', 'āyā'], ['ābhyām'], ['ābhiḥ', 'ābhi', 'āhi', 'ais', 'ebhiḥ', 'ehi'],),
'Dat': (['āyai', 'āye', 'āe', 'āyi', 'aye', 'āyai'], ['ābhyām'], ['ābhyaḥ'],),
'Abl': (['āyāḥ', 'ayā', 'āyām', 'āe', 'āyi', 'aye', 'āt', 'ātas', 'āto', 'āta', 'atas', 'atu'], ['ayoḥ'], ['ābhyaḥ'],),
'Gen': (['āyāḥ', 'āe', 'āyi', 'aye', 'ayā', 'āyāṃ', 'asyā', 'asya'], ['ayoḥ'], ['ānām', 'āna'],),
'Loc': (['āyām', 'āyaṃ', 'e', 'ayām', 'āyaṃ', 'āe', 'āyi', 'aye'], ['ayoḥ'], ['āsu', 'āsū', 'asu'],),
},
'i/īAllGender':{
    'Nom':(['iḥ', 'ī', 'i', 'iṃ', 'im', 'īm', 'is','īs', 'ā'],['ī', 'iṇī', 'yau', 'inau'],['ayaḥ', 'īṇi', 'inā', 'ina', 'īno', 'īna', 'īnī','yas', 'ya','yā', 'yās', 'īn', 'īṃ', 'īs', 'iyas', 'iyo', 'iya', 'iyā', 'īo', 'īyo', 'īyā', 'īya', 'īye', 'iye', 'ī', 'is', 'iḥ']),
'Voc':(['e', 'i', 'ī'],['ī', 'iṇī', 'yau'], ['yaḥ', 'īṇi', 'ī', 'īho'],),
'Acc': (['im', 'iṃ', 'i', 'īm', 'īṃ', 'y', 'ī', 'is', 'īnam', 'iya', 'iyaṃ'],['ī', 'iṇī', 'inau'],['in', 'īḥ', 'īṇi', 'inā', 'ina', 'īno', 'īna', 'īnī','yas', 'ya','yā', 'yās', 'īn', 'īṃ', 'īs', 'iyas', 'iyo', 'iya', 'iyā', 'īo', 'īyo', 'īyā', 'īya', 'īye', 'iye', 'ī', 'is', 'iḥ'] ,),
'Inst':(['inā','yā', 'i', 'yā', 'ina', 'īnā', 'īye', 'īya', 'īyo', 'īyena'],['ibhyām', 'ibhyāṃ'],['ibhiḥ', 'ibḥir', 'ībhiḥ', 'ībhir', 'īhi', 'ībhis', 'ībhi', 'ihi', 'ibhi'],),
'Dat':(['aye', 'yai', 'iṇe', 'yai', 'ayi', 'īye','iye', 'īyai', 'ye'],['ibhyām', 'ibhyāṃ'], ['ibhyaḥ', 'ībhyaḥ','ibhyas', 'ībhyas'],),
'Abl':(['eḥ', 'yāḥ', 'iṇaḥ', 'ito', 'iye', 'īya', 'īyo', 'yā', 'īto'],['ibhyām', 'ibhyāṃ'], ['ibhyaḥ', 'ībhyaḥ','ibhyas', 'ībhyas','īhi'],),
'Gen':(['eḥ', 'yāḥ', 'iṇaḥ', 'yāḥ', 'isya', 'e', 'yus', 'inaḥ', 'īye', 'īya', 'īyu', 'iyo', 'yā', 'yas', 'aye', 'ayi', 'īyaṃ'],['yoḥ', 'yor', 'ṇoḥ'], ['īnām', 'īṇām', 'īnāṃ', 'īṇāṃ', 'inā'],),
'Loc':(['au', 'yām', 'yāṃ', 'iṇi', 'iṃ', 'yau', 'e', 'esmiṃ','ismiṃ', 'ismi', 'iyi', 'iye', 'iyā', 'īyo', 'ya', 'īyaṃ', 'iyaṃ'],['yoḥ', 'yor', 'ṇoḥ'], ['iṣu', 'īṣu', 'īṣū'],),
},
'u/ūAllGender':{
'Nom':(['uḥ', 'ūḥ', 'u', 'v', 'ū', 'uṃ'],['ū', 'unī','vau'], ['vaḥ', 'ūni', 'avaḥ', 'ava', 'uvaḥ', 'uno', 'ūna', 'ūni', 'uni', 'uṃ', 'um', 'ūs', 'ūḥ', 'uḥ', 'ūyo', 'uyo', 'ū', 'u'],),
'Voc':(['o', 'u', 'ū'], ['ū', 'unī', 'vau'], ['vaḥ', 'ūni', 'ūḥ', 'o'],),
'Acc':(['um', 'ūm', 'u', 'ū', 'um', 'uyam', 'unam', 'una', 'uvam', 'us'],['ū', 'vau', 'unī'],['ūḥ', 'ūn', 'ūni', 'avaḥ', 'avo', 'ava', 'uno', 'ūna', 'uni', 'ūni', 'uṃ', 'um', 'ūyo', 'uyo', 'ū', 'u'],),
'Inst':(['unā', 'vā', 'ūnā', 'ūye', 'uye', 'ūya', 'uya', 'ūyo', 'ūyaṃ', 'ūyam'], ['ubhyām', 'ubhyāṃ'], ['ubhiḥ', 'ubhir', 'ūbhiḥ', 'ūbhir', 'ūhi', 'ūbhi', 'uhi', 'ubhi', 'ubhīr'],),
'Dat':(['ave', 'vai', 'une','ūye', 'uye', 'ūya', 'uya', 'ūyo', 'ūyaṃ', 'ūyam'], ['ubhyām', 'ubhyāṃ'],['ubhyaḥ', 'ubhyas', 'ūbhyaḥ', 'ūbhyas'],),
'Abl':(['yoḥ', 'yor', 'oḥ', 'or', 'unaḥ', 'uno', 'ūye', 'uye', 'ūya', 'uya', 'ūyo', 'ūyaṃ', 'ūyam'], ['ubhyām', 'ubhyāṃ'], ['ubhyaḥ', 'ubhyas', 'ūbhyaḥ', 'ūbhyas'],),
'Gen':(['yoḥ', 'yor', 'oḥ', 'or', 'vaḥ', 'unaḥ','uno', 'usya', 'ūsya', 'o','ūye', 'uye', 'ūya', 'uya', 'ūyo', 'ūyaṃ', 'ūyam'],['voḥ', 'unoḥ'],['unām', 'ūnāṃ', 'ūnam', 'unāṃ', 'ūna'],),
'Loc':(['vām', 'vāṃ', 'enau', 'au', 'uni', 'une', 'usmin', 'usmiṃ', 'ūye', 'uye', 'ūya', 'uya', 'ūyo', 'ūyaṃ', 'ūyam'],['voḥ', 'unoḥ'], ['uṣu', 'ūṣu'],),
},
'sAllGender':{
'Nom':(['ḥ','asas', 'aso', 'asā', 'asaṃ', 'asa', 'ā', 'as', 'aṃ', 'am'],['sī'], ['ṃsi', 'ūṃsi', 'āṃsi', 'ās', 'āni', 'ānī'],),
'Voc':(['ḥ', 'asa'],['sī'],['ṃsi', 'ūṃsi', 'āṃsi'],),
'Acc':(['ḥ','am', 'aṃ', 'ām'], ['sī'], ['ṃsi', 'ūṃsi', 'āṃsi', 'āni', 'ānī'],),
'Inst':(['sā', 'ṣā', 'ena'],['obhyām', 'obhyāṃ', 'rbhyām', 'rbhyāṃ'], ['obhiḥ', 'rbhiḥ', 'obhiṛ', 'rbhir', 'ais'],),
'Dat':(['se'], ['obhyām', 'obhyāṃ', 'rbhyām', 'rbhyāṃ', 'ābhyāṃ'], ['obhyaḥ', 'rbhyaḥ'],),
'Abl':(['saḥ', 'āto', 'ato', 'ātu', 'atu'],  ['obhyām', 'obhyāṃ', 'rbhyām', 'rbhyāṃ'], ['obhyaḥ', 'rbhyaḥ'],),
'Gen':(['saḥ', 'asya'], ['soḥ', 'sor'], ['sām', 'ṣām', 'ānām', 'asānām'],),
'Loc':(['si', 'asmi', 'ase'], ['soḥ', 'sor'], ['ḥsu', 'eṣu'],),
},
'nAllGender':{
'Nom':(['ā', 'ah','o', 'u', 'a', 'ās', 'ānu','nas'],['ānau', 'nī'], ['ānaḥ', 'āni', 'ās', 'ā', 'āna', 'nas', 'ānaḥ', 'āna'],),
'Voc':(['an', 'a', 'ā','e'], ['nī', 'ānau'], ['ānaḥ', 'āni'],),
'Acc':(['ānam', 'a', 'aṃ', 'am', 'ā', 'āna', 'anam', 'anu', 'ana'],['ānau', 'nī'], ['aḥ', 'āni', 'ā', 'ānaḥ', 'āna'],),
'Inst':(['ñā', 'nā','ena', 'ina', 'nena', 'anena'], ['abhyām'],['abhiḥ', 'abhir', 'ehi', 'ānais', 'ānehi', 'ābhis'],),
'Dat':(['ñe','ne'], ['abhyām'], ['abyaḥ'],),
'Abl':(['ñaḥ', 'naḥ', 'a', 'nātu'],[ 'abhyām'], ['abhyaḥ'],),
'Gen':(['ñāḥ', 'naḥ','asya', 'ana', 'āno', 'ānas', 'ānasya', 'nasya'], ['ñoḥ', 'noḥ'], ['ñām', 'nām', 'ānaṃ'],),
'Loc':(['ani', 'ni', 'ñi', 'i', 'e','ne', 'āne', 'āni'],['ñoḥ', 'noḥ'], ['asu', 'āneṣu', 'neṣu'],),
},
'atAllGender':{
'Nom':(['an', 'ān', 'nta', 'ntā', 'ntu', 'nto', 'ntaḥ', 'at', 'tas', 'ta', 'tu', 'as', 'ā'], ['ntau', 'atī'], ['ntaḥ', 'nti', 'ntās','ntā', 'nti', 'ntāni'],),
'Voc':(['an', 'nta', 'at', 'tā'],['ntau'], ['ntaḥ'],),
'Acc':(['ntam', 'at','āntam', 'stām', 'nta', 'ntaṃ', 'tam', 'tu', 'tāṃ', 'a'],['ntau', 'atī'],['taḥ', 'anti','ntān', 'ntām', 'ntā', 'ntāni', 'āni', 'a', 'ā', 'tā', 'tāni' ],),
'Inst':(['tā', 'ntena', 'ena'], ['adbhyām'], ['dhiṛ', 'dbhir', 'ntais', 'ntebhis'],),
'Dat':(['te'], ['adbhyām'],['adhyaḥ', 'ntebhyas']),
'Abl':(['taḥ'],['adbhyām'],['adbhyaḥ', 'adbhyo'],),
'Gen':(['taḥ', 'to', 'ntasya', 'asya', 'tu'], ['toḥ'],['tām', 'ntānām', 'ntānam', 'ntān', 'ntān', 'tānām', 'ntam', 'tu'],),
'Loc':(['ti', 'āyām', 'te'], ['toḥ'], ['tsu', 'nteṣu'],),
},
'inAllGender':{
'Nom':(['ī', 'i'], ['inau', 'inī'],['inaḥ', 'īni'],),
'Voc':(['in', 'i'], ['inau', 'inī'], ['inaḥ', 'īni'],),
'Acc':(['inam', 'i'], ['inau', 'inī'], ['inaḥ', 'īni'],),
'Inst':(['inā'],['ibhyām'],['ibhi', 'ibhir', 'ṛhi'],),
'Dat':(['ine'], ['ibhyām'],['ibhyaḥ', 'ibhyo'],),
'Abl':([ 'usmā'], ['ibhyām'],['ibhyaḥ', 'ibhyo'],),
'Gen':(['inaḥ', 'uno'], ['inoḥ'], ['inām', 'unām', 'ṛṇām'],),
'Loc':(['ini'], ['inoḥ'], ['iṣu', 'ṛṣu'],),
},
'ṛAllGender':{
'Nom':(['ā', 'a', 'uḥ', 'u', 'ās'],['ārau'], ['āraḥ', 'ā'],),
'Voc':(['aḥ', 'ar','e'], ['ārau'], ['āraḥ'],),
'Acc':(['āram', 'āṃ', 'ā', 'ṛ', 'uṃ', 'u'],['ārau'],['ṛn', 'ṛm'],),
'Inst':(['rā', 'ṛṇā', 'unā'],['ṛbhyām'],['ṛbhiḥ', 'ṛbhir'],),
'Dat':(['re'],['ṛbhyām'],['ṛbhyaḥ', 'ṛbhyo'],),
'Abl':(['uḥ', 'ur'],['ṛbhyām'], ['ṛbhyaḥ', 'ṛbhyo'],),
'Gen':(['uḥ', 'ur', 'aro', 'u', 'uno'], ['oḥ', 'or'],['ṛṇām', 'unām'],),
'Loc':(['ari'],['oḥ', 'or'], ['ṛṣu'],)
}, #the preceding may apply to all genders
'ṛ':{
'Nom':(['ṛ', 'rā', 'rī'],['ṛṇī'],['ṛṇi'],),
'Voc':(['ṛ', 'e'],['ṛṇī'],['ṛṇi'],),
'Acc':(['ṛ', 'ām'],['ṛṇī'],['ṛṇi','ṛn', 'ṛm'],),
'Inst':(['ṛṇā'],['ṛbhyām'],['ṛbhiḥ', 'ṛbhir', 'ṛhi'],),
'Dat':(['ṛṇe', 'are'], ['ṛbhyām'],['ṛbhiḥ', 'ṛbhir'],),
'Abl':(['ṛṇaḥ', 'ṛno'],['ṛbhyām'], ['ṛbhyaḥ', 'ṛbhyo'],),
'Gen':(['ṛṇaḥ', 'ṛno', 'aro', 'u'], ['ṛhoḥ'], ['ṛṇām'],),
'Loc':(['ṛṇi'],['ṛṇoḥ'],['ṛṣu'],),
}

}

def combine_inftypes(Inf1,Inf2):
    Combined={}
    for (Feat,FormSets1) in Inf1.items():
        FormSets2=Inf2[Feat]
        Combined[Feat]=tuple( [ set(FormSets1[i]).union(set(FormSets2[i])) for i in range(3) ] )
    return Combined
        

AdjExtra=combine_inftypes(noun['A'],noun['AM'])
adj=copy.copy(noun)
adj[('AAllGender')]=AdjExtra

##============ Verb ========================


#the preceding may apply to all genders# rules to generate conjugated forms from the third person singular verb stem
# example: 
# in the StarDict wordlist we find the form akṣati , remove ti and attach all suffixes

# !!forms in 'te', e.g. ucyate are 'passive', attach ONLY the MiddlePassive suffixes below

# please add to the wordlist the following forms: 'avocat', 'avocanti', 'āha', āhuḥ. they are frequently occurring 'aorists', no need to conjugate 'them', other persons do not occur.

verb={
#ati/otiVerb:{
'PresentActive':{
('1','sg',):[ 'mi'],
('2','sg',):[ 'si'],
('3','sg',):['ti'],
('1','dl',):['vaḥ', 'vas'],
('2','dl',):['thaḥ', 'thas'],
('3','dl',):['tas', 'taḥ'],
('1','pl',):['mas', 'maḥ', 'āmaḥ'],
('2','pl',):[  'tha'],
('3','pl',):['nti', 'anti'],
},
'PresentMiddlePassive':{
('1','sg',):[ 'e'],
('2','sg',):[ 'se'],
('3','sg',):['te'],
('1','dl',):['vahe', 'ḥvahe'],
('2','dl',):['ethe', 'āthe'],
('3','dl',):['et', 'ate'],
('1','pl',):['mahe', 'ḥmahe', 'āmahe'],
('2','pl',):[  'dhve'],
('3','pl',):['te', 'nte'],
},
'ImpfActive':{  # for the imperfect put an 'a' before the stem:['e'.g. 'bhavati'> 'abhavan', when stem starts in 'vowl', sandhi applies:[  'akṣati' > ākṣan
('1','sg',):['m', 'am'],
('2','sg',):[ 's'],
('3','sg',):['t'],
('1','dl',):[ 'va'],
('2','dl',):[ 'tam'],
('3','dl',):[ 'tām'],
('1','pl',):['ma', 'āma'],
('2','pl',):[  'ta'],
('3','pl',):['n', 'an', 'ur', 'uḥ'],
},
'ImpfMiddlePassive':{  # for the imperfect put an 'a' before the stem:['e'.g. 'bhavati'> 'abhavan', when stem starts in 'vowl', sandhi applies:[  'akṣati' > ākṣan
('1','sg',):[ 'i'],
('2','sg',):['thās', 'thāḥ'],
('3','sg',):['ta'],
('1','dl',):[ 'vahi'],
('2','dl',):['ethām', 'āthām'],
('3','dl',):['etām', 'ātam'],
('1','pl',):['mahi', 'āmahi'],
('2','pl',):[  'dhvam'],
('3','pl',):['nta', 'ata'],
},
'OptativeActive':{
('1','sg',):['eyam', 'yām'],
('2','sg',):['es', 'yās'],
('3','sg',):['et', 'yāt'],
('1','dl',):['eva', 'yāva'],
('2','dl',):['etam', 'yātam'],
('3','dl',):['etām', 'yātām'],
('1','pl',):['emam' 'yāma'],
('2','pl',):['eha', 'yāta'],
('3','pl',):['eyur', 'eyuḥ', 'yur', 'yuḥ'],
},
'OptativeMiddlePassive':{ 
('1','sg',):['eya', 'īya'],
('2','sg',):['ethās', 'ethāḥ', 'īthās'],
('3','sg',):['eta', 'īta'],
('1','dl',):['evahi', 'īvahi'],
('2','dl',):['eyāthām', 'īyāthām'],
('3','dl',):['eyātam', 'īyātām'],
('1','pl',):['emahi', 'īmahi'],
('2','pl',):['dhvam', 'īdhvam'],
('3','pl',):['eran', 'īran'],
},
'ImperativeActiv':{

('1','sg',):[ 'āni'],
('2','sg',):['dhi', 'hi'],
('3','sg',):['tu'],
('1','dl',):['āva'],
('2','dl',):['tam'],
('3','dl',):[ 'tām'],
('1','pl',):[ 'āma'],
('2','pl',):[ 'ta'],
('3','pl',):['ntu', 'antu'],
},
'ImperativeMiddlepassiv':{

('1','sg',):[ 'ai'],
('2','sg',):[ 'sva'],
('3','sg',):['tām'],
('1','dl',):['āvahai'],
('2','dl',):['ethām', 'ātham'],
('3','dl',):['ethām', 'ātām'],
('1','pl',):[ 'āmahai'],
('2','pl',):['dhvam'],
('3','pl',):['ntām', 'atām'],
}


}


 
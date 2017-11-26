#from pdb import set_trace
import copy

###===== pronouns and adjectives ==============

pronoun={
#yad/tad-replace ad with:
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

NounInfTypes={
    (('a',),('m')):'AM',
    (('a',),('n')):'AN',
    (('ā',),('f')):'Ā',
    (('ī'),('m')):'īM',
    (('ī'),('f')):'īF',
    (('i'),('m')):'iM'
    (('i'),('n')):'iN'
    (('i'),('f')):'iF',
        (('u','ū'),('m','f','n')):'u/ūAllGender',
        (('an',),('m','f','n')):'anAllGender',
            (('vat',),('m','n')):'vatMN',
            (('vat',),('f')):'vatF',
            (('in',),('m','n')):'inMN',
            (('in',),('f')):'inF',
                (('ṛ',),('m','f','n')):'ṛAllGender',
                    (('t'),('m', 'f')):'tMF',
                    (('t'),('n')):'tN',
                    (('ad'),('m', 'f')):'adMF',
                    (('d'),('m', 'f')):'dMF',
                    (('d'),('n')):'dN',
                    (('c'),('f', 'm')):'cFM',
                    (('j'),('f', 'm')):'jFM',
                    (('as'),('f', 'm', 'n')):'asAllGender',
                    (('ṣ', 's'),('f', 'm')):'ṣsFM',
                    (('ś'),('f', 'm')):'śFM',
                    (('ś','s',),('m','f','n')):'sAllGender',
                    (('dik'),('f')):'dikF',
                    (('ṃs'),('m')):'ṃsM',
                    (('go'),('f')):'go',
                    (('nau'),('f')):'nau'
}


noun={


    'AM':{
'Nom':(['aḥ'],['au'],['āh'],),
'Voc': (['a'],['au'],['āh'],),
'Acc':(['am'], ['au'],['ān'],),
'Inst':(['ena'], ['ābhyām'],['aiḥ'],),
'Dat': (['āya'],['ābhyām'], ['ebhyaḥ'],),
'Abl': (['āt'],['ābhyām'],[ 'ebhyaḥ'],),
'Gen':(['asya'], ['ayoḥ'], ['ānām'],),
'Loc': (['e'], ['ayoḥ'], ['eṣu'],),
},
'AN':{
'Nom': (['am'], ['e'], ['āni'],),
'Voc':(['am'],['e'], ['āni'],),
'Acc':(['am'], ['e'], ['āni'],),
'Inst': (['ena'], ['ābhyām'],['aiḥ'],),
'Dat': (['āya'],['ābhyām'], ['ebhyaḥ'],),
'Abl': (['āt'],['ābhyām'],[ 'ebhyaḥ'],),
'Gen':(['asya'], ['ayoḥ'], ['ānām']),
'Loc': (['e'], ['ayoḥ'], ['eṣu'],),
},
'Ā':{
'Nom': (['ā'],[ 'e'], ['āḥ'],),
'Voc':(['e'], ['e'], ['āḥ'],),
'Acc': (['ām'], ['e'],['āḥ'],),
'Inst': (['ayā'], ['ābhyām'], ['ābhiḥ'],),
'Dat': (['āyai'], ['ābhyām'], ['ābhyaḥ'],),
'Abl': (['āyāḥ'], ['ayoḥ'], ['ābhyaḥ'],),
'Gen': (['āyāḥ'], ['ayoḥ'], ['ānām'],),
'Loc': (['āyām'], ['ayoḥ'], ['āsu'],),
},
'īM':{
'Nom': (['īḥ'], ['ī'], ['iyaḥ'],),
'Voc':(['ī'], ['ī'], ['iyaḥ'],),
'Acc':(['iyam'], ['ī'], ['iyīn'],),
'Inst':(['iyā'], ['iybhyām'], ['iybhiḥ'],),
'Dat':(['iye'], ['iybhyām'], ['iybhyaḥ'],),
'Abl':(['iyaḥ'], ['iybhyām'], ['iybhyaḥ'],),
'Gen':(['iyaḥ'], ['iyoḥ'], ['iyām'],),
'Loc':(['iyau'], ['iyoḥ'], ['iṣu'],),
},
'īF':{
'Nom':(['ī','īḥ'],['yau', 'iyau'],['yaḥ', 'iyaḥ'],),
'Voc':(['i', 'īḥ'],['yau', 'iyau'],['yaḥ', 'iyaḥ']),),
'Acc': (['īṃ','iyam'],['yau', 'iyau'],['īḥ','iyaḥ'],),
'Inst':(['yā','īya'],['ībhyām', 'ibhyām'],['ībhiḥ'],),
'Dat':(['yai','iye', 'iyai'],['ībhyām', 'ibhyām'], ['ībhyaḥ'],),
'Abl':(['yāḥ', 'iyaḥ', 'iyāḥ'],['ībhyām', 'ibhyām'], [ 'ībhyaḥ'],),
'Gen':(['yāḥ', 'iyaḥ', 'iyāḥ'],['yoḥ', 'iyoḥ'], ['īnām','iyām'],),
'Loc':(['yām', 'iyi', 'iyām'],['yoḥ', 'iyoḥ'], ['īṣu'],),
},
'iM':{
    'Nom':(['iḥ'],['ī'],['ayaḥ']),
'Voc':(['e'],['ī'], ['yaḥ'],),
'Acc': (['im'],['ī'],['īn'] ,),
'Inst':(['inā'],['ibhyām'],['ibhiḥ'],),
'Dat':(['aye'],['ibhyām'], ['ibhyaḥ'],),
'Abl':(['eḥ'],['ibhyām'], ['ibhyaḥ'],),
'Gen':(['eḥ'],['yoḥ'], ['īnām'],),
'Loc':(['au'],['yoḥ'], ['iṣu'],),
},
'iN':{
    'Nom':(['i'],['īṇī'],['īṇi'],),
'Voc':(['i'],['īṇī'],['īṇi'],),
'Acc': (['i'],['īṇī'],['īṇi'],),
'Inst':(['iṇā'],['ibhyām'],['ibhiḥ'],),
'Dat':(['iṇe'],['ibhyām'], ['ibhyaḥ'],),
'Abl':(['iṇaḥ'],['ibhyām'], ['ibhyaḥ'],),
'Gen':(['iṇaḥ'],['iṇoḥ'], ['īṇām'],),
'Loc':(['iṇi'],['iṇoḥ'], ['iṣu'],),
},
'iF':{
    'Nom':(['iḥ'],['ī'],['ayaḥ'],),
'Voc':(['e'],['ī'], ['yaḥ'],),
'Acc': (['im'],['ī'],['iḥ'] ,),
'Inst':(['inā'],['ibhyām'],['ibhiḥ'],),
'Dat':(['aye', 'yai'],['ibhyām'], ['ibhyaḥ'],),
'Abl':(['eḥ', 'yāḥ'],['ibhyām'], ['ibhyaḥ'],),
'Gen':(['eḥ', 'yāḥ'],['yoḥ'], ['īnām'],),
'Loc':(['au', 'yām'],['yoḥ'], ['iṣu'],),
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
'anAllGender':{
'Nom':(['ā', 'a'],['ānau', 'nī', 'anau'], ['ānaḥ', 'āni'],),
'Voc':(['an', 'a'], ['nī', 'ānau'], ['ānaḥ', 'āni'],),
'Acc':(['ānam', 'a'],['ānau', 'nī'], ['aḥ', 'āni', 'ā', 'ānaḥ', 'āna'],),
'Inst':(['nā'], ['abhyām'],['abhiḥ'],),
'Dat':(['ne'], ['abhyām'], ['abyaḥ'],),
'Abl':(['naḥ'],[ 'abhyām'], ['abhyaḥ'],),
'Gen':(['naḥ'], ['noḥ'], ['nām'],),
'Loc':(['ani', 'ni'],[ 'noḥ'], ['asu'],),
},
'vatMN':{
'Nom':(['vān','vat'],['vāṃsau', 'uṣī'],['āṃṣaḥ','āṃsi'],),
'Voc':(['van','vat'],['vāṃsau', 'uṣī'],['āṃṣaḥ','āṃsi'],),
'Acc':(['vāṃsam','vat'],['vāṃsau', 'uṣī'],['āṃsi','uṣaḥ'],),
'Inst':(['uṣā'], ['vadbhyām'], ['vadbhiḥ'],),
'Dat':(['uṣe'], ['vadbhyām'],['vadbhyaḥ']),
'Abl':(['uṣaḥ'],['vadbhyām'],['vadbhyaḥ'],),
'Gen':(['uṣaḥ'], ['uṣoḥ'],['uṣām'],),
'Loc':(['uṣi'], [ 'uṣoḥ'], ['vatsu'],),
},
'vatF':{
'uṣNom':(['uṣī','uṣīḥ'],['uṣyau', 'uṣiyau'],['uṣyaḥ', 'uṣiyaḥ'],),
'uṣVoc':(['uṣi', 'uṣīḥ'],['uṣyau', 'uṣiyau'],['uṣyaḥ', 'uṣiyaḥ']),),
'uṣAcc': (['uṣīṃ','uṣiyam'],['uṣyau', 'uṣiyau'],['uṣīḥ','uṣiyaḥ'],),
'uṣInst':(['uṣyā','uṣīya'],['uṣībhyām', 'uṣibhyām'],['uṣībhiḥ'],),
'uṣDat':(['uṣyai','uṣiye', 'uṣiyai'],['uṣībhyām', 'uṣibhyām'], ['uṣībhyaḥ'],),
'uṣAbl':(['uṣyāḥ', 'uṣiyaḥ', 'uṣiyāḥ'],['uṣībhyām', 'uṣibhyām'], [ 'uṣībhyaḥ'],),
'uṣGen':(['uṣyāḥ', 'uṣiyaḥ', 'uṣiyāḥ'],['uṣyoḥ', 'uṣiyoḥ'], ['uṣīnām','uṣiyām'],),
'uṣLoc':(['uṣyām', 'uṣiyi', 'uṣiyām'],['uṣyoḥ', 'uṣiyoḥ'], ['uṣīṣu'],),
},
'inMN':{
'Nom':(['ī', 'i'], ['inau', 'inī'],['inaḥ', 'īni'],),
'Voc':(['in', 'i'], ['inau', 'inī'], ['inaḥ', 'īni'],),
'Acc':(['inam', 'i'], ['inau', 'inī'], ['inaḥ', 'īni'],),
'Inst':(['inā'],['ibhyām'],['ibhi', 'ibhir', 'ṛhi'],),
'Dat':(['ine'], ['ibhyām'],['ibhyaḥ', 'ibhyo'],),
'Abl':([ 'usmā'], ['ibhyām'],['ibhyaḥ', 'ibhyo'],),
'Gen':(['inaḥ', 'uno'], ['inoḥ'], ['inām', 'unām', 'ṛṇām'],),
'Loc':(['ini'], ['inoḥ'], ['iṣu', 'ṛṣu'],),
},
'inF':{
'inNom':(['inī','inīḥ'],['inyau', 'iniyau'],['inyaḥ', 'iniyaḥ'],),
'inVoc':(['ini', 'inīḥ'],['inyau', 'iniyau'],['inyaḥ', 'iniyaḥ']),),
'inAcc': (['inīṃ','iniyam'],['inyau', 'iniyau'],['inīḥ','iniyaḥ'],),
'inInst':(['inyā','inīya'],['inībhyām', 'inibhyām'],['inībhiḥ'],),
'inDat':(['inyai','iniye', 'iniyai'],['inībhyām', 'inibhyām'], ['inībhyaḥ'],),
'inAbl':(['inyāḥ', 'iniyaḥ', 'iniyāḥ'],['inībhyām', 'inibhyām'], [ 'inībhyaḥ'],),
'inGen':(['inyāḥ', 'iniyaḥ', 'iniyāḥ'],['inyoḥ', 'iniyoḥ'], ['inīnām','iniyām'],),
'inLoc':(['inyām', 'iniyi', 'iniyām'],['inyoḥ', 'iniyoḥ'], ['inīṣu'],),
},
'ṛAllGender':{
'Nom':(['ṛ', 'rā', 'rī','ā', 'a', 'uḥ', 'u', 'ās'],['ṛṇī','ārau'], ['ṛṇi','āraḥ', 'ā'],),
'Voc':(['ṛ', 'e','aḥ', 'ar','e'], ['ṛṇī','ārau'], ['ṛṇi', 'āraḥ'],),
'Acc':(['āram', 'āṃ', 'ā', 'ṛ', 'uṃ', 'u'],['ṛṇī','ārau'],['ṛṇi','ṛn', 'ṛm'],),
'Inst':(['rā', 'ṛṇā', 'unā'],['ṛbhyām'],['ṛbhiḥ', 'ṛbhir','ṛhi'],),
'Dat':(['re','ṛṇe', 'are'],['ṛbhyām'],['ṛbhyaḥ', 'ṛbhyo'],),
'Abl':(['uḥ', 'ur','ṛṇaḥ', 'ṛno'],['ṛbhyām'], ['ṛbhyaḥ', 'ṛbhyo'],),
'Gen':(['uḥ', 'ur', 'aro', 'u', 'uno','ṛṇaḥ', 'ṛno'], ['oḥ', 'or','ṛhoḥ'],['ṛṇām', 'unām'],),
'Loc':(['ari','ṛṇi'],['oḥ', 'or','ṛṇoḥ'], ['ṛṣu'],)
}, #the preceding may apply to all genders
'tMF':{
'Nom': (['t'], ['tau'], ['taḥ']),
'Voc':(['t'], ['tau'], ['taḥ']),
'Acc':(['tam'], ['tau'], ['taḥ']),
'Inst':(['tā'], ['dbhyām'], ['dbhiḥ', 'dbhir']),
'Dat':(['te'], ['dbhyām'], ['dbhyaḥ', 'dbhyo', 'dbhyaś']),
'Abl':(['taḥ'], ['dbhyām'], ['dbhyaḥ', 'dbhyo', 'dbhyaś']),
'Gen':(['taḥ'], ['toḥ'], ['tām']),
'Loc':(['ti'], ['toḥ'], ['tsu']),
},
'tN':{
'Nom': (['t'], ['tī'], ['nti']),
'Voc':(['t'], ['tī'], ['nti']),
'Acc':(['t'], ['tī'], ['nti']),
'Inst':(['tā'], ['dbhyām'], ['dbhiḥ', 'dbhir']),
'Dat':(['te'], ['dbhyām'], ['dbhyaḥ']),
'Abl':(['taḥ'], ['dbhyām'], ['dbhyaḥ']),
'Gen':(['taḥ'], ['toḥ'], ['tām']),
'Loc':(['ti'], ['toḥ'], ['tsu']),
},
'adMF':{
'Nom': (['ad'], ['adau'], ['adaḥ']),
'Voc':(['ad'], ['adau'], ['adaḥ']),
'Acc':(['adam', 'adām'], ['adau'], ['adaḥ', 'ado', 'adāḥ']),
'Inst':(['adā'], ['adbhyām'], ['adbhiḥ', 'adbhir']),
'Dat':(['ade'], ['adbhyām'], ['adbhyaḥ', 'adbhyo', 'adbhyaś']),
'Abl':(['adaḥ'], ['adbhyām'],['adbhyaḥ', 'adbhyo', 'adbhyaś']),
'Gen':(['adaḥ'], ['adoḥ'], ['adām', 'adānāṃ']),
'Loc':(['adi'], ['adoḥ'], ['atsu']),
},
'dMF':{
'Nom': (['d'], ['dau'], ['daḥ']),
'Voc':(['d'], ['dau'], ['daḥ']),
'Acc':(['dam'], ['dau'], ['daḥ']),
'Insd':(['dā'], ['dbhyām'], ['dbhiḥ', 'dbhir']),
'Dad':(['de'], ['dbhyām'], ['dbhyaḥ', 'dbhyo', 'dbhyaś']),
'Abl':(['daḥ'], ['dbhyām'], ['dbhyaḥ', 'dbhyo', 'dbhyaś']),
'Gen':(['daḥ'], ['doḥ'], ['dām']),
'Loc':(['di'], ['doḥ'], ['dsu']),
},
'dN':{
'Nom': (['d'], ['dī'], ['di']),
'Voc':(['d'], ['dī'], ['di']),
'Acc':(['d'], ['dī'], ['di']),
'Insd':(['dā'], ['dbhyām'], ['dbhiḥ', 'dbhir']),
'Dad':(['de'], ['dbhyām'], ['dbhyaḥ']),
'Abl':(['daḥ'], ['dbhyām'], ['dbhyaḥ']),
'Gen':(['daḥ'], ['doḥ'], ['dām']),
'Loc':(['di'], ['doḥ'], ['dsu']),
},
'cFM':{
'Nom': (['k'], ['cau'], ['caḥ']),
'Voc':(['k'], ['cau'], ['caḥ']),
'Acc':(['cam', 'cām'], ['cau'], ['acaḥ', 'co', 'cāḥ']),
'Inst':(['cā'], ['gbhyām'], ['gbhiḥ', 'gbhir']),
'Dat':(['ce'], ['gbhyām'], ['gbhyaḥ', 'gbhyo', 'gbhyaś']),
'Abl':(['caḥ'], ['gbhyām'], ['gbhyaḥ', 'gbhyo', 'gbhyaś']),
'Gen':(['caḥ'], ['coḥ'], ['cām']),
'Loc':(['ci'], ['coḥ'], ['kṣu']),
},
'jFM':{
'Nom': (['k'], ['jau'], ['jaḥ']),
'Voc':(['k'], ['jau'], ['jaḥ']),
'Acc':(['jam', 'jām'], ['jau'], ['jaḥ', 'jo']),
'Inst':(['jā'], ['gbhyām'], ['gbhiḥ', 'gbhir']),
'Dat':(['je'], ['gbhyām'], ['gbhyaḥ', 'gbhyo', 'gbhyaś']),
'Abl':(['jaḥ'], ['gbhyām'], ['gbhyaḥ', 'gbhyo', 'gbhyaś']),
'Gen':(['jaḥ'], ['joḥ'], ['jām']),
'Loc':(['ji'], ['joḥ'], ['kṣu']),
},
'asAllGender':{
'Nom': (['at','asas', 'aso', 'asā', 'asaṃ','as', 'o'], ['asau'], ['asaḥ', 'ās']),
'Voc':(['at', 'asa','asaṃ', 'aṃ'], ['asau'], ['asaḥ']),
'Acc':(['asam', 'asām'], ['asau'], ['asaḥ', 'āni', 'ānī', 'a']),
'Inst':(['asā', 'ena'], ['adbhyām', 'ābhyāṃ'], ['adbhiḥ', 'ais']),
'Dat':(['ase'], ['adbhyām'], ['adbhyat', 'adbhyo', 'adbhyas']),
'Abl':(['asaḥ', 'āto', 'ato', 'atu'], ['adbhyām'], ['adbhyat', 'adbhyo', 'adbhyas']),
'Gen':(['asaḥ', 'asya'], ['asoḥ'], ['asām', 'asānām','ānāṃ']),
'Loc':(['asi', 'ase', 'e', 'asmi'], ['asoḥ'], ['atsu', 'eṣu']),
},
'ṣsFM':{
'Nom': (['ḥ'], ['ṣau'], ['ṣaḥ']),
'Voc':(['ḥ'], ['ṣau'], ['ṣaḥ']),
'Acc':(['ṣam', 'ṣām'], ['ṣau'], ['ṣaḥ', 'ṣo']),
'Inst':(['ṣā'], ['rbhyām'], ['rbhiḥ', 'rbhir']),
'Dat':(['ṣe'], ['rbhyām'], ['rbhyaḥ', 'rbhyo', 'rbhyaś']),
'Abl':(['ṣaḥ'], ['rbhyām'], ['rbhyaḥ', 'rbhyo', 'rbhyaś']),
'Gen':(['ṣaḥ'], ['ṣoḥ'], ['ṣām']),
'Loc':(['ṣi'], ['ṣoḥ'], ['ḥṣu']),
},
'śFM':{
'Nom': (['ṭ'], ['śau'], ['ṣaṭ']),
'Voc':(['ṭ'], ['ṣau'], ['ṣaṭ']),
'Acc':(['ṣam', 'ṣām'], ['ṣau'], ['ṣaṭ', 'ṣo']),
'Inst':(['ṣā'], ['ḍbhyām'], ['ḍbhiṭ', 'ḍbhiḍ']),
'Dat':(['ṣe'], ['ḍbhyām'], ['ḍbhyaṭ', 'ḍbhyo', 'ḍbhyaś']),
'Abl':(['ṣaṭ'], ['ḍbhyām'], ['ḍbhyaṭ', 'ḍbhyo', 'ḍbhyaś']),
'Gen':(['ṣaṭ'], ['ṣoṭ'], ['ṣām']),
'Loc':(['ṣi'], ['ṣoṭ'], ['ṭṣu']),
},
'sAllGender':{
'Nom':(['ḥ'],['sī'], ['ṃsi'],),
'Voc':(['ḥ'],['sī'],['ṃsi'],),
'Acc':(['ḥ'], ['sī'], ['ṃsi'],),
'Inst':(['sā'],['obhyām'], ['obhiḥ'],),
'Dat':(['se'], ['obhyām'], ['obhyaḥ'],),
'Abl':(['saḥ'],  ['obhyām'], ['obhyaḥ'],),
'Gen':(['saḥ'], ['soḥ'], ['sām'],),
'Loc':(['si'], ['soḥ'], ['ḥsu'],),
},
'dikF':{
'Nom': (['dik'], ['diśau'], ['diśaḥ']),
'Voc':(['dik'], ['diśau'], ['diśaḥ']),
'Acc':(['diśam'], ['diśau'], ['diśaḥ']),
'Inst':(['diśā'], ['digbhyām'], ['digbhiḥ']),
'Dat':(['diśe'], ['digbhyām'], ['digbhyaḥ']),
'Abl':(['diśaḥ'], ['digbhyām'], ['digbhyaḥ']),
'Gen':(['diśaḥ'], ['diśoḥ'], ['diśām']),
'Loc':(['diśi'], ['diśoḥ'], ['dikṣu']),
},
'ṃsM':{
'Nom': (['mān'], ['māṃsau'], ['māṃsaḥ','māṃṣaḥ']),
'Voc':(['man'], ['māṃsau'], ['māṃsaḥ','māṃṣaḥ']),
'Acc':(['māṃsam','mṣam'], ['māṃsau'],['ṃsaḥ','mṣaḥ']),
'Inst':(['ṃsā','mṣā'], ['ṃbhyām','mbhyām'], ['ṃbhiḥ','mbhiḥ']),
'Dat':(['ṃse','mṣe'], ['ṃbhyām', 'ṃbhyām'], ['ṃbhyaḥ','mbhyām']),
'Abl':(['ṃsaḥ','mṣaḥ'], ['ṃbhyām','mbhyām'], ['ṃbhyaḥ','mbhyaḥ']),
'Gen':(['ṃsaḥ','mṣaḥ'], ['ṃsoḥ','ṃṣoḥ'], ['ṃsām', 'ṃṣāṃ']),
'Loc':(['ṃsi', 'ṃṣi'], ['ṃsoḥ','ṃṣoḥ'], ['ṃsu','mṣu']),
},
'go':{
'Nom': (['gauḥ'], ['gāvau'], ['gavaḥ'],),
'Voc':(['gauḥ'], ['gāvau'], ['gavaḥ'],),
'Acc': (['gām'], ['gāvau'], ['gavaḥ'],),
'Inst': (['gavā'], ['gobhyām'], ['gobhiḥ'],),
'Dat': (['gave'], ['gobhyām'], ['gobhyaḥ'],),
'Abl': (['goḥ'], ['gobhyām'], ['gobhyaḥ'],),
'Gen': (['goḥ'], ['gavoḥ'], ['gavām'],),
'Loc': (['gavi'], ['gaoḥ'], ['goṣu'],),
},
'nau':{
'Nom': (['nauḥ'], ['nāvau'], ['nāvaḥ'],),
'Voc':(['nauḥ'], ['nāvau'], ['nāvaḥ'],),
'Acc': (['nāvam'], ['nāvau'], ['nāvaḥ'],),
'Inst': (['nāvā'], ['naubhyām'], ['naubhiḥ'],),
'Dat': (['nāve'], ['naubhyām'], ['naubhyaḥ'],),
'Abl': (['nāvaḥ'], ['naubhyām'], ['naubhyaḥ'],),
'nen': (['nāvaḥ'], ['navoḥ'], ['nāvām'],),
'Loc': (['nāvi'], ['navoḥ'], ['nauṣu'],),
}
}
def combine_inftypes(Inf1,Inf2):
    Combined={}
    for (Feat,FormSets1) in Inf1.items():
        FormSets2=Inf2[Feat]
        Combined[Feat]=tuple( [ set(FormSets1[i]).union(set(FormSets2[i])) for i in range(3) ] )
    return Combined

AdjInfTypes=copy.copy(NounInfTypes)
AdjInfTypes[('a',),('m','f','n')]='AAllGender'


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
#atiVerb:{
'PresentActive':{
('1','sg',):[ 'āmi'],
('2','sg',):[ 'asi'],
('3','sg',):['ati'],
('1','dl',):['āvaḥ'],
('2','dl',):['athaḥ'],
('3','dl',):['ataḥ'],
('1','pl',):['āmaḥ'],
('2','pl',):['atha'],
('3','pl',):['anti'],
},
'PresentMiddlePassive':{
('1','sg',):[ 'e'],
('2','sg',):[ 'ase'],
('3','sg',):['ate'],
('1','dl',):['āvahe'],
('2','dl',):['ethe'],
('3','dl',):['ate'],
('1','pl',):['āmahe'],
('2','pl',):['adhve'],
('3','pl',):['ante'],
},
'ImpfActive':{  # for the imperfect put an 'a' before the stem:['e'.g. 'bhavati'> 'abhavan', when stem starts in 'vowl', sandhi applies:[  'akṣati' > ākṣan
('1','sg',):['am'],
('2','sg',):[ 'aḥ'],
('3','sg',):['at'],
('1','dl',):[ 'āva'],
('2','dl',):[ 'atam'],
('3','dl',):[ 'atām'],
('1','pl',):['āma'],
('2','pl',):['ata'],
('3','pl',):['an'],
},
'ImpfMiddlePassive':{  # for the imperfect put an 'a' before the stem:['e'.g. 'bhavati'> 'abhavan', when stem starts in 'vowl', sandhi applies:[  'akṣati' > ākṣan
('1','sg',):[ 'e'],
('2','sg',):['athāḥ'],
('3','sg',):['ata'],
('1','dl',):[ 'āvahi'],
('2','dl',):['ethām'],
('3','dl',):['etām'],
('1','pl',):['āmahi'],
('2','pl',):['adhvam'],
('3','pl',):['nta'],
},
'OptativeActive':{
('1','sg',):['eyam'],
('2','sg',):['eḥ'],
('3','sg',):['et'],
('1','dl',):['eva'],
('2','dl',):['etam'],
('3','dl',):['etām'],
('1','pl',):['ema'],
('2','pl',):['eta'],
('3','pl',):['yuḥ'],
},
'OptativeMiddlePassive':{ 
('1','sg',):['eya'],
('2','sg',):['ethāḥ'],
('3','sg',):['eta'],
('1','dl',):['evahi'],
('2','dl',):['eyāthām'],
('3','dl',):['eyātam'],
('1','pl',):['emahi'],
('2','pl',):['edhvam'],
('3','pl',):['eran'],
},
'ImperativeActiv':{

('1','sg',):['āni'],
('2','sg',):['a'],
('3','sg',):['atu'],
('1','dl',):['āva'],
('2','dl',):['atam'],
('3','dl',):['atām'],
('1','pl',):['āma'],
('2','pl',):['ata'],
('3','pl',):['antu'],
},
'ImperativeMiddlepassiv':{

('1','sg',):[ 'ai'],
('2','sg',):[ 'asva'],
('3','sg',):['atām'],
('1','dl',):['āvahai'],
('2','dl',):['ethām'],
('3','dl',):['etām'],
('1','pl',):[ 'āmahai'],
('2','pl',):['adhvam'],
('3','pl',):['antām'],
}


}


 

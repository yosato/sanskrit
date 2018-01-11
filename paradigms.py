#from pdb import set_trace
import copy
from collections import OrderedDict

###===== pronouns and adjectives ==============

pronoun={
#yad/tad-replace ad with:
'PronTad':{
    'm':{
        'Nom':(['sah', 'so'],[ 'tau' ],['te', 'tāni'],),
        'Voc':([''],[''],[''],),
        'Acc':(['tam'],['tau'],['ān'],),
        'Inst':([ 'tena'], [ 'tābhyām'], ['taiḥ'],),
        'Dat':([ 'tasmai'], [ 'tābhyām'], ['tebhyaḥ'],),
        'Abl':(['tasmāt',  'tasmād'],[ 'ābhyām'], ['tebhyaḥ'],),
        'Gen':([ 'tasya'], ['tayoḥ',  'tayor'],['teṣām',  'teṣāṃ'],),
        'Loc':(['tasmin', 'tasmim', 'tasmiṃ'], ['tayoḥ'],['teṣu'],),
    },
    'f':{
        'Nom':(['sā'],['te'], ['tāḥ'],),
        'Voc':([''],[''],[''],),
        'Acc':(['tām'],['te'],['tāḥ'],),
        'Inst':([ 'tayā'], [ 'tābhyām'], ['tābhiḥ'],),
        'Dat':([ 'tasyai'], [ 'tābhyām'], ['tābhyaḥ'],),
        'Abl':([ 'tasyāḥ'],[ 'tābhyām'], ['tābhyaḥ'],),
        'Gen':([ 'tasyāḥ'], ['tayoḥ'],['āṣām',  'tāṣāṃ'],),
        'Loc':([ 'tasyām'], ['tayoḥ'],['tāsu'],),
    },
    'n':{
        'Nom':(['tad', 'tat'],['te'], [ 'tāni'],),
        'Voc':([''],[''],[''],),
        'Acc':(['tad', 'tat'],['te'],['tāni'],),
            'Inst':([ 'tena'], [ 'ābhyām'], ['taiḥ'],),
            'Dat':([ 'tasmai'], [ 'ābhyām'], ['tebhyaḥ'],),
            'Abl':(['tasmāt'],[ 'tābhyām'], ['tebhyaḥ'],),
            'Gen':([ 'tasya'], ['tayoḥ',  'tayor'],['teṣām',  'teṣāṃ'],),
            'Loc':(['tasmin', 'tasmim', 'tasmiṃ'], ['tayoḥ'],['teṣu'],),
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

NounInfTypes=OrderedDict({
    (('a',),('m',)):'AM',
    (('a',),('n',)):'AN',
    (('ā',),('f',)):'Ā',
    (('ī'),('m',)):'īM',
    (('ī'),('f',)):'īF',
    (('i'),('m',)):'iM',
    (('i'),('n',)):'iN',
    (('i'),('f',)):'iF',
        (('u','ū'),('m','f','n')):'u/ūAllGender',
        (('an',),('m','f','n')):'anAllGender',
            (('vat',),('m','n')):'vatMN',
            (('vat',),('f',)):'vatF',
            (('in',),('m','n')):'inMN',
            (('in',),('f',)):'inF',
                (('ṛ',),('m','f','n')):'ṛAllGender',
                    (('t',),('m', 'f')):'tMF',
                    (('t',),('n',)):'tN',
                    (('ad',),('m', 'f')):'adMF',
                    (('d',),('m', 'f')):'dMF',
                    (('d',),('n',)):'dN',
                    (('c',),('f', 'm')):'cFM',
                    (('j',),('f', 'm')):'jFM',
                    (('as',),('f', 'm', 'n')):'asAllGender',
                    (('ṣ', 's'),('f', 'm')):'ṣsFM',
                    (('ś',),('f', 'm')):'śFM',
                    (('ś','s',),('m','f','n')):'sAllGender',
                    (('dik',),('f',)):'dikF',
                    (('ṃs',),('m',)):'ṃsM',
                    (('go',),('f',)):'go',
                    (('nau',),('f',)):'nau'
})


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
'Voc':(['i', 'īḥ'],['yau', 'iyau'],['yaḥ', 'iyaḥ'],),
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
'uṣVoc':(['uṣi', 'uṣīḥ'],['uṣyau', 'uṣiyau'],['uṣyaḥ', 'uṣiyaḥ'],),
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
'inVoc':(['ini', 'inīḥ'],['inyau', 'iniyau'],['inyaḥ', 'iniyaḥ'],),
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
'Nom': (['t'], ['tau'], ['taḥ'],),
'Voc':(['t'], ['tau'], ['taḥ'],),
'Acc':(['tam'], ['tau'], ['taḥ'],),
'Inst':(['tā'], ['dbhyām'], ['dbhiḥ', 'dbhir'],),
'Dat':(['te'], ['dbhyām'], ['dbhyaḥ', 'dbhyo', 'dbhyaś'],),
'Abl':(['taḥ'], ['dbhyām'], ['dbhyaḥ', 'dbhyo', 'dbhyaś'],),
'Gen':(['taḥ'], ['toḥ'], ['tām'],),
'Loc':(['ti'], ['toḥ'], ['tsu'],),
},
'tN':{
'Nom': (['t'], ['tī'], ['nti'],),
'Voc':(['t'], ['tī'], ['nti'],),
'Acc':(['t'], ['tī'], ['nti'],),
'Inst':(['tā'], ['dbhyām'], ['dbhiḥ', 'dbhir'],),
'Dat':(['te'], ['dbhyām'], ['dbhyaḥ'],),
'Abl':(['taḥ'], ['dbhyām'], ['dbhyaḥ'],),
'Gen':(['taḥ'], ['toḥ'], ['tām'],),
'Loc':(['ti'], ['toḥ'], ['tsu'],),
},
'adMF':{
'Nom': (['ad'], ['adau'], ['adaḥ'],),
'Voc':(['ad'], ['adau'], ['adaḥ'],),
'Acc':(['adam', 'adām'], ['adau'], ['adaḥ', 'ado', 'adāḥ'],),
'Inst':(['adā'], ['adbhyām'], ['adbhiḥ', 'adbhir'],),
'Dat':(['ade'], ['adbhyām'], ['adbhyaḥ', 'adbhyo', 'adbhyaś'],),
'Abl':(['adaḥ'], ['adbhyām'],['adbhyaḥ', 'adbhyo', 'adbhyaś'],),
'Gen':(['adaḥ'], ['adoḥ'], ['adām', 'adānāṃ'],),
'Loc':(['adi'], ['adoḥ'], ['atsu'],),
},
'dMF':{
'Nom': (['d'], ['dau'], ['daḥ'],),
'Voc':(['d'], ['dau'], ['daḥ'],),
'Acc':(['dam'], ['dau'], ['daḥ'],),
'Insd':(['dā'], ['dbhyām'], ['dbhiḥ', 'dbhir']),
'Dad':(['de'], ['dbhyām'], ['dbhyaḥ', 'dbhyo', 'dbhyaś'],),
'Abl':(['daḥ'], ['dbhyām'], ['dbhyaḥ', 'dbhyo', 'dbhyaś'],),
'Gen':(['daḥ'], ['doḥ'], ['dām'],),
'Loc':(['di'], ['doḥ'], ['dsu'],),
},
'dN':{
'Nom': (['d'], ['dī'], ['di'],),
'Voc':(['d'], ['dī'], ['di'],),
'Acc':(['d'], ['dī'], ['di'],),
'Insd':(['dā'], ['dbhyām'], ['dbhiḥ', 'dbhir'],),
'Dad':(['de'], ['dbhyām'], ['dbhyaḥ'],),
'Abl':(['daḥ'], ['dbhyām'], ['dbhyaḥ'],),
'Gen':(['daḥ'], ['doḥ'], ['dām'],),
'Loc':(['di'], ['doḥ'], ['dsu'],),
},
'cFM':{
'Nom': (['k'], ['cau'], ['caḥ'],),
'Voc':(['k'], ['cau'], ['caḥ'],),
'Acc':(['cam', 'cām'], ['cau'], ['acaḥ', 'co', 'cāḥ'],),
'Inst':(['cā'], ['gbhyām'], ['gbhiḥ', 'gbhir'],),
'Dat':(['ce'], ['gbhyām'], ['gbhyaḥ', 'gbhyo', 'gbhyaś'],),
'Abl':(['caḥ'], ['gbhyām'], ['gbhyaḥ', 'gbhyo', 'gbhyaś'],),
'Gen':(['caḥ'], ['coḥ'], ['cām'],),
'Loc':(['ci'], ['coḥ'], ['kṣu'],),
},
'jFM':{
'Nom': (['k'], ['jau'], ['jaḥ'],),
'Voc':(['k'], ['jau'], ['jaḥ'],),
'Acc':(['jam', 'jām'], ['jau'], ['jaḥ', 'jo'],),
'Inst':(['jā'], ['gbhyām'], ['gbhiḥ', 'gbhir'],),
'Dat':(['je'], ['gbhyām'], ['gbhyaḥ', 'gbhyo', 'gbhyaś'],),
'Abl':(['jaḥ'], ['gbhyām'], ['gbhyaḥ', 'gbhyo', 'gbhyaś'],),
'Gen':(['jaḥ'], ['joḥ'], ['jām'],),
'Loc':(['ji'], ['joḥ'], ['kṣu'],),
},
'asAllGender':{
'Nom': (['at','asas', 'aso', 'asā', 'asaṃ','as', 'o'], ['asau'], ['asaḥ', 'ās'],),
'Voc':(['at', 'asa','asaṃ', 'aṃ'], ['asau'], ['asaḥ'],),
'Acc':(['asam', 'asām'], ['asau'], ['asaḥ', 'āni', 'ānī', 'a'],),
'Inst':(['asā', 'ena'], ['adbhyām', 'ābhyāṃ'], ['adbhiḥ', 'ais'],),
'Dat':(['ase'], ['adbhyām'], ['adbhyat', 'adbhyo', 'adbhyas'],),
'Abl':(['asaḥ', 'āto', 'ato', 'atu'], ['adbhyām'], ['adbhyat', 'adbhyo', 'adbhyas'],),
'Gen':(['asaḥ', 'asya'], ['asoḥ'], ['asām', 'asānām','ānāṃ'],),
'Loc':(['asi', 'ase', 'e', 'asmi'], ['asoḥ'], ['atsu', 'eṣu'],),
},
'ṣsFM':{
'Nom': (['ḥ'], ['ṣau'], ['ṣaḥ'],),
'Voc':(['ḥ'], ['ṣau'], ['ṣaḥ'],),
'Acc':(['ṣam', 'ṣām'], ['ṣau'], ['ṣaḥ', 'ṣo'],),
'Inst':(['ṣā'], ['rbhyām'], ['rbhiḥ', 'rbhir'],),
'Dat':(['ṣe'], ['rbhyām'], ['rbhyaḥ', 'rbhyo', 'rbhyaś'],),
'Abl':(['ṣaḥ'], ['rbhyām'], ['rbhyaḥ', 'rbhyo', 'rbhyaś'],),
'Gen':(['ṣaḥ'], ['ṣoḥ'], ['ṣām'],),
'Loc':(['ṣi'], ['ṣoḥ'], ['ḥṣu'],),
},
'śFM':{
'Nom': (['ṭ'], ['śau'], ['ṣaṭ'],),
'Voc':(['ṭ'], ['ṣau'], ['ṣaṭ'],),
'Acc':(['ṣam', 'ṣām'], ['ṣau'], ['ṣaṭ', 'ṣo'],),
'Inst':(['ṣā'], ['ḍbhyām'], ['ḍbhiṭ', 'ḍbhiḍ'],),
'Dat':(['ṣe'], ['ḍbhyām'], ['ḍbhyaṭ', 'ḍbhyo', 'ḍbhyaś'],),
'Abl':(['ṣaṭ'], ['ḍbhyām'], ['ḍbhyaṭ', 'ḍbhyo', 'ḍbhyaś'],),
'Gen':(['ṣaṭ'], ['ṣoṭ'], ['ṣām'],),
'Loc':(['ṣi'], ['ṣoṭ'], ['ṭṣu'],),
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
'Nom': (['dik'], ['diśau'], ['diśaḥ'],),
'Voc':(['dik'], ['diśau'], ['diśaḥ'],),
'Acc':(['diśam'], ['diśau'], ['diśaḥ'],),
'Inst':(['diśā'], ['digbhyām'], ['digbhiḥ'],),
'Dat':(['diśe'], ['digbhyām'], ['digbhyaḥ'],),
'Abl':(['diśaḥ'], ['digbhyām'], ['digbhyaḥ'],),
'Gen':(['diśaḥ'], ['diśoḥ'], ['diśām'],),
'Loc':(['diśi'], ['diśoḥ'], ['dikṣu'],),
},
'ṃsM':{
'Nom': (['mān'], ['māṃsau'], ['māṃsaḥ','māṃṣaḥ'],),
'Voc':(['man'], ['māṃsau'], ['māṃsaḥ','māṃṣaḥ'],),
'Acc':(['māṃsam','mṣam'], ['māṃsau'],['ṃsaḥ','mṣaḥ'],),
'Inst':(['ṃsā','mṣā'], ['ṃbhyām','mbhyām'], ['ṃbhiḥ','mbhiḥ'],),
'Dat':(['ṃse','mṣe'], ['ṃbhyām', 'ṃbhyām'], ['ṃbhyaḥ','mbhyām'],),
'Abl':(['ṃsaḥ','mṣaḥ'], ['ṃbhyām','mbhyām'], ['ṃbhyaḥ','mbhyaḥ'],),
'Gen':(['ṃsaḥ','mṣaḥ'], ['ṃsoḥ','ṃṣoḥ'], ['ṃsām', 'ṃṣāṃ'],),
'Loc':(['ṃsi', 'ṃṣi'], ['ṃsoḥ','ṃṣoḥ'], ['ṃsu','mṣu'],),
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


AdjExtra=combine_inftypes(noun['AN'],noun['AM'])
adj=copy.copy(noun)
adj[('AAllGender')]=AdjExtra

##============ Verb ========================

# rules to generate conjugated forms from the third person singular verb stem
# example: 
# in the StarDict wordlist we find the form akṣati , remove ti and attach all suffixes

# !!forms in 'te', e.g. ucyate are 'passive', attach ONLY the MiddlePassive suffixes below

# please add to the wordlist the following forms: 'avocat', 'avocanti', 'āha', āhuḥ. they are frequently occurring 'aorists', no need to conjugate 'them', other persons do not occur.
# the paradigms listed here do **not** include aorist, perfect, future, gerund, gerundive and participles
# gerund, gerundive and participles are listed in dictionary_IAST.others.txt but *not* connected with their corresponding verb lemma
# aorist, perfect and future are irregular and cannot easily be geenrated from rules. Arthaśāstra should not contain many of them, so for the time being this impoverished paradigm should work


# For all verb paradigms we need to allow for the following spelling variants in the suffixes:
# n> ṅ
# s > ṣ
# ṭ > t
# hi > dhi
# dh > ddh AND ḍh AND ḍḍh

# addhiVerb: the nasal in the stem (before the suffixes) changes between 'ṇ' and 'n'. please generate both forms

# aktiVerb the nasal in the stem (before the suffixes) changes between 'n' 'ñ' and 'ṅ' please geenrate all three forms


# For tiVerb the last vowel of the verb stem _before_ the suffix is subject to the following changes:
# e > i AND ī and vice versa
# ay > ī AND i and vice versa
# ai > ī AND i and vice versa
# āy > ī AND i and vice versa
# ā > a and vice versa
# o > u and vice versa
# au > o AND u and vice versa
# av > ū and vice versa
#please generate parallel forms that incorporate the changes above, they should not add much ambiguity.

# tiVerb verbs are very irregular. A few add a 'i' before some suffixes, some drop the last consonant of the stem before some suffixes.
#Shall we try to generate forms that insert an i before stem and suffix and see what happens. This may generate ambiguous forms, I am not sure.
#As for the dropped consonant, I suspect generating forms without it could create a lot of ambiguity, so let's try not accounting for it and see how many forms it misses



VerbInfTypes=OrderedDict({
    ('ati',):'atiVerb',
    ('āti',):'ātiVerb',
    ('karoti',):'karotiVerb',
    ('oti',):'otiVerb',
    ('addhi',):'addhiVerb',
    ('akti',):'aktiVerb',
    ('ti',):'tiVerb'

})

verb={
'atiVerb':{
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
},
'ātiVerb':{
'PresentActive':{
('1','sg',):[ 'āmi'],
('2','sg',):[ 'āsi'],
('3','sg',):['āti'],
('1','dl',):['āvaḥ'],
('2','dl',):['āthaḥ'],
('3','dl',):['ātaḥ'],
('1','pl',):['āmaḥ'],
('2','pl',):['ātha'],
('3','pl',):['ānti'],
},
'PresentMiddlePassive':{
('1','sg',):[ 'e'],
('2','sg',):['āse', 'se'],
('3','sg',):['āte', 'te'],
('1','dl',):['āvahe'],
('2','dl',):['ethe'],
('3','dl',):['āte'],
('1','pl',):['āmahe'],
('2','pl',):['ādhve'],
('3','pl',):['ānte'],
},
'ImpfActive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['ām'],
('2','sg',):['āḥ'],
('3','sg',):['āt'],
('1','dl',):['āva'],
('2','dl',):['ātam'],
('3','dl',):['ātām'],
('1','pl',):['āma'],
('2','pl',):['āta'],
('3','pl',):['ān'],
},
'ImpfMiddlePassive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['e', 'i'],
('2','sg',):['āthāḥ', 'thāḥ'],
('3','sg',):['āta', 'ta'],
('1','dl',):['āvahi'],
('2','dl',):['ethām'],
('3','dl',):['etām'],
('1','pl',):['āmahi'],
('2','pl',):['ādhvam'],
('3','pl',):['nta'],
},
'OptativeActive':{
('1','sg',):['eyam', 'yām'],
('2','sg',):['eḥ', 'yāḥ'],
('3','sg',):['et', 'yāt'],
('1','dl',):['eva'],
('2','dl',):['etam'],
('3','dl',):['etām'],
('1','pl',):['ema'],
('2','pl',):['eta'],
('3','pl',):['yuḥ'],
},
'OptativeMiddlePassive':{
('1','sg',):['eya', 'yā'],
('2','sg',):['ethāḥ', 'thāḥ'],
('3','sg',):['eta', 'ta'],
('1','dl',):['evahi'],
('2','dl',):['eyāthām'],
('3','dl',):['eyātam'],
('1','pl',):['emahi'],
('2','pl',):['edhvam'],
('3','pl',):['eran'],
},
'ImperativeActiv':{

('1','sg',):['āni'],
('2','sg',):['ā', 'hi'],
('3','sg',):['ātu'],
('1','dl',):['āva'],
('2','dl',):['ātam'],
('3','dl',):['ātām'],
('1','pl',):['āma'],
('2','pl',):['āta'],
('3','pl',):['āntu'],
},
'ImperativeMiddlepassiv':{

('1','sg',):[ 'āi'],
('2','sg',):[ 'āsva', 'sva'],
('3','sg',):['ātām', 'tām'],
('1','dl',):['āvahai'],
('2','dl',):['ethām'],
('3','dl',):['etām'],
('1','pl',):[ 'āmahai'],
('2','pl',):['ādhvam'],
('3','pl',):['āntām'],
}
},
'karotiVerb':{
'karPresentActive':{
('1','sg'):['karomi'],
('2','sg'):['karoṣi'],
('3','sg'):['karoti'],
('1','dl'):['kurvaḥ'],
('2','dl'):['kuruthaḥ'],
('3','dl'):['kurutaḥ'],
('1','pl'):['kurumaḥ'],
('2','pl'):['kurutha'],
('3','pl'):['karvanti'],
},
'PresentMiddlePassive':{
('1','sg'):['kurve'],
('2','sg'):['kuruṣe'],
('3','sg'):['kurute'],
('1','dl'):['kurvahe'],
('2','dl'):['karvāthe'],
('3','dl'):['karvāte'],
('1','pl'):['kurmahe'],
('2','pl'):['kurdhve'],
('3','pl'):['karvate'],
},
'ImpfActive':{  # for the imperfect put an 'karā' before the stem:['kare'.g. 'karbhavati'> 'karābhavan', when stem starts in 'karvowl', sandhi applies:[  'karākṣati' > ākṣan
('1','sg'):['akaravam'],
('2','sg'):['akaroḥ'],
('3','sg'):['akarot'],
('1','dl'):['akurva'],
('2','dl'):['akurutam'],
('3','dl'):['akurutām'],
('1','pl'):['akuruma'],
('2','pl'):['akuruta'],
('3','pl'):['akarvan'],
},
'ImpfMiddlePassive':{  # for the imperfect put an 'karā' before the stem:['kare'.g. 'karbhavati'> 'karābhavan', when stem starts in 'karvowl', sandhi applies:[  'karākṣati' > ākṣan
('1','sg'):['akurvi'],
('2','sg'):['akuruthāḥ'],
('3','sg'):['akuruta'],
('1','dl'):['akurvahi'],
('2','dl'):['akurvāthām'],
('3','dl'):['akurvātām'],
('1','pl'):['akurmahi'],
('2','pl'):['akurdhvam'],
('3','pl'):['akurvata'],
},
'OptativeActive':{
('1','sg'):['kuryām'],
('2','sg'):['kuryāḥ'],
('3','sg'):['kuryāt'],
('1','dl'):['kuryāva'],
('2','dl'):['kuryātam'],
('3','dl'):['kuryātām'],
('1','pl'):['kuryāma'],
('2','pl'):['kuryāta'],
('3','pl'):['kuryuḥ'],
},
'OptativeMiddlePassive':{
('1','sg'):['kurvīya'],
('2','sg'):['kurvīthāḥ'],
('3','sg'):['kurvīta'],
('1','dl'):['kurvīvahi'],
('2','dl'):['kurvīyāthām'],
('3','dl'):['kurvīyātam'],
('1','pl'):['kurvīmahi'],
('2','pl'):['kurvīdhvam'],
('3','pl'):['kurvīran'],
},
'ImperativeActiv':{

('1','sg'):['karavāṇi'],
('2','sg'):['kuru'],
('3','sg'):['karotu'],
('1','dl'):['karavāva'],
('2','dl'):['kurutam'],
('3','dl'):['kurutām'],
('1','pl'):['karavāma'],
('2','pl'):['kuruta'],
('3','pl'):['kurvantu'],
},
'ImperativeMiddlepassiv':{

('1','sg'):['karavai'],
('2','sg'):['kuruṣva'],
('3','sg'):['kurutām'],
('1','dl'):['kuravāvahai'],
('2','dl'):['kuruvāthām'],
('3','dl'):['kuravātām'],
('1','pl'):['kuravāmahai'],
('2','pl'):['kurudhvam'],
('3','pl'):['kurvatām'],
}
},

'otiVerb':{
'PresentActive':{
('1','sg',):['omi'],
('2','sg',):['osi'],
('3','sg',):['oti'],
('1','dl',):['uvaḥ'],
('2','dl',):['uthaḥ'],
('3','dl',):['utaḥ'],
('1','pl',):['umaḥ'],
('2','pl',):['utha'],
('3','pl',):['ati', 'vanti'],
},
'PresentMiddlePassive':{
('1','sg',):['ve'],
('2','sg',):['uṣe'],
('3','sg',):['ute'],
('1','dl',):['uvahe'],
('2','dl',):['vāthe'],
('3','dl',):['vāte'],
('1','pl',):['umahe'],
('2','pl',):['udhve'],
('3','pl',):['vate'],
},
'ImpfActive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['avam'],
('2','sg',):['oḥ'],
('3','sg',):['ot'],
('1','dl',):['uva'],
('2','dl',):['utam'],
('3','dl',):['utām'],
('1','pl',):['uma'],
('2','pl',):['uta'],
('3','pl',):['avuḥ', 'van'],
},
'ImpfMiddlePassive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['vi'],
('2','sg',):['uthāḥ'],
('3','sg',):['uta'],
('1','dl',):['uvahi'],
('2','dl',):['uvāthām'],
('3','dl',):['uvātām'],
('1','pl',):['umahi'],
('2','pl',):['udhvam'],
('3','pl',):['uvata', 'vata'],
},
'OptativeActive':{
('1','sg',):['uyām'],
('2','sg',):['uyāḥ'],
('3','sg',):['uyāt'],
('1','dl',):['uyāva'],
('2','dl',):['uyātam'],
('3','dl',):['uyātām'],
('1','pl',):['uyāma'],
('2','pl',):['uyāta'],
('3','pl',):['uyuḥ'],
},
'OptativeMiddlePassive':{
('1','sg',):['vīya'],
('2','sg',):['vīthāḥ'],
('3','sg',):['vīta'],
('1','dl',):['vīvahi'],
('2','dl',):['vīyāthām'],
('3','dl',):['vīyātam'],
('1','pl',):['vīmahi'],
('2','pl',):['vīdhvam'],
('3','pl',):['vīran'],
},
'ImperativeActiv':{

('1','sg',):['vāni'],
('2','sg',):['udhi', 'u'],
('3','sg',):['otu'],
('1','dl',):['avāva'],
('2','dl',):['utam'],
('3','dl',):['utām'],
('1','pl',):['avāma'],
('2','pl',):['uta'],
('3','pl',):['vatu', 'vantu'],
},
'ImperativeMiddlepassiv':{

('1','sg',):['avai'],
('2','sg',):['uṣva'],
('3','sg',):['utām'],
('1','dl',):['avāvahai'],
('2','dl',):['vāthām'],
('3','dl',):['vātām'],
('1','pl',):['avāmahai'],
('2','pl',):['udhvam'],
('3','pl',):['vatām'],
}
},
'addhiVerb':{
'PresentActive':{
('1','sg',):['adhmi'],
('2','sg',):['atsi'],
('3','sg',):['addhi'],
('1','dl',):[''],
('2','dl',):[''],
('3','dl',):[''],
('1','pl',):['dhmaḥ'],
('2','pl',):['ddha'],
('3','pl',):['dhanti'],
},
'PresentMiddlePassive':{
('1','sg',):['dhe'],
('2','sg',):['tse'],
('3','sg',):['ddhe'],
('1','dl',):[''],
('2','dl',):[''],
('3','dl',):[''],
('1','pl',):['dhmahe'],
('2','pl',):['ddhve'],
('3','pl',):['dhate'],
},
'ImpfActive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['adham'],
('2','sg',):['at'],
('3','sg',):['at'],
('1','dl',):['ava'],
('2','dl',):['atam'],
('3','dl',):['atām'],
('1','pl',):['dhma'],
('2','pl',):['ddha'],
('3','pl',):['dhan'],
},
'ImpfMiddlePassive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['dhi'],
('2','sg',):['ddhāḥ'],
('3','sg',):['ddha'],
('1','dl',):['dhvahi'],
('2','dl',):['dhāthām'],
('3','dl',):['dhātām'],
('1','pl',):['dhmahi'],
('2','pl',):['ddhvam'],
('3','pl',):['dhata'],
},
'OptativeActive':{
('1','sg',):['dhyām'],
('2','sg',):['dhāḥ'],
('3','sg',):['dhāt'],
('1','dl',):['dhāva'],
('2','dl',):['dhātam'],
('3','dl',):['dhātām'],
('1','pl',):['dhāma'],
('2','pl',):['dhāta'],
('3','pl',):['dhyuḥ'],
},
'OptativeMiddlePassive':{
('1','sg',):['dhīya'],
('2','sg',):['dhīthāḥ'],
('3','sg',):['dhīta'],
('1','dl',):['dhīvahi'],
('2','dl',):['dhīyāthām'],
('3','dl',):['dhīyātam'],
('1','pl',):['dhīmahi'],
('2','pl',):['dhīdhvam'],
('3','pl',):['dhīran'],
},
'ImperativeActiv':{

('1','sg',):['dhāni'],
('2','sg',):['ddhi'],
('3','sg',):['ddhu'],
('1','dl',):['dhāva'],
('2','dl',):['ddham'],
('3','dl',):['ddhām'],
('1','pl',):['dhāma'],
('2','pl',):['ddha'],
('3','pl',):['dhantu'],
},
'ImperativeMiddlepassiv':{

('1','sg',):['dhai'],
('2','sg',):['tsva'],
('3','sg',):['ddhām'],
('1','dl',):['dhāvahai'],
('2','dl',):['dhāthām'],
('3','dl',):['dhātām'],
('1','pl',):['dhāmahai'],
('2','pl',):['ddhvam'],
('3','pl',):['dhatām'],
}
},
'aktiVerb':{
'PresentActive':{
('1','sg',):['ajmi'],
('2','sg',):['akṣi'],
('3','sg',):['akti'],
('1','dl',):[''],
('2','dl',):[''],
('3','dl',):[''],
('1','pl',):['jmaḥ'],
('2','pl',):['ktha'],
('3','pl',):['janti'],
},
'PresentMiddlePassive':{
('1','sg',):['je'],
('2','sg',):['kṣe'],
('3','sg',):['kte'],
('1','dl',):[''],
('2','dl',):[''],
('3','dl',):[''],
('1','pl',):['jmahe'],
('2','pl',):['gdhve'],
('3','pl',):['jate'],
},
'ImpfActive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['ajam'],
('2','sg',):['ak'],
('3','sg',):['ak'],
('1','dl',):[''],
('2','dl',):[''],
('3','dl',):[''],
('1','pl',):['jma'],
('2','pl',):['kta'],
('3','pl',):['jan'],
},
'ImpfMiddlePassive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['ji'],
('2','sg',):['kthāḥ'],
('3','sg',):['kta'],
('1','dl',):[''],
('2','dl',):[''],
('3','dl',):[''],
('1','pl',):['jmahi'],
('2','pl',):['gdhvam'],
('3','pl',):['jata'],
},
'OptativeActive':{
('1','sg',):['jyām'],
('2','sg',):['jāḥ'],
('3','sg',):['jāt'],
('1','dl',):['jāva'],
('2','dl',):['jātam'],
('3','dl',):['jātām'],
('1','pl',):['jāma'],
('2','pl',):['jāta'],
('3','pl',):['jyuḥ'],
},
'OptativeMiddlePassive':{
('1','sg',):['jīya'],
('2','sg',):['jīthāḥ'],
('3','sg',):['jīta'],
('1','dl',):['jīvahi'],
('2','dl',):['jīyāthām'],
('3','dl',):['jīyātam'],
('1','pl',):['jīmahi'],
('2','pl',):['jīdhvam'],
('3','pl',):['jīran'],
},
'ImperativeActiv':{

('1','sg',):['nāni'],
('2','sg',):['gdhi'],
('3','sg',):['ktu'],
('1','dl',):['jāva'],
('2','dl',):['ktam'],
('3','dl',):['ktām'],
('1','pl',):['jāma'],
('2','pl',):['kta'],
('3','pl',):['jantu'],
},
'ImperativeMiddlepassiv':{

('1','sg',):['jai'],
('2','sg',):['kṣva'],
('3','sg',):['ktām'],
('1','dl',):['jāvahai'],
('2','dl',):['jāthām'],
('3','dl',):['jātām'],
('1','pl',):['jāmahai'],
('2','pl',):['gdhvam'],
('3','pl',):['jatām'],
}
},
'tiVerb':{
'PresentActive':{
('1','sg',):['mi'],
('2','sg',):['si'],
('3','sg',):['ti'],
('1','dl',):['vaḥ'],
('2','dl',):['thaḥ'],
('3','dl',):['taḥ'],
('1','pl',):['maḥ'],
('2','pl',):['tha'],
('3','pl',):['nti'],
},
'PresentMiddlePassive':{
('1','sg',):['e'],
('2','sg',):['se'],
('3','sg',):['te'],
('1','dl',):['vahe'],
('2','dl',):['āthe'],
('3','dl',):['āte'],
('1','pl',):['mahe'],
('2','pl',):['dhve'],
('3','pl',):['ate'],
},
'ImpfActive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['am'],
('2','sg',):['ḥ', 'īḥ', 't'],
('3','sg',):['t', 'īt'],
('1','dl',):['va'],
('2','dl',):['tam'],
('3','dl',):['tām'],
('1','pl',):['ma'],
('2','pl',):['ta'],
('3','pl',):['an'],
},
'ImpfMiddlePassive':{  # for the imperfect put an 'ā' before the stem:['e'.g. 'bhavati'> 'ābhavan', when stem starts in 'vowl', sandhi applies:[  'ākṣati' > ākṣan
('1','sg',):['i'],
('2','sg',):['thāḥ'],
('3','sg',):['ta'],
('1','dl',):['vahi'],
('2','dl',):['āthām', 'thām'],
('3','dl',):['ātām', 'tām'],
('1','pl',):['mahi'],
('2','pl',):['dhvam'],
('3','pl',):['ata'],
},
'OptativeActive':{
('1','sg',):['yām'],
('2','sg',):['āḥ'],
('3','sg',):['āt'],
('1','dl',):['āva'],
('2','dl',):['ātam'],
('3','dl',):['ātām'],
('1','pl',):['āma'],
('2','pl',):['āta'],
('3','pl',):['yuḥ'],
},
'OptativeMiddlePassive':{
('1','sg',):['īya'],
('2','sg',):['īthāḥ'],
('3','sg',):['īta'],
('1','dl',):['īvahi'],
('2','dl',):['īyāthām'],
('3','dl',):['īyātam'],
('1','pl',):['īmahi'],
('2','pl',):['īdhvam'],
('3','pl',):['īran'],
},
'ImperativeActiv':{

('1','sg',):['āni'],
('2','sg',):['hi'],
('3','sg',):['tu'],
('1','dl',):['āva'],
('2','dl',):['tam'],
('3','dl',):['tām'],
('1','pl',):['āma'],
('2','pl',):['ta'],
('3','pl',):['antu'],
},
'ImperativeMiddlepassiv':{

('1','sg',):['ai'],
('2','sg',):['sva'],
('3','sg',):['tām'],
('1','dl',):['āvahai'],
('2','dl',):['āthām'],
('3','dl',):['ātām'],
('1','pl',):['āmahai'],
('2','pl',):['dhvam'],
('3','pl',):['atām'],
}
}

}


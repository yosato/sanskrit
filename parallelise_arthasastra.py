import re,sys

Out=sys.stdout

Org='/rawData/sanskrit/Arthasastra_original.txt'
Seg='/rawData/sanskrit/ArthasastraSandhi.txt'

FSrO=open(Org)
FSrS=open(Seg)
while FSrO and FSrS:
    MatchO=None;MatchS=None
    while FSrO and not MatchO:
        Line=FSrO.readline().strip()
        if not Line:
            continue
        MatchO=re.match(r'^([0-9]{2}\.[1-9]\.[0-9]{2}[a-z]?) +(.+)[ -,/]*',Line)
    while FSrS and not MatchS:
        Line=FSrS.readline().strip()
#        if not Line:
#           continue
#        print(Line)
        MatchS=re.match(r'^KAZ([0-9]{2}\.[1-9]\.[0-9]{2}[a-z]?)[/ ]+(.+)[ -,/]*',FSrS.readline().strip())
    SerNumO,LineO=MatchO.groups()[:2]
    SerNumS,LineS=MatchS.groups()[:2]
    
    while (FSrO and FSrS) and SerNumO!=SerNumS:
        LstNumO=re.sub(r'[a-z]$','',SerNumO.split('.')[-1])
        LstNumS=re.sub(r'[a-z]$','',SerNumS.split('.')[-1])
        if LstNumO.isnumeric() and LstNumS.isnumeric():
            GoNextStr=FSrO if int(LstNumO)<int(LstNumS) else FSrS
        else:
            GoNextStr=FSrO if not LstNumO.isnumeric() else FSrS
        GoNextStr.readline()
    
    Out.write(SerNumO+': '+LineO+'\t'+LineS)
            
        

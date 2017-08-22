import re,sys
import collections

Out=sys.stdout

Org='/rawData/sanskrit/Arthasastra_original.txt'
Seg='/rawData/sanskrit/ArthasastraSandhi.txt'

def get_indsent_pairs(File):
    Dict=collections.OrderedDict()
    for LiNe in open(File):
        Match=re.match(r'^(?:...)?([0-9]{2}\.[1-9]\.[0-9]{2}[a-z]?)\/? +(.+?)[ -,/]*$',LiNe.strip())
        if Match:
            Dict[Match.groups()[0]]=Match.groups()[1]
    return Dict 

Dicts=[]
for File in (Org,Seg):
    Dicts.append(get_indsent_pairs(File))

for Ind,SentO in Dicts[0].items():
    if Ind in Dicts[1].keys():
        Out.write(Ind+'\t'+SentO+'\t'+Dicts[1][Ind]+'\n')

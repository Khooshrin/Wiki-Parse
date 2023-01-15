import requests
import pandas as pd
import json

S = requests.Session()
finaljsonlist=[]

URL = "https://en.wikipedia.org/w/api.php"

df = pd.read_csv('TeKnowbaseEntities.tsv', sep='\t')
# print(df)

i = 0

for entity in df['entity_URI']:

    res = str(entity).split('/')
    #print(res)
    print(i)
    i += 1
    entity=res[len(res)-1]
    entity=entity.replace("_"," ")
    print(entity)

    PARAMS = {
        "action": "parse",
        "page": entity,
        "format": "json"
    }

    R = S.get(url=URL, params=PARAMS)

    if R.status_code<29 or R.status_code>200:
        continue

    DATA = R.json()
    
    if "parse" in DATA:
        jsondict={}
        jsondict[entity]=DATA["parse"]["text"]["*"]
        finaljsonlist.append(jsondict)


with open("sample.json", "w") as outfile:
    json.dump(finaljsonlist,outfile)

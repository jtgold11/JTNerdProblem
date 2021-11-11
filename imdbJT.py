import requests
import json

# responseF = requests.get("https://imdb-api.com/en/API/FullCast/k_ej78sz8s/tt0108778")
# with open('friends.json','w') as fre:
#     json.dump(responseF.json(), fre,ensure_ascii=False, indent=4)
#
# responseS = requests.get("https://imdb-api.com/en/API/FullCast/k_ej78sz8s/tt0098904")
# with open('seinfield.json','w') as sein:
#     json.dump(responseS.json(), sein,ensure_ascii=False, indent=4)

listF = []
listS = []
with open('friends.json', 'r') as fre:
    data = json.loads(fre.read())
    for key in data['actors']:
        listF.append(key['name'])
with open('seinfield.json', 'r') as sei:
    data1 = json.loads(sei.read())
    for key1 in data1['actors']:
        listS.append(key1['name'])
with open('actors.txt', 'w') as f:
    for name in listS:
        if name in listF:
            f.write(name)
            f.write("\n")
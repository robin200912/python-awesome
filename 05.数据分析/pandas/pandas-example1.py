import pandas as pd
import json

json_str = '''[
    {"id": 2018,
    "manu": "KFC",
    "group": "fast foods",
    "description": "ddd...",
    "nut": [{
        "value": 20.8,
        "units": "g",
        "description": "",
        "group": "Compt"
    },
    {
        "value": 30.8,
        "units": "kg",
        "description": "ddd",
        "group": "Compt222"
    }
    ]},
    {"id": 2019,
    "manu": "KFC2",
    "group": "fast foods2",
    "description": "ddd2...",
    "nut": [{
        "value": 30.8,
        "units": "kg",
        "description": "ddd",
        "group": "Compt2"
    }]}
    ]
'''

data_dic = json.loads(json_str)
print data_dic

a = pd.DataFrame(data_dic[0]['nut'])
print a

nutes = []
for rec in data_dic:
    fruits = pd.DataFrame(rec['nut'])
    fruits['id'] = rec['id']
    nutes.append(fruits)

nutes = pd.concat(nutes)
print nutes

nutes = nutes.drop_duplicates()

info = pd.DataFrame(data_dic, columns=['description', 'group', 'id', 'manu'])
print info

info = info.rename(columns={ 'description': 'food', 'group': 'fgroup' }, copy=False)
nutes = nutes.rename(columns={ 'description': 'nutes', 'group': 'ngroup' }, copy=False)

ndata = pd.merge(info, nutes, on='id', how='outer')
print ndata
print

print ndata.ix[2]
print

result = ndata.groupby(['nutes', 'fgroup'])['value'].quantile(0.5)
print result
print type(result)
result['Zinc, Zn'].order().plot(kind='barh')
# result.order().plot(kind='barh')
# by_nutrient = ndata.groupby(['ngroup', 'nutes']) 

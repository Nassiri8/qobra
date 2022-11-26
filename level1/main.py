import json

table = []
result = []

def comission_ten(wallet):
    return (wallet*10)/100

def comission_twenty(wallet):
    return (wallet*20)/100

def print_result(result):
    return json.dumps({"commissions":result})

with open("./input.json", "r") as write_file:
    obj = json.load(write_file)

#create one list of dict to manipulate
for u in obj['users']:
    dicts = {}
    dicts['user_id'] = u['id']
    dicts['amount'] = 0
    dicts['deals'] = 0
    for d in obj['deals']:
        if u['id'] == d['user']:
            dicts['amount'] += d['amount']
            dicts['deals'] += 1
    table.append(dicts)

#create final object with calcul            
for value in table:
    dicts = {}
    dicts['user_id'] = value['user_id']
    dicts['comission'] = 0
    if value['deals'] <= 2 and  value['deals'] > 0:
        dicts['comission'] = comission_ten(value['amount'])
    if value['deals'] >= 3:
        dicts['comission'] = comission_twenty(value['amount'])
    if value['amount'] >=2000:
        dicts['comission'] += 500
    result.append(dicts)

print(print_result(result))
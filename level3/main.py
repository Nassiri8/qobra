import json

table = []
amount = []
result = []

def comission_five(objectif):
    return ((objectif/2)*5)/100

def comission_ten(objectif):
    return ((objectif/2)*10)/100

def comission_twenty(objectif, amount):
    value = amount - objectif
    return ((value/2)*15)/100

def print_result(result):
    return json.dumps({"commissions":result})

with open("./input.json", "r") as write_file:
    obj = json.load(write_file)


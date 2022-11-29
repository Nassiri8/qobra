'use strict';

const fs = require('fs');

let rawdata = fs.readFileSync('input.json');
let json = JSON.parse(rawdata);

let result = []; 
let table = [];

function fivePercent(objectif){
    return ((objectif/2)*5)/100;
}

function tenPercent(objectif){
    return ((objectif/2)*10)/100;
}

function fifteenPercent(amount, objectif){
    let value = amount - objectif;
    return ((value/2)*15)/100;
}

//Create one Object
for(let i=0; i<json['users'].length; i++){
    let dicts = {"user_id":json['users'][i]['id'],"amount":0,"objective":json['users'][i]['objective']};
    for(let j=0; j<json['deals'].length;j++){
        if(json['users'][i]['id'] == json['deals'][j]['user']){
            dicts['amount'] += json['deals'][j]['amount'];
        }
    }
    table.push(dicts);
}

//Manipulate and calculate comission
for(let i= 0; i<table.length; i++){
    let dicts = {'user_id': table[i]['user_id'], 'commission': fivePercent(table[i]['objective']) + tenPercent(table[i]['objective'])};
    if(table[i]['amount'] > table[i]['objective']){
        dicts['commission'] += fifteenPercent(table[i]['amount'], table[i]['objective']);
    }
    result.push(dicts)
}

console.log(JSON.stringify({commissions: result}));
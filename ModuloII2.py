def validarEntero(num):
    isValid = False
    try:
        int(num)
        isValid = True
    except ValueError:
        isValid = False
    return isValid

def pedirNumeroEnteroValidado(messages = "Ingrese un numero Enter0"):
    num = input(messages)
    while not validarEntero(num):
        print("Error valor ingresado incompatible")
        num = input(messages)
    return int(num)  

import requests
import json

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

querystring = {"country":""}

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "90c2b8b002mshc23f61200f8d6d6p1765bdjsn9c69c1b3ac52"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


dicc = response.json()

def ImpresiondeTop (Lista,Diccionario):
    n= 1
    while n < 11:
        print(str(n) + ".   " + Lista[n-1]+ " : " + str(Diccionario[Lista[n-1]]))
        n += 1
    return



                
diccinfectados = {}
for x in dicc ['data']['covid19Stats']:
    if x ['country'] in diccinfectados:
        diccinfectados[x ['country']] = diccinfectados[x ['country']] + x['confirmed']
    else: 
        diccinfectados[x ['country']] =  x['confirmed']

dicciMuertos = {}
for x in dicc ['data']['covid19Stats']:
    if x ['country'] in dicciMuertos:
        dicciMuertos[x ['country']] = dicciMuertos[x ['country']] + x['deaths']
    else: 
        dicciMuertos[x ['country']] =  x['deaths']

diccsalvados = {}
for x in dicc ['data']['covid19Stats']:
    if x ['country'] in diccsalvados:
        diccsalvados[x ['country']] = diccsalvados[x ['country']] + x['recovered']
    else: 
        diccsalvados[x ['country']] =  x['recovered']



top_infectados = []
for x in diccinfectados:
    beta = False
    if len(top_infectados)== 0:
        top_infectados.append(x)
    elif len(top_infectados)!= 0:
        for y in top_infectados:
            if diccinfectados[y] <= diccinfectados[x]:
                top_infectados.insert((top_infectados.index(y)),x)
                beta = True
                break
    if beta == False:
        top_infectados.append(x)
top_infectados.pop(0)
    
top_Muetos = []              
for x in dicciMuertos:
    beta = False
    if len(top_Muetos)== 0:
        top_Muetos.append(x)
    elif len(top_Muetos)!= 0:
        for y in top_Muetos:
            if dicciMuertos[y] <= dicciMuertos[x]:
                top_Muetos.insert((top_Muetos.index(y)),x)
                beta = True
                break
    if beta == False:
        top_Muetos.append(x)
top_Muetos.pop(0)          


top_salvados = []
for x in diccsalvados:
    beta = False
    if len(top_salvados)== 0:
        top_salvados.append(x)
    elif len(top_salvados)!= 0:
        for y in top_salvados:
            if diccsalvados[y] <= diccsalvados[x]:
                top_salvados.insert((top_salvados.index(y)),x)
                beta = True
                break
    if beta == False:
        top_salvados.append(x)
top_salvados.pop(0) 




ImpresiondeTop(top_infectados,diccinfectados)

ImpresiondeTop(top_Muetos,dicciMuertos)

ImpresiondeTop(top_salvados,diccsalvados)
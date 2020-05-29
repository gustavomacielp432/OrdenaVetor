from operator import attrgetter
from Item import Item
import pandas as pd
import csv

def partition(array, start, end, compare_func):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and compare_func(array[high], pivot):
            high = high - 1

        while low <= high and not compare_func(array[low], pivot):
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end, compare_func):
    if start >= end:
        return
    
    p = partition(array, start, end, compare_func)
    quick_sort(array, start, p - 1, compare_func)
    quick_sort(array, p + 1, end, compare_func)


dados = pd.read_csv("SitesDesordenados_20200519003057.csv", sep=';', names=["site", "classificacao"])
tipos_classificacao = dados.sort_values('classificacao').drop_duplicates('classificacao', keep="first")['classificacao'].tolist()
itens = []

for (i, row) in dados.iterrows():
    itens.append(Item(row['site'], row['classificacao']))

compare_func =  ( lambda x, y:  x.classificacao > y.classificacao ) 
quick_sort(itens, 0, len(itens) - 1, compare_func )


lista_ordenada = []
for tipo in tipos_classificacao:
    lista = (list(filter(lambda x: x.classificacao == tipo, itens)))
    compare_func =  ( lambda x, y:  x.site.lower() > y.site.lower()) 
    quick_sort(lista, 0, len(lista) - 1, compare_func )
    lista_ordenada = lista_ordenada + lista

with open('./SitesOrdenados.csv', 'w', newline='') as csvfile:
    fieldnames = ['site', 'classificacao']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in lista_ordenada:
        writer.writerow({'site': item.site, 'classificacao': item.classificacao})
    
    

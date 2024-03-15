import csv

with open('scientist.csv','r',encoding='UTF-8') as f:
    list = csv.reader(f)
    with open('scientist.csv','w',encoding='UTF-8') as g:
        new_list = csv.writer(g)

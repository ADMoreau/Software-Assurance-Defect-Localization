import csv
from difflib import SequenceMatcher

file = open('50percent.csv','r')
data = csv.reader((line.replace('\0','') for line in file), delimiter = '\n')    
into = list(data)
x = len(into)
for i in into:
    temp = 0
    print(temp)
    print(x)
    for j in into:
        s = SequenceMatcher(None, i, j).ratio()
        #print(j)        
        if s < .5 and s != 1:
            #print(s)
            into.pop(temp)
        temp += 1
    x = len(into)
    temp = 0
x = len(into)
print(into)
out = open('50filteredGOOD.csv','w')
for i in range(x):
    out.write(into[i][0])
    out.write('\n')
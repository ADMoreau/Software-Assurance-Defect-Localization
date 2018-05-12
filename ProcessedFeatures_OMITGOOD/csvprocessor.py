import csv
from difflib import SequenceMatcher
'''
This program works exactly like the program used in the OMITBAD file, it was just left here for simplicity.
For documentation see that python code.
'''
file = open('90percent_GOOD.csv','r')
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
        if s < .5 or s == 1:
            #print(s)
            into.pop(temp)
        temp += 1
    x = len(into)
    temp = 0
x = len(into)
print(into)
out = open('90filteredGOOD.csv','w')
for i in range(x):
    out.write(into[i][0])
    out.write('\n')

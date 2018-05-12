import csv
from difflib import SequenceMatcher
'''
This code is used to read the csv of found features from the first step of sequencing where a single sample string returned from the mVista program
was compared to every other sample returned by mVista to determine all of the strings that matched above a certain threshhold 
After that rough set of features are found the csv of rough features are passed to this program where every sample from the rough set is compared
to every other sample to find a set that is self similar above a designated theshold, in this case that is 50% similarity but this can be changed 
by altering a few lines of the code.
'''
#Open and read the csv, the 50percent indicates that this is the csv containing comparisons that were similar to the initial sample at a level
#between 50 and 60 percent. This csv file name can be altered to a different level of comparison by changing the 50 to 60, 70, 80 etc.
file = open('50percent.csv','r')
data = csv.reader((line.replace('\0','') for line in file), delimiter = '\n')    
into = list(data)
x = len(into)
for i in into:
    temp = 0
    print(temp)
    print(x)
    for j in into:
        #this sequence matcher finds the level of comparison between two strings by calculating the level at 2*T/M where T is the number of similar
        #chars and M is the length of the longest string 
        s = SequenceMatcher(None, i, j).ratio()
        #If the level of similarity is below 50% or 100%(no need for redundancy) the feature is removed from the list of rough features        
        if s < .5 or s == 1:
            #print(s)
            into.pop(temp)
        temp += 1
    x = len(into)
    temp = 0
x = len(into)
print(into)
#The final set of features is written to the csv listed below
out = open('50filteredGOOD.csv','w')
for i in range(x):
    out.write(into[i][0])
    out.write('\n')

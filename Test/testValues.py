import csv
from difflib import SequenceMatcher

trainInit = []
testInit = []

############LISTS OS IMPORTEED FEATURES#############################
temp1 = open('90filteredOMITGOOD.csv','r')
data1 = csv.reader((line.replace('\0','') for line in temp1), delimiter = '\n')    
OMITGOODFEATS = list(data1)

temp2 = open('90filteredOMITBAD.csv','r')
data2 = csv.reader((line.replace('\0','') for line in temp2), delimiter = '\n')    
OMITBADFEATS = list(data2)

trainFeats = OMITGOODFEATS + OMITBADFEATS
#################################IMPORT TEST DOCS#######################################
OMITBAD_TRAIN1 = open('OMITBAD_TRAIN_200.txt')
OMITBAD_TRAIN1 = OMITBAD_TRAIN1.readlines()[1:]
trainInit.append(OMITBAD_TRAIN1[0])

OMITBAD_TRAIN2 = open('OMITBAD_TRAIN_3.txt')
OMITBAD_TRAIN2 = OMITBAD_TRAIN2.readlines()[1:]
trainInit.append(OMITBAD_TRAIN2[0])

OMITBAD_TRAIN3 = open('OMITBAD_TRAIN_361.txt')
OMITBAD_TRAIN3 = OMITBAD_TRAIN3.readlines()[1:]
trainInit.append(OMITBAD_TRAIN3[0])

OMITBAD_TRAIN4 = open('OMITBAD_TRAIN_25.txt')
OMITBAD_TRAIN4 = OMITBAD_TRAIN4.readlines()[1:]
trainInit.append(OMITBAD_TRAIN4[0])

OMITBAD_TRAIN5 = open('OMITBAD_TRAIN_428.txt')
OMITBAD_TRAIN5 = OMITBAD_TRAIN5.readlines()[1:]
trainInit.append(OMITBAD_TRAIN5[0])

OMITBAD_TEST1 = open('OMITBAD_TEST_16.txt')
OMITBAD_TEST1 = OMITBAD_TEST1.readlines()[1:]
testInit.append(OMITBAD_TEST1[0])

OMITBAD_TEST2 = open('OMITBAD_TEST_27.txt')
OMITBAD_TEST2 = OMITBAD_TEST2.readlines()[1:]
testInit.append(OMITBAD_TEST2[0])

OMITBAD_TEST3 = open('OMITBAD_TEST_70.txt')
OMITBAD_TEST3 = OMITBAD_TEST3.readlines()[1:]
testInit.append(OMITBAD_TEST3[0])

OMITBAD_TEST4 = open('OMITBAD_TEST_208.txt')
OMITBAD_TEST4 = OMITBAD_TEST4.readlines()[1:]
testInit.append(OMITBAD_TEST4[0])

OMITBAD_TEST5 = open('OMITBAD_TEST_173.txt')
OMITBAD_TEST5 = OMITBAD_TEST5.readlines()[1:]
testInit.append(OMITBAD_TEST5[0])

OMITGOOD_TRAIN1 = open('OMITGOOD_TRAIN_57.txt')
OMITGOOD_TRAIN1 = OMITGOOD_TRAIN1.readlines()[1:]
trainInit.append(OMITGOOD_TRAIN1[0])

OMITGOOD_TRAIN2 = open('OMITGOOD_TRAIN_193.txt')
OMITGOOD_TRAIN2 = OMITGOOD_TRAIN2.readlines()[1:]
trainInit.append(OMITGOOD_TRAIN2[0])

OMITGOOD_TRAIN3 = open('OMITGOOD_TRAIN_253.txt')
OMITGOOD_TRAIN3 = OMITGOOD_TRAIN3.readlines()[1:]
trainInit.append(OMITGOOD_TRAIN3[0])

OMITGOOD_TRAIN4 = open('OMITGOOD_TRAIN_315.txt')
OMITGOOD_TRAIN4 = OMITGOOD_TRAIN4.readlines()[1:]
trainInit.append(OMITGOOD_TRAIN4[0])

OMITGOOD_TRAIN5 = open('OMITGOOD_TRAIN_193.txt')
OMITGOOD_TRAIN5 = OMITGOOD_TRAIN5.readlines()[1:]
trainInit.append(OMITGOOD_TRAIN5[0])

OMITGOOD_TEST1 = open('OMITGOOD_TEST_15.txt')
OMITGOOD_TEST1 = OMITGOOD_TEST1.readlines()[1:]
testInit.append(OMITGOOD_TEST1[0])

OMITGOOD_TEST2 = open('OMITGOOD_TEST_87.txt')
OMITGOOD_TEST2 = OMITGOOD_TEST2.readlines()[1:]
testInit.append(OMITGOOD_TEST2[0])

OMITGOOD_TEST3 = open('OMITGOOD_TEST_263.txt')
OMITGOOD_TEST3 = OMITGOOD_TEST3.readlines()[1:]
testInit.append(OMITGOOD_TEST3[0])

OMITGOOD_TEST4 = open('OMITGOOD_TEST_491.txt')
OMITGOOD_TEST4 = OMITGOOD_TEST4.readlines()[1:]
testInit.append(OMITGOOD_TEST4[0])

OMITGOOD_TEST5 = open('OMITGOOD_TEST_421.txt')
OMITGOOD_TEST5 = OMITGOOD_TEST5.readlines()[1:]
testInit.append(OMITGOOD_TEST5[0])

testfinal = []
for i in range(0,5):
    x = testInit[i]
    print(i)
    temp = []
    for j in range(len(trainFeats)):
        s = .5
        y = trainFeats[j][0]
        z = (len(x) - len(y))
        #print(z)
        for k in range(0, z):  
            #print(x[k:len(y)+k])
            stemp = SequenceMatcher(None, x[k:len(y)+k], y).ratio()
            if stemp > s:
                s = stemp
        print(s)
        if s == .5:
            temp.append(0)
        else:
            temp.append(s)
    temp.append(1)#Class value for OMITBAD aka Good
    testfinal.append(temp)
    
#for i in testfinal:
#    i.append(1) #the first five are OMITBAD so 1 = good code this last element is the class
             
                
for i in range(5,10):
    x = testInit[i]
    print(i)
    temp = []
    for j in range(len(trainFeats)):
        s = .5
        y = trainFeats[j][0]
        z = (len(x) - len(y))
        #print(z, len(y))
        for k in range(0, z):  
            #print(x[k:len(y)+k])
            stemp = SequenceMatcher(None, x[k:len(y)+k], y).ratio()
            if stemp > s:
                s = stemp
        print(s)
        if s == .5:
            temp.append(0)
        else:
            temp.append(s)
    temp.append(0)#the last five are OMITGOOD
    testfinal.append(temp)

'''
trainfinal = []
for i in range(0,5):
    x = trainInit[i]
    print(i)
    temp = []
    for j in range(len(OMITBADFEATS)):
        s = .5
        y = OMITGOODFEATS[j][0]
        z = (len(x) - len(y))
        #print(len(y))
        #print(z, len(y))
        for k in range(0, z):  
            #print(x[k:len(y)+k])
            stemp = SequenceMatcher(None, x[k:len(y)+k], y).ratio()
            if stemp > s:
                s= stemp
        print(s)
        if s == .5:
            temp.append(0)
        else:
            temp.append(s)
    temp.append(1) #the first five are OMITBAD so 1 = good code this last element is the class
    trainfinal.append(temp)
                
for i in range(5,10):
    x = trainInit[i]
    print(i)
    temp = []
    for j in range(len(OMITGOODFEATS)):
        s = .5
        y = OMITGOODFEATS[j][0]
        z = (len(x) - len(y))
        #print(z)
        for k in range(0, z):  
            #print(x[k:len(y)+k])
            stemp = SequenceMatcher(None, x[k:len(y)+k], y).ratio()
            if stemp > s:
                s = stemp
        print(s)
        if s == .5:
            temp.append(0)
        else:
            temp.append(s)
    temp.append(0)#the last five are OMITGOOD
    trainfinal.append(temp)
'''
    
#print(trainfinal)     

print(testfinal) 








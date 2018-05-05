#!/usr/bin/env python
import glob, os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'*.bin')
dir_path = os.path.dirname(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
filelist= glob.glob(os.path.expanduser(path))
#filelist = os.path.dirname(os.path.realpath(__file__)) #<-- absolute dir the script is in

temp = 0
for i in filelist:
    
    with open(i, 'r') as file:
            file = file.read()
            if len(file) %2 == 0:
                out = open('%sDNA_%s.txt' % (i,temp) ,'w+')
                DNA = ""
                for x in range(0, len(file), 2):
                    j =''    
                    j += file[x]
                    if file[x+1]:
                        j += file[x+1]
                    
                        if j == '00':
                            DNA += ('ATT')
                        if j == '01':        
                            DNA += ('C')
                        if j == '10':
                            DNA += ('G')
                        if j == '11':        
                            DNA += ('TAA')
                #print(DNA)
                out.write(">"+str(temp)+"\n"+DNA)
                temp += 1
            

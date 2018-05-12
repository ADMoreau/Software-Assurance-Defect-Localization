#!/usr/bin/env python
'''
This code is designed to translate the binary object files that the path is defined as into a DNA analogue capable of being 
considered in FASTA format for the mVista software to be able to work with it. 
FASTA is a common formatting style many genome sequencing programs require.
In this case a numerical representation of the file number is appended to the first line of a text file with a binary to DNA sequence on the 
next line 
For example.
>496
ATTGATGGACCGTATAGCGATAGCTAGCC....

Side note: originally the researchers intended to have a direct translation where two bits would represent a single base but due to the fact 
that this would result in long sequences of single letters, which is something the mVIsta software was not designed to handle, the researchers
had to reformat the translation to what is used below.
'''
import glob, os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'*.bin')
dir_path = os.path.dirname(os.path.abspath(__file__))
#print(os.path.dirname(os.path.abspath(__file__)))
filelist= glob.glob(os.path.expanduser(path))
#filelist = os.path.dirname(os.path.realpath(__file__)) #<-- absolute dir the script is in

temp = 0
for i in filelist:
#WIth the file open as i and as long as there are two more chars in the sequence the next few lines take a duo of chars and translates them     
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
                    #j represents the two chars to be translated and depending on the two chars the next step appends a predesignated string of 
                    #base pairs to the DNA string holding the entire translation 
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
            

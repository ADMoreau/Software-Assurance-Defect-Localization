#importing libraries
import urllib
from bs4 import BeautifulSoup
import os
import sys

#reading in the file of url links
file1 = open(sys.argv[1])

urllist = file1.read().split()

#variable for file number
holder = 48
#variable to keep track of numbering and to avoid situations as "1-1" in numbering of text file
pp = 46


for item in urllist:

	os.makedirs("Sequencedatarun271/sequence"+ str(holder)+"/")
	#start of the sequence
	count = 55
	sequenceurl=[]
	for num in range(55,155):
		try:
			url = (item +str(count))
			html = urllib.urlopen(url).read()
			soup = BeautifulSoup(html,'html.parser')
		except Exception as e:
			print e
		else:
			for link in soup.find_all('a', string ="Get all CNS alignments"):
				sequenceurl.append(link.get('href'))
		count +=1
	#end of second for loop
	index = 0
	pair = 1
	
	#loop to read in all the links gathered from the first link
	for item in sequenceurl:
		try:
			url = ("http://pipeline.lbl.gov/"+sequenceurl[index])
			html = urllib.urlopen(url).read()
			fsoup = BeautifulSoup(html,'html.parser')
		except Exception as a:
			print a
		else:
			if pair > pp:
				f = open("Sequencedatarun271/sequence"+str(holder)+"/sequence"+str(holder)+"-"+str(pair+1)+".txt","w")
				for link in fsoup.find_all('pre'):
					f.write(link.text)
			else:
				f = open("Sequencedatarun271/sequence"+str(holder)+"/sequence"+str(holder)+"-"+str(pair)+".txt","w")
				for link in fsoup.find_all('pre'):
					f.write(link.text)
			f.close()
			index +=1
			pair +=1
	pp += 1
	holder+=1	
	#end of third loop
print "Downloaded sequence" + str(holder)
#end of first loop

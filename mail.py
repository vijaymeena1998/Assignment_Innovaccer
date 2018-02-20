'''EXTRACTING MAIL IDs FROM A GIVEN TEXTFILE:
											Program iterates through each line and using Regular Expression Library it seaches for any number of mail IDs in that line.
'''
import os,re

while True:
	try:
		filename=input('Enter filepath without extension: ')
		fhand=open(filename+'.txt')
		break
	except:
		print('Filepath has not been located.\n')			

for line in fhand:
	line=line.rstrip()
	l=re.findall('\S+@[a-zA-Z.]+\S',line)
	if len(l)>0:
		print (l)	
input('All mail IDs have been retrieved')
import csv
import re
import pprint as pp

with open('faculty.csv', newline='') as csvfile:
	f = csv.reader(csvfile)
	next(f)
	faculty = list(f)

degree = {}
title = {}
email_address = []
email = set()

for staff in faculty:
	#degree
	d = re.findall('\S.\S*', staff[1])
	for a in d:
		degree[a.replace('.', '')] = degree.get(a.replace('.', ''), 0)+1
	
	#title
	t = re.search('^.+B', staff[2]).group()[:-5]
	title[t] = title.get(t, 0)+1

	#email
	email_address.append(staff[3])
	e = re.search('(@.*$)' , staff[3]).group()[1:]
	email.add(e)

#Q1: different degrees and their frequencies
print (degree)

#Q2: different titles and their frequencies
print (title)

#Q3: ist of email addresses
pp.pprint(email_address)

#Q4: different email domains 	
print (list(email))

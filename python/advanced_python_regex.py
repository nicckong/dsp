import csv
import re

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

print (degree)
print (title)

for e in email_address:
	print (e)
	
print (list(email))

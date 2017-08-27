import csv
import re
from collections import defaultdict

with open('faculty.csv', newline='') as csvfile:
	f = csv.reader(csvfile)
	next(f)
	faculty = list(f)

# stripping off space character in the beginning
for space in faculty:
	space[1] = space[1].lstrip()

faculty_dict = defaultdict(list)
professor_dict = {}

for staff in faculty:
	lastname = re.search('\w*$', staff[0]).group()
	faculty_dict[lastname].append(staff[1:])

	firstname = re.search('^\w*', staff[0]).group()
	professor_dict[firstname, lastname] = staff[1:]

#Q6: first 3 elements in faculty_dict
print ({k: faculty_dict[k] for k in sorted(faculty_dict.keys())[0:3]})

#Q7: first 3 elements in professor_dict
print ({k: professor_dict[k] for k in sorted(professor_dict.keys())[0:3]})

#Q8: sort by lastname
for k,v in sorted(professor_dict.items(), key= lambda x : x[0][1]):
	print (k, v)




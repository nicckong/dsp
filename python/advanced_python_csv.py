import csv

with open('faculty.csv', newline='') as csvfile:
	f = csv.reader(csvfile)
	next(f)
	faculty = list(f)

email_address = []

for staff in faculty:
	#email
	email_address.append(staff[3])

with open('emails.csv', 'w') as myfile:
	wr = csv.writer(myfile)
	wr.writerow(['list_of_emails'])
	wr.writerows([email] for email in email_address)
myfile.close()
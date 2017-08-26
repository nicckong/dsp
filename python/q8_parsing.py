# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
result = dict()

with open('football.csv', newline='') as csvfile:
	football = csv.reader(csvfile)
	next(football)
	teams = list(football)

#using dictionary
for team in teams:
	result[team[0]]= abs(int(team[5]) - int(team[6]))

print (min(result, key=result.get))

'''
#for hackerrank

diff = 0
count = 0
result = 0
for team in teams:
	team.append(abs(int(team[5]) - int(team[6])))
	if count == 0:
		diff = team[-1:]

	elif team[-1:] < diff:
		diff = team[-1:]
		result = count
	count += 1

print (teams[result][0])'''







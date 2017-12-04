import csv

print("Welcome to the GPA calculator.")

grading = {'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.70, 'C+': 2.30, 'C': 2.0, 'C-': 1.70, 'D+': 1.30, 'D': 1.0, 'D-': 0.7, 'F': 0.0}

courses = 0
total = 0 

with open('students.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	user = input('Whats your name?: ')
	for row in reader:
		x = row[user]
		print(x)
		if x in grading:
			courses += 1
			total += grading[x] 
if courses > 0:
	print('Your GPA is %0.2f' % (total / courses))

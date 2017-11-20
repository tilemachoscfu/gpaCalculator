import csv

print("""Welcome to the GPA calculator.
Please enter all your letter grades, one per line.
Enter a blank line to designate the end.""")

grading = {'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.70, 'C+': 2.30, 'C': 2.0, 'C-': 1.70, 'D+': 1.30, 'D': 1.0, 'D-': 0.7, 'F': 0.0}

with open('students.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
	 

courses = 0
total = 0
boolean = True

while boolean:
	grade = input().upper()
	if grade == '':
		boolean = False
	elif grade not in grading:
		print("Unknown grade %s" % (grade))
	else:
		courses += 1
		total += grading[grade]

if courses > 0:
	print('Your GPA is %0.2f' % (total / courses))

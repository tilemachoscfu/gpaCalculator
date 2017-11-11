print("Welcome to the GPA calculator.")
print("Please enter all your letter grades, one per line.")
print("Enter a blank line to designate the end.")

points = {'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.70, 'C+': 2.30, 'C': 2.0, 'C-': 1.70, 'D+': 1.30, 'D': 1.0, 'D-': 0.7, 'F': 0.0}

num_courses = 0
total_points = 0
done = False
while not done:
	grade = input()
	if grade == '':
		done = True
	elif grade not in points:
		print("Unknown grade '{0}' being ignored".format(grade))
	else:
		num_courses += 1
		total_points += points[grade]
if num_courses > 0:
	print('Your GPA is {0:.3}'.format(total_points / num_courses))

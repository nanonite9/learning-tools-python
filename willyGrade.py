# Write a function that outputs the letter grade, after the meanie pants instructor Ms. Williams subtracts 5% from everyone
def willyGrade(grade):
	grade = grade - 5           #subtracts 5 points from every mark a student gets
	if 80 <= grade <= 100:
		return 'A'          #this range gives output 'A'
	elif 70 <= grade < 80:
		return 'B'          #this range gives output 'B'
	elif 60 <= grade < 70:
		return 'C'          #this range gives output 'C'
	elif 50 <= grade < 60:
		return 'D'          #this range gives output 'D'
	else:
		return 'F'          #if not above, 'F'
'''
Test Case:
>>> willyGrade(73)
'C'
'''

score = float(input('Please enter your score:'))
grade = 'Unknown'
if score >= 85:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'D'
# Check grade

print('Your level is:', grade, 'Good luck next time!')  # Print grade

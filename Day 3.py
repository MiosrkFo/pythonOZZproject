score = float(input('Please enter your score:'))
grade = 'Unknown'
if score == 114514:
    print('Come on! Enter the current answer!')
elif score >= 85:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'D'

print('Your level is:', grade, ', Good luck next time!')  # Print grade

# Practise 1
def fahrenhelt_to_celsus():
    fahrenhelt_temperature = float(input('Please enter the Fahrenheit temperature: '))
    celsus_temperature = (fahrenhelt_temperature - 32) / 1.8
    print('%.1f Fahrenheit = %.1f Celsius' % (fahrenhelt_temperature, celsus_temperature))


# Practise 2
def circle_calculator():
    radius = float(input('Please enter the radius of the circle: '))
    perimeter = 2 * 3.1415926536 * radius
    area = 3.1415926536 * radius * radius
    print('Perimeter: %.2f' % perimeter)
    print('Area: %.2f' % area)


# Practise 3
def leap_checker():
    year = int(input('Please enter the year: '))
    # If the code is too long to write on a single line and it is not easy to read, you can use \ to wrap the code
    is_leap = year % 4 == 0 and year % 100 != 0 or \
              year % 400 == 0
    print(is_leap)


function = int((input('Please enter the functional that you need\
(1 for leap_checker, \
2 for circle_calculator, \
3 for fahrenhelt_to_celsus): ')))
if function == 3:
    fahrenhelt_to_celsus()
elif function == 2:
    circle_calculator()
elif function == 1:
    leap_checker()
else:
    print('Wrong options!')

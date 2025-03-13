# exercises week 1: Python

# 1.
print('\\')

# 2.
hotel_name = 'Adler'

print(type(hotel_name))

# 3.
user_number = float(input('Enter a number: '))
print(user_number)

# 4.
selected_weekday = input('Select a weekday: ')

if selected_weekday.lower() in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
    print('The selected weekday is a Workday')
elif selected_weekday.lower() in ['saturday', 'sunday']:
    print('The selected weekday is a weekend')
else:
    print('What you entered is not a weekday, please try again')

# 5.
def BMI_formula(weight, height):
    BMI = weight / (height**2)
    return BMI

print(round(BMI_formula(74, 1.7),2))

# 6.
def BMI_input():
    weight = float(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))
    return (weight, height)

BMI_input()

# 7.
def bmi_calculation():
    weight = float(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))
    bmi = weight / (height ** 2)
    return bmi
user_bmi = round(bmi_calculation(), 2)
print('Your BMI is: ', user_bmi)

# 7.2.
def bmi_calculation():
    weight = float(input('Enter your weight in kilograms: '))
    height = float(input('Enter your height in meters: '))
    bmi = weight / (height ** 2)
    print(bmi)

bmi_calculation()
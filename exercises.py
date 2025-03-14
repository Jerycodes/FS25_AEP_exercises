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

# exercises week 2: Python

# 1.
number_1 = 224
number_2 = '435.5'
number_3 = 435.5

# 2.
print(type(number_1))
print(type(number_2))
print(type(number_3))

# 3.
number_1 = str(number_1)
number_2 = float(number_2)
number_3 = int(number_3)

print(type(number_1))
print(type(number_2))
print(type(number_3))

print(number_1)
print(number_2)
print(number_3)

# 4. -

# 5.
var_1 = ["This is my ", "list number", 1]
var_2 = ("This is my ", "tuple number", 1)
var_3 = {"dict_numb" : 1, "content": "this is my first dictionary"}
var_4 = {"this is my ", "set number", 1}

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

# 7.
list_1 = ["liste", 455, "another string"]
print(list_1[1])

# 8.
#a)
list_1.append(66)

#b)
list_2 = ["hello", 312]
list_1.append(list_2)

#c)
print(list_1)

#d)
print(list_1[4][1])

#e)
list_3 = ["another", "list"]
list_1.extend(list_3)

#f)
print(list_1[-2])

# 9.
#a)
list_numbers = [1,2,3,4,5,6,7,8,9,10]
for number in list_numbers:
    print(number)

for number in range(1, 11):
    print(number)

#b)
z = 1
while z < 11:
    print(z)
    z += 1

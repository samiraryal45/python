print('o----')
print(' ||||')
print('1' * 10)


name='John Smith'
age=20
check_in=True
print(name)
print(age)
print(check_in)


name=input('whst is your name?  ')
color=input("What is your favourite color? ")
print(name + ' likes ' + color + '.' )

birth_year=input('What is you birth year: ')

age=2025 - int(birth_year)
print( str(age) + ' years old ')


weight_in_pounds=input("What's your weight in pounds? ")
weight_in_kgs=0.45* float(weight_in_pounds)
print('Your weight is ' +str(weight_in_kgs) +' kilogram.')

a=5
b=f'{a} is a prime number'
print(b)

a=input('what is your name ')
print('The length of yor name is ' + str(len(a)))

a=input('write your name ')
print('Your name in uppercase is ' + a.upper())
print(a.find('l'))

a=50
b=f'You got this marks in your examination {a}'
print(b.upper())

a=' chus'
print(a.replace('kha'))


a='hello I am from Nepal,Kathmandu'
print(a.find('l'))

print(3*2)

x=5
x *= 5
print(x)


x=5.49()
print(round(x))

x=-3
print(abs(x))

import math
print(math.sin(30))


import math

print(math.factorial)
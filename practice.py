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



print(math.factorial)

is_holiday =False
is_college=False

if is_holiday:
    print("Go travel")
elif is_college:
    print("Go college")   
else:
    print("Sleep")     
    
    payment=int(input('enter the payment you want to offer '))
credit= int(input("enter the credit you want to offer "))

if payment>10000 and credit>1200:
    print(' Deal confirmed')
else:
    print(f'Increase the payment or the credit')
    
    
name=input('what is your name')
if len(name)<3:
    print('The name must be at least 3 characters long')
    
elif len(name)>10:
    print('The name must be maximum of 10 characters long')    
    
else:
    print('The name is perfect')    
    
    a=5
while a<=50:
    print(a)
    a=a+5



i=1
n=int(input('Enter a number to calculate its multiplication table '))
print(f'The multiplication table of {n} is as follows')
while i<=10:
    a=n*i
    print(f'{n} * {i} = {a}')
    i=i+1

a=1
while a<=5:   
     print('*' * a)
     a=a+1    
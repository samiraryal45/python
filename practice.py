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
     
     
secret_num=5
i=0 

while i<3:
    
    a=int(input('Give a number'))
    i=i+1
    if a==secret_num:
        print('the secret number is 5')
        break
    else:
        print(f'{a} is not the secret number')  
         
print('you have used your all attempts')         


command =''
while True:
    command=input('> ').lower()
    if command =='start':
        print('The car is started.... Ready to Go!!')
    elif command =='stop':
        print('The car is stopped')
    elif command =='help':
      print(''' 
Write the commands:
start - to start the car
stop - to stop the car
quit - to exit the game 
''')   
    elif command =='quit':
        break          
                
    else:
        print("""
Cannot understand this .
TYPE help/HELP for details....      
""")    
        
for a in range(4,10,3):
    print(a)
    
marks =[52,44,56,68,40,60]
full_marks=[75,75,75,75,75,50]
total_marks_obtained =0
actual_total_marks=0

for result,full in zip(marks,full_marks):
   total_marks_obtained += result
   actual_total_marks += full
print(f'The total marks obtained as a result is {total_marks_obtained}. ')
print(f'Total marks is {actual_total_marks}.')

for a in [5-1,10//4]:
    print(a)    
                     
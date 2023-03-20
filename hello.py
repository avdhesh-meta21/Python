print("Avdhesh")

# Single Line Comment

"""
Multiple
line
comment
"""

# We do not have to specify data types in python it by defalut assings the data type to the variable
a = 10        # a is of integer datatype
d = 12.23     # f is of floating datatype
s = 'string'  # s id of string datatype

# Complex numbers in python can be defined as 
c1 = complex(2,4) #or
c2 = 2+4j

# We can define binary and hexadecimal values in python using 0B and 0X as prefix respectively
b = 0B1001 #Binary
h = 0X12F  #Hexadecimal

#Boolean type
t = True
f = False


#Type Conversion in python
i = int("22")
#Similarly, we have float(), bin(), hex() and oct() to convert into float, binary, hexadecimal and octal numbers

#We can get the type of datatype using type() function
#So let's check the type of all of the above varibles
print("a is of type")
print(type(a))

print("d is of type")
print(type(d))

print("s is of type")
print(type(s))

print("c1 is of type")
print(type(c1))

print("c2 is of type")
print(type(c2))

print("b is of type")
print(type(b))

print("h is of type")
print(type(h))

print("t is of type")
print(type(t))

print("f is of type")
print(type(f))

print("i is of type")
print(type(i))


#String can be written inside both single quotes ' ' and double quotes " "
str1 = "Hello World"
str2 = 'Hello World'

#Multiple line String can be written using triple single or double quotes """ """ or ''' '''
str3 = """ We can write String 
in multiple lines like this """
str4 = ''' and also 
like this'''

#We can convert any datatype or object to string using str() function
str5 = str(43)         #Integer to String
str6 = str([3,23,85])  #List to String

#We can access a string using its indexes and in string indexing starts from 0
S = "ABCDEFGHIJKL"
print(S[0]) #A will be printed

#Similarly we can access the string using negative indexing
#-1 refers to the last index and the index gets deceresing as we move towards start
print(S[-2]) #K will be printed as it is at 2nd last index

#We can slice the string using the slice operator
#it slices the string from the given starting index to the ending index
#Starting index is included whereas the last index is excluded
print(S[1:5]) #prints BCDE

#Strings are immutable in python so we cannot directly change a string 
#We can create a new string which is the variation of the existing string
Str = "Hello World"

new_Str = "Namaste"+Str[5:] #[5:] will print the entire string from index 5
# print(new_Str)

#We can find the length of the string using the len() function
print(len(Str)) #Prints 11


# We can split a string into a list by specifying a specific character
Str2 = "laptop,monitor,mouse,keyboard"
S_Str = Str2.split(',')
print(S_Str)

#Vice versa we can convert a list into string using the join function
J_Str = ','.join(S_Str)
print(J_Str)


#We can do case conversion of a string using lower(), upper(), capitalize(), swapcase() and title()
U_Str = Str.upper()
print(U_Str)

#We can iterate a string using a for loop
for s in Str:
    print(s) #In this way each character is printed in different line

for s in Str:
    print(s, end="") #In this wholw line is printed in the same line
print()

print(S[::-1])  #Reverses the string

Strx=""

for s in Str: 
    if s == ' ':
        print(Strx)
        Strx = ''
    else:
        Strx = Strx+s

print(Strx)

#OPERATORS
#Arthematic Operators in Python
x = 16
y = 4

# + Operator (Addition)
print('x + y =',x+y)

# - Operator (Substraction)
print('x - y =',x-y)

# * Operator (Multiplication)
print('x * y =',x*y)

# / Operator (Division)
print('x / y =',x/y)

# // Operator (Gives remainder fllor value in int)
print('x // y =',x//y)

# ** Operator (x to the power y)
print('x ** y =',x**y)

#Comparison Operators in Python

# > Operator (returns true if LHS is greater than RHS)
print('x > y is',x>y)

# > Operator (returns true if RHS is greater than LHS)
print('x < y is',x<y)

# > Operator (returns true if LHS and RHS are equal)
print('x == y is',x==y)

# > Operator (returns true if LHS and RHS are not equal)
print('x != y is',x!=y)

# > Operator (returns true if LHS is greater than or equal to RHS)
print('x >= y is',x>=y)

# > Operator (returns true if RHS is greater than or equal to LHS)
print('x <= y is',x<=y)

#Logical Operators in Python
x = True
y = False

# and Operator (retuens true if both values are true)
print('x and y is',x and y)

#or Operator (returns true if any one value is true)
print('x or y is',x or y)

#not Operator (returns true if false and vice versa)
print('not x is',not x)

#Flow Control Statements
#If statement
num = 3

if num > 0:
    print(num, "is a positive number.")

#If else Statement
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

#If elif else Statement
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#Nested If Statement
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

#for loop
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
	sum = sum + val

print("The sum is", sum)

#while loop
n = 10

sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1

print("The sum is", sum)

#functions in python
def greet(name):
    print("Hello, " + name + ". Good morning!")

greet('Avdhesh')

#function with return statement
def absolute_value(num):
    if num >= 0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))

#function having multiple number of arguments
def greet(*names):
    for name in names:
        print("Hello", name)

greet("Monica", "Luke", "Steve", "John")

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))


#List Comprehension in python

#using normal method
h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

#using lambda function
letters = list(map(lambda x: x, 'human'))
print(letters)

#using List Comprehension
H_letters = [ letter for letter in 'human' ]
print(H_letters)


#OOPs in Pyhton
class Phone:
    def set_color(self, color):
        self.color = color

    def set_cost(self,cost):
        self.cost = cost

    def get_color(self):
        print(self.color)

    def get_cost(self):
        print(self.cost)

    def make_call(self):
        print("Making a call")

    def play_game(self):
        print("playing a game")

phone = Phone()
phone.set_color("blue")
phone.set_cost(5000)
phone.get_color()
phone.get_cost()
phone.make_call()
phone.play_game()

class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of Employee is", self.name)
        print("Age of Employee is", self.age)
        print("Salary of Employee is", self.salary)
        print("Gender of Employee is", self.gender)

e1 = Employee("Avdhesh", 20, 10000, "Male")

e1.employee_details()

#Inheritance
class Vehicle:
    def __init__(self, cost, mileage):
        self.cost = cost
        self.mileage = mileage

    def show_details(self):
        print("I am Vehicle")
        print("Cost of Vehicle is " ,self.cost)
        print("Mileage of Vehicle is " ,self.mileage)

v1 = Vehicle(5000, 20)
v1.show_details()

#Over riding init method(Constructor)
class Car(Vehicle):
    def __init__(self, cost, mileage, company, hp):
        super().__init__(cost, mileage)
        self.company = company
        self.hp = hp

    def show_car_details(self):
        print("I am car")
        print("Company of car is", self.company)
        print("Horsepower of car is", self.hp)

c1 = Car(10000, 25, "Toyota", 2000)
c1.show_details()
c1.show_car_details()

#Multiple Inheritance
class Parent1:
    def set_string_one(self, s1):
        self.s1 = s1
    def get_string_one(self):
        print(self.s1)

class Parent2:
    def set_string_two(self, s2):
        self.s2 = s2
    def get_string_two(self):
        print(self.s2)

class Child(Parent1, Parent2):
    def set_string_three(self, s3):
        self.s3 = s3
    def get_string_three(self):
        print(self.s3)

child = Child()
child.set_string_one("I am string of parent1")
child.set_string_two("I am string of parent2")
child.set_string_three("I am string of child")
child.get_string_one()
child.get_string_two()
child.get_string_three()

#Multi-level Inheritance
class Parent:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        print("Name is " ,self.name)

class Child(Parent):
    def set_age(self, age):
        self.age = age
    def get_age(self):
        print("Age is ", self.age)

class Grandchild(Child):
    def set_gender(self, gender):
        self.gender = gender
    def get_gender(self):
        print("Gender is ", self.gender)

gc = Grandchild()
gc.set_name("Mohan")
gc.set_age(22)
gc.set_gender("Male")
gc.get_name()
gc.get_age()
gc.get_gender()

#Exception handling
try:
    a = int(input("Enter Dividend: "))
    b = int(input("Enter Divisior: "))
    print("a/b = ",a/b)
except:
    print("Divisior should not be 0")

#file handling
try:
    f = open("text.txt",'r+t')
    f.read()
    f.write("my first text file\n")
finally:
    f.close()

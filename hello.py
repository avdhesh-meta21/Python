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









s = "My name is Avdhesh"

str2446=""

for x in s:
    if x == ' ':
        print(str2446)
        str2446 = ''
    else:
        str2446 = str2446+x

print(str2446)
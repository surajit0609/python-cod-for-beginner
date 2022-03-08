from __future__ import division
from ast import operator


a=34
b=56
c=45
# Arithmetic Operators
# Addition
print("the value of a+b=",a+b)
# Subtraction
print("the value of a-b=",a-b)
# Multiplication
print ("the valu of a*b =",a*b)
# division
print("the valu of a/b",a/b)
# Modulus
print('the value of b%a=',b%a)
#  Exponentiation Operator
s=2
f=3
print(f**s)
# assignment
d=45
d+=2
print(d)
# comparison operator
# Examples of Relational Operators
a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)

# logical operator(and, or ,not)
a=34
b=45
c=56
if a>b and b>c :
    print("a is max")
elif b>c and a>c :
    print("b is max")
else:
    print("c is max")    

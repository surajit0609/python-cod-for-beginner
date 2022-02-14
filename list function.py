#python list fuction :--https://www.programiz.com/python-programming/methods/list/append


shop=["dress","shose","drink","water",34]
print(shop[2])
numbers=[1,3,45,67,7,3,6,78,2,5,87,3,5,87,7,3,76,8,2,6,8]
print(numbers[3])
#maximum numbers of python
print(max(numbers))
# minmum numbers of python 
print(min(numbers))
#lenth of the list
print(len(numbers))
#list reversed
print(list(reversed(numbers)))
#append 
numbers.append(23)
numbers.append(23)
numbers.append(23)
numbers.append(23)
print(numbers)
#insert
numbers.insert(1,34)
print(numbers)
#remove 
numbers.remove(45)
print(numbers)
#pop
numbers.pop()
print(numbers)
numbers[1]=14
print(numbers)
#mutable=can change
#immutable=can not change
tq=(1,4,6,7)
# tq[1] =7 can not be used this number
print(tq)
sk=(1,)
print(sk)
#inter change for 2 numbers
z=12
k=23
#temp=z
#z=k
#k=temp
#python using this code
k,z=z,k
print(z,k)
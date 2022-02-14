age=36
# txt='my name is jhon, iam' +age
# print(txt)
# error becuse we can not combine strings and numbers by using the the format()method

txt="my name is jhon ,i am {}"
print(txt.format(age))

quantity =3
itemon =567
price =49.95
#myorder ="I want {} prices of item {} for {} dollars."
#print(myorder.format(quantity,itemon,price))
 myorder="i want to pay {2} dollars for {0} prices of item {1} "

print(myorder.format(quantity,itemon,price))
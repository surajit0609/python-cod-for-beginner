mystr="surajit is a good programmer"
print(mystr[3])
print(mystr[0:10])
print(mystr[:10]) #is same as mystr[0:10]
print(mystr[0:]) #is same as mystr[0:28]
print(len(mystr))
print(mystr[0:7:3])
print(mystr[::])
print(mystr[0:10])
print(mystr[:])
#negative slicing
print(mystr[-5:-3]) 
#isalnum string
a="surajit123"
print(a.isalnum())
b="sur 123"
print(b.isalnum())
c="motal"
print(c.isalnum())
#isalpha string
mystr="jonnyisagoodboy"
print(mystr.isalpha())
mystr="jonnyisagoodboy1234"
print(mystr.isalpha())
#endwith string
sk="mia is a good girl"
print(sk.endswith("girl"))
#count string
print(sk.count("a"))
print(sk.count("y"))
print(sk.count("o"))
#capitalize string
print(sk.capitalize())
#find 
print(sk.find("girl"))
#lower case & upper case
print(sk.lower())
print(sk.upper())
#replace string
print(sk.replace("is","are"))

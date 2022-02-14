#dictionary is nothing but key valu pairs


d1={}
d2=()
d3=[]
print(type(d1))
print(type(d2))
print(type(d3))
dic={"surajit":"chicken","rahul":"chockelt","subha":"coldrinks","arijit":{"B":"roati","l":"rice","d":"chicken biriney"}}

print(dic)
print(dic["rahul"])
print(dic["subha"])
print(dic["arijit"]["B"])
dic["swpan"]="janck food"
dic["rajesh"]="dry bread"
print(dic)
#del dic["swpan"] then dic remove swpan
dic1=dic
print(dic1)
dic.update({"leena":"toffe"})
print(dic.keys())
print(dic.items())
#question
print("wc to dictionary")
d5={"set":"A set of things is a number of things that belong together or that are thought of as a group","mutable":"can change","immutable":"can not change"}
search=input()
print(d5[search])



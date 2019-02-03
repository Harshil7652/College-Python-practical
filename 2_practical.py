print("------------Practical 2------------")
#List Programs
#append in list
print("------Program for list------")
animals=list()
numbers=int(input("How many animals you like to add"))
x=0

for x in range(numbers):
	animal_name=input("Enter Animal name")
	x=x+1
	animals.append(animal_name)
print(animals)	
#print(animals.pop())
animals.remove("Tiger")
print("After Removing",animals)
#Sort the list
animals.sort()
print("After sorting",animals)
#Copy the List to another list
animal_copy=animals.copy()
print("After Copying:-",animal_copy)

#Dictionary Programs
print("------Program For Dictionary------")
profile={}
flag=0
num=int(input("How many details you want to enter:-"))
x1=0
for x1 in range(num):
	key=input("Enter the Key:-")
	value=input("Enter the Value:-")
	profile[key]=value
print("Dictionary:-",profile)
age=profile.get("Age")
print(age)
for x,y in profile.items():
	print(x,y)
print("Values are in Profile are following")
for x1 in profile.values():
	print(x1)

#Tuple Program
print("------Program for tuple------")
names=("Sankar","Shekhar","Gandhi","Nehru","Yadav","Modi")
for name in names:
	print(name)
if "Sankar" in names:
	print("Yes Exists")
else:
	print("Not found")
print("Length is:-",len(names))
index=names.index("Gandhi")
print("Index of Gandhi is:-",index)
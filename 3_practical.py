#List Mutability
print("------------Practical 3------------")
print("------List Mutability------")
names=["Harshil","Hinal","Hemal","Heeva","Hardik"]
print("Before Editing:-",names)
for name in names:
	if name=="Harshil":
		index=names.index("Harshil")
		names[index]="Harsh"
#Here Index one is replaced by the Harsh
print("After Editing:-",names)

#Function Scoping
print("------Function Scoping------")
x=4#Global Elemnt
def outer (number):
	def inner():
		nonlocal number
		number=5
		print("inner:- ",number)
	inner()
	print("Outer:- ",str(number))
outer(9)
print("Global",x)


#recursion in python

def func_factorial(x):
	if x==1:
		return 1
	else:
		return(x*func_factorial(x-1))

num=int(input("enter the number to find Factorial:-"))
print("The Factorial is of ",num,"is ",func_factorial(num))
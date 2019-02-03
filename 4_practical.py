#Exception Handling
#1.Division by Zero Exception
'''print("------------Exception Handling------------")
print("------Division by Zero Exception------")
def Division(number,divider):
	try:
		answer=number/divider
	except ZeroDivisionError as e:
		print("No number can divide by zero")
	else:
		print("Answer is:-",answer)
	finally:
		print("Done.")

Division(num,divider)'''
#2.Raising the Error
def raise_error(number,divider1):
		answer1=number/divider1
		print("Answer:-",answer1)

flag=0
while flag==0:
	num=int(input("Enter Number:-"))
	divider=int(input("Enter Divider:-"))
	if divider==0:
		raise Exception("Please Enter correct divider")
		flag=0
		continue
	else:
		raise_error(num,divider)
		flag=1
	
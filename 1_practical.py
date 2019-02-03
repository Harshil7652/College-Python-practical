print("------------practical1------------")
#there are main two type of control statement 1.loop 2. if-else
#1.loop there two types of loops
#1.1 FOR LOOP and WHILE loop
#For Loop
print("------For Loop------")
names=["Harshil","Hinal","Hemal","Heeva","Arun","Nisha"]
count_name=0
for count in range(len(names)):
	print(names[count])
	count=count+1
print("------While Loop------")
sports=["Volleyball","Cricket","Football","Kabaddi","Sqash"]
count_sport=0
while count_sport<len(sports):
	print(sports[count_sport])
	count_sport=count_sport+1
#If-else
print("------If-else------")
#pass or fail program
marks=input("Enter Marks to check pass or fail")
if int(marks)<35:
	print("You have failed in exam")
elif int(marks)>35 and int(marks)<=100:
	print("You have passed in the exam")
else:
	print("Please enter correct marks")
#pass and break 
name="Harshil"
print("------Output of Break------ ")
for letter in name:
	if letter == "h":
		break
	print("Letter :- ",letter)
print("------Output of continue------ ")
for letter1 in name:
	if letter1 == "i":
		continue
	print("Lettre:- ",letter1) 
print("------Output of pass------ ")	
for letter2 in name:
	if letter2 == "s":
		pass
	print("Letter:- ",letter2)
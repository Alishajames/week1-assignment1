#Print first 10 natural numbers using while

num=1
while num<=10:
    print(num)
    num+=1

# Take Input from user , and print even number till that input number

number=int(input("enter a number "))

for i in range(2,number+1,2):
    print(i)

# Take Input from user , and print odd number till that input number
number=int(input("enter a number "))

for i in range(1,number+1,2):
    print(i)

# Take Input from user , and print prime number till that input number
#number=int(input("enter a number "))


#for i in number:



# Print multiplication table of a given number
number=int(input("enter a number to get multiplication table "))
for i in range(1,11):
    print(number,"*",i,"=",i*number)

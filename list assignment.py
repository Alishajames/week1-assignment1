#revserve a list
A=[4,5,6,7,8,]
B = A[::-1]
print(B)


#Turn every item of a list into its square

A=[i**2 for i in A]
print(A)


#Remove empty strings from the list of strings
A=["Apple","","Banana","","grapes",""]
i=0
while i<len(A):
    if A[i]=="":
        A.pop(i)
    else:
        i=i+1

print(A)


#Add new item to list after a specified item
A=["Apple","","Banana","","grapes",""]
if "Banana" in A:
    index=A.index("Banana")
    A.insert(index+1,"oragan")

print(A)


#Replace list’s item with new value if found

list=[]
while True:
    item=input("Enter items or type done to finish : ")
    if item.lower()=='done':
        break
    else:
        list.append(item)

print("Your list is: " ,list)
find=input("Enter a item you want to replace : " )
replace=input("Replace with : ")
if find in list:
    index=list.index(find)
    #A.pop(index)
   #A.insert(index,3)
    list[index]=replace
    

print(list)






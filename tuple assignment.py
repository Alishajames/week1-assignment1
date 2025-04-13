#Reverse the tuple
tup=(2,3,4,5,6,30,20)
print(tup[::-1])


#Access value 20 from the tuple
if 20 in tup:
    index=tup.index(20)
    print("value 20 found at index: ", index)
else:
    print("value not found")

#Swap two tuples in Python
A = (1,2,3,4,5,6)
B = (6,7,8,9,10,11)

print("Before swap A: ", A )
print("Before swap B: ", B )

C=A
A=B
B=C

print("After swap A: ", A )
print("Before swap B: ", B )
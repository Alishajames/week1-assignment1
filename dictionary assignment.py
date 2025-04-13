#Check if a value exists in a dictionary

new_dict={"name":"alisha","age":25,"all good":True}

print("Your dict is :",new_dict)
value=input("enter value to check is in dict or not: ")
if value in new_dict:
    print("Your value is found")
else:
    print("Your value is not found")


#Get the key of a minimum value from the following dictionary
dict={"chem":70,"math":90,"Urdu":50}
min_key=min(dict,key=dict.get)

print("Key found with minimum value: ",min_key)


#Delete a list of keys from a dictionary
remove_key=["math"]

for key in remove_key:
    if key in dict:
        del dict[key]

print(dict)
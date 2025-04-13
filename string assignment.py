#Write a program to create a new string made of an input string’s first,middle, and last character.
# Take input from the user
input_string = input("Enter a string: ")

# Check if the string is empty
if len(input_string) == 0:
    print("The input string is empty.")
else:
    # Get the first character (always the first character)
    first_char = input_string[0]

    # Get the last character (always the last character)
    last_char = input_string[-1]
    
    # Get the middle character:
    # If the string length is odd, we take the exact middle character
    # If the string length is even, we take the character just before the exact middle
    if len(input_string) % 2 != 0:
        middle_char = input_string[len(input_string) // 2]
    else:
        middle_char = input_string[(len(input_string) // 2) - 1]

    # Create and print the new string made up of the first, middle, and last characters
    new_string = first_char + middle_char + last_char
    print(f"New string: {new_string}")


#Write a program to count occurrences of all characters within a string Given.

count_char={}

for char in input_string:
    if char in count_char:
        count_char[char]=count_char[char]+1
    else:
        count_char[char]=1

for char, count in count_char.items():
    print(char, count)


# Reverse a given string
reverse=input_string[::-1]
print("Reverse a given string: "+ reverse)

# Split a string on hyphens

split_string=input_string.split('-')

output_string='-'.join(input_string)

print(split_string,output_string)

#Q:Remove special symbols / punctuation from a string


# Initialize an empty string to store the cleaned result
cleaned_string = ""

# Loop through each character in the input string
for char in input_string:
    # If the character is alphanumeric (letters or digits) or a space, add it to the result
    if char.isalnum() or char == ' ':
        cleaned_string += char

# Print the result
print("Cleaned string:", cleaned_string)


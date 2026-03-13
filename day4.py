# for i in range(1,5):
#     if i == 3:
#         break #break statement is used to exit the loop when the condition is true
# print(i)
#-------------------------------------------------------------------------------------------------------------------------------------
# for i in range(1,5):
#     if i == 3:
#         continue #continue statement is used to skip the current iteration when the condition is true and move to the next iteration
# print(i)
#--------------------------------------------------------------------------------------------------------------------------------------
# pairs = [(1, 5), (2, 4), (4, 2), (5, 1)] #list of tuples
# for x, y in pairs: #unpacking the pairs in the list of tuples and assigning the values to x and y
#     print(f"{x}  {y}") #unpacking the pairs and printing them in the format x y
#--------------------------------------------------------------------------------------------------------------------------------------
# pairs = [(1, 5,2), (2, 4,3), (4, 2,3), (5, 1,2)]
# for x, y, z in pairs:
#     print(f"{x}  {y}  {z}") #unpacking the pairs and printing them in the format x y z
#--------------------------------------------------------------------------------------------------------------------------------------
# i = 1
# while i <= 5:
#     print(i)
#     i+=1 #i=i+1 is used to increment the value of i by 1 in each iteration of the loop\
#--------------------------------------------------------------------------------------------------------------------------------------
# username = ""
# password = ""
# while username != "Admin" or password != "hello":
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username == "Admin" and password == "hello":
#         print("Login successful")
#     else:
#         print("Invalid username or password")
#--------------------------------------------------------------------------------------------------------------------------------------
# n=int(input("Enter a number:"))
# sum =0
# i=1
# while i <= n:
#     sum = sum + i
#     i+=1
# print("Sum of first", n, "natural numbers is:", sum)
#--------------------------------------------------------------------------------------------------------------------------------------
# word = "janhavi"
# result = ""
# for char in word:
#     if char not in result:
#         result += char
# print(result)
#--------------------------------------------------------------------------------------------------------------------------------------
# word = "janhavi"
# reversed_word = ""
# for char in word:
#     reversed_word = char + reversed_word  # prepend each character
# print(reversed_word)
#--------------------------------------------------------------------------------------------------------------------------------------
# mycart = [10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400:
#      print("this is my purchased cart item")
#      continue
#     print(i)
#--------------------------------------------------------------------------------------------------------------------------------------
# word = "Racecar"
# # Convert to lowercase for case-insensitive comparison
# word_lower = word.lower() #lower() method is used to convert the string to lowercase so that we can compare it with the reversed string without worrying about the case of the characters
# reversed_word = "" 
# i = 0
# while i < len(word_lower):#len() function is used to get the length of the string and we are using it to iterate through each character in the string
#     reversed_word = word_lower[i] + reversed_word #we are prepending each character to the reversed_word string to reverse the string
#     i += 1
# if word_lower == reversed_word: #we are comparing the original string in lowercase with the reversed string to check if they are the same
#     print(f"'{word}' is a palindrome")
# else:
#     print(f"'{word}' is not a palindrome")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# word = input("Enter your name: ")
# # Convert to lowercase for case-insensitive comparison
# word_lower = word.lower() #lower() method is used to convert the string to lowercase so that we can compare it with the reversed string without worrying about the case of the characters
# reversed_word = "" 
# i = 0
# while i < len(word_lower):#len() function is used to get the length of the string and we are using it to iterate through each character in the string
#     reversed_word = word_lower[i] + reversed_word #we are prepending each character to the reversed_word string to reverse the string
#     i += 1
# if word_lower == reversed_word: #we are comparing the original string in lowercase with the reversed string to check if they are the same
#     print(f"'{word}' is a palindrome")
# else:
#     print(f"'{word}' is not a palindrome")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Input two strings
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# # Convert to lowercase and remove spaces
# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()
# # Check if lengths are same
# if len(str1) != len(str2):
#     print("Not an anagram")
# else:
#     # Count characters in str1
#     char_count1 = {}
#     for char in str1:
#         if char in char_count1:
#             char_count1[char] += 1
#         else:
#             char_count1[char] = 1
#     # Count characters in str2
#     char_count2 = {}
#     for char in str2:
#         if char in char_count2:
#             char_count2[char] += 1
#         else:
#             char_count2[char] = 1
#     # Compare both dictionaries
#     if char_count1 == char_count2:
#         print("The strings are anagrams")
#     else:
#         print("The strings are not anagrams")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Initialize empty dictionary
# my_dict = {}
# # Number of key-value pairs to add
# n = int(input("How many key-value pairs do you want to add? "))
# # Loop to take input and add to dictionary
# for i in range(n):
#     key = input(f"Enter key {i+1}: ")
#     value = input(f"Enter value for '{key}': ")
#     my_dict[key] = value  # Add key-value pair to dictionary
# # Display the dictionary
# print("Dictionary:", my_dict)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Initialize empty dictionary
# my_dict = {}
# # Number of key-value pairs to add
# n = int(input("How many key-value pairs do you want to add? "))
# # Loop to take input and add to dictionary
# for i in range(n):
#     key = input(f"Enter key {i+1}: ")
#     value = input(f"Enter value for '{key}': ")
#     my_dict[key] = value  # Add key-value pair to dictionary
# # Display the dictionary
# print("Dictionary before removal:", my_dict)
# # Remove a key (if it exists)
# remove_key = input("Enter the key you want to remove: ")
# if remove_key in my_dict:
#     del my_dict[remove_key]
#     print(f"Key '{remove_key}' removed successfully.")
# else:
#     print(f"Key '{remove_key}' not found in the dictionary.")
# # Display the updated dictionary
# print("Dictionary after removal:", my_dict)
#--------------------------------------------------------------------------------------------
# # Initialize empty dictionary
# my_dict = {}
# # Number of key-value pairs to add
# n = int(input("How many key-value pairs do you want to add? "))
# # Loop to take input and add to dictionary
# for i in range(n):
#     key = input(f"Enter key {i+1}: ")
#     value = input(f"Enter value for '{key}': ")
#     my_dict[key] = value  # Add key-value pair to dictionary
# # Display the dictionary
# print("Dictionary:", my_dict)
# # Check if a key exists
# check_key = input("Enter the key you want to check: ")
# if check_key in my_dict:
#     print(f"Key '{check_key}' exists with value: {my_dict[check_key]}")
# else:
#     print(f"Key '{check_key}' does not exist in the dictionary.")
#--------------------------------------------------------------------------------------------
# for i in range(1,4): #outer loop for rows
#     for j in range(1,4): #inner loop for columns
#         print("i" , end = " ")
#     print() #print a new line after each row
#--------------------------------------------------------------------------------------------
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1): #outer loop for rows
#     for j in range(1, n + 1): #inner loop for columns
#         print(chr(64+i), end=" ") #chr() function is used to convert the ASCII value to character and we are using it to print the characters in the pattern
#     print() #print a new line after each row
#--------------------------------------------------------------------------------------------
# n = int(input("Enter the number of rows: "))
# for i in range(1, n + 1): #outer loop for rows
#     for j in range(1, n + 1): #inner loop for columns
#         print(n+1-i, end=" ") #print the number in the pattern
#     print() #print a new line after each row
#--------------------------------------------------------------------------------------------
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1): #outer loop for rows
    for j in range(1, n +2- i): #inner loop for columns
        print("*", end=" ") #print the star in the pattern and we are using n+2-i to print the decreasing number of stars in each row
    print() #print a new line after each row
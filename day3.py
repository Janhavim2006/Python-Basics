# # Accept marks of 3 papers
# m1 = int(input("Enter marks of Paper 1: "))
# m2 = int(input("Enter marks of Paper 2: "))
# m3 = int(input("Enter marks of Paper 3: "))

# # Nested if-else to find maximum
# if m1 > m2:
#     if m1 > m3:
#         print("Maximum marks =", m1)
#     else:
#         print("Maximum marks =", m3)
# else:
#     if m2 > m3:
#         print("Maximum marks =", m2)
#     else:
#         print("Maximum marks =", m3)
#--------------------------------------------------
# # Accept marks of 3 papers
# m1 = int(input("Enter marks of Paper 1: "))
# m2 = int(input("Enter marks of Paper 2: "))
# m3 = int(input("Enter marks of Paper 3: "))

# # Nested if-else to find maximum
# if m1 < m2:
#     if m1 < m3:
#         print("Maximum marks =", m1)
#     else:
#         print("Maximum marks =", m3)
# else:
#     if m2 <m3:
#         print("Maximum marks =", m2)
#     else:
#         print("Maximum marks =", m3)
#---------------------------------------------------
# p = float(input("Enter percentage: "))

# if p > 90:
#     print("Grade A")
# elif p >= 80:
#     print("Grade B")
# elif p >= 70:
#     print("Grade C")
# elif p >= 60:
#     print("Grade D")
# elif p >= 50:
#     print("Grade E")
# else:
#     print("Grade F")
#---------------------------------------------------
# mydict = {"name": "Aditi", "age": 20, "city": "Nagpur"}
# print(mydict["name"])
# print(type(mydict))
#--------------------------------------------------------
# mydict ={
#     101: "Janhavi",
#     102: "Aditi",
#     103: "Kanak",
#     104: "Kohana",
#     101: "Shrushti", #updates values stored in 101 and replaces it with new value
#     104:"Mariyam",
# }
# print(mydict)
# a = mydict[102]
# print(a)
# mydict[104] = "Janhavi" #adds new key value pair in dict
# print(mydict)
#----------------------------------------------------------
# for x in mydict:
#     print(x) #prints keys of dict
#----------------------------------------------------------
# for x in mydict.values():
#       print(x) #prints values of dict
#----------------------------------------------------------
# for x,y in mydict.items():
#     print(x,y) #prints key and value of dict
#---------------------------------------------------------
# mydict["Mobile no."] = "1234567890"
# print(mydict)
#----------------------------------------------------------
# mydict.pop(101) #removes key 101 and its value from dict
# print(mydict)
#-----------------------------------------------------------------------------
# name = input("Enter your name: ")
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5]) #prints characters from index 0 to 4 (5-1)
# print(name[1:]) #prints characters from index 1 to end of string
# print(name[1:5]) #prints characters from index 1 to 4 (5-1)
# print(name[1:8:2]) #prints characters from index 1 to 7 with a step of 2 (1,3,5,7)
# print(name[:]) #prints the whole string
# print(name[::-1]) #prints the string in reverse order
#----------------------------------------------------------------------------------
# s = "help4code is a best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))
#----------------------------------------------------------------------------------
# s = "Janhavi","Aditi","Kanak","Kohana","Shrushti","Mariyam"
# m ='|'.join(s) #joins the elements of tuple s with '|' as a separator and returns a string
# print(m)
#--------------------------------------------------------------------------------------------
# s = "Python is a high-level programming language."
# print(s.lower()) #converts all characters in string to lowercase
# print(s.upper()) #converts all characters in string to uppercase
# print(s.swapcase()) #converts uppercase characters to lowercase and lowercase characters to uppercase
# print(s.title()) #converts the first character of each word to uppercase and the rest to lowercase
# print(s.capitalize()) #converts the first character of the string to uppercase and the rest to lowercase
#----------------------------------------------------------------------------------------------------------
# print("Subject Marks:")
# phy = 50
# chem = 60
# math = 70
# print("physics ={} chemistry ={} math ={}".format(phy,chem,math)) #format method is used to format the string and insert the values of variables in the string
# print("physics = {0} chemistry = {1} math = {2}".format(phy,chem,math)) #format method with positional arguments
# print("physics = {p} chemistry = {c} math = {m}".format(p=phy,c=chem,m=math)) #format method with keyword arguments
# total = phy + chem + math
# print("Total marks =", total)
# print("Roll no=" "36" .zfill(4)) #zfill method is used to pad the string with zeros on the left until it reaches the specified width (4 in this case)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# print('janhavimolkar777'.isalnum())
# print('janhavimolkar777'.isalpha())
# print('janhavimolkar777'.isdecimal())
# print('777f'.isdigit())
# print('Hello22'.isnumeric())
# print('Hello'.isidentifier())
# print('sdsdsdsd'.islower())
# print('sdsdsdsd'.isupper())
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d) #order of precedence is () > * > / > + > -
# print((a-b)*c/d) #order of precedence is * > / > + > -
# print(a+(b*c)/d) #order of precedence is * > / > + > +
#-------------------------------------------------------------------------------------------------------------------
# x =['a','b','c','d']
# y =['a','b','c','d']
# z =[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x != z)
#----------------------------------------------------------------------------------------------------
# name ='Janhavi'
# for i in name:
#     print(i) #i=0,1,2,3,4,5,6
#----------------------------------------------------------------------------------------------------
# name = "janhavi"
# vowels = 0
# consonants = 0
# for ch in name:
#     if ch in "aeiouAEIOU":
#         vowels += 1
#     else:
#         consonants += 1
# print("Vowels =", vowels)
# print("Consonants =", consonants)
#-----------------------------------------------------------------------------------------------
# name = "janhavi"
# result = ""
# for ch in name:
#     if ch not in result:
#         result = result + ch
# print("After removing duplicates:", result)
#-----------------------------------------------------------------------------------------------
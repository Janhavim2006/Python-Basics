# mylist = ["Janhavi","Aditi","Kanak",48,"Kohana",28.88,"Janhavi"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[2:])
# print(mylist[:5])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])
#-----------------------------------------------------------------
# mylist = ["Janhavi","Aditi","Kanak",48,"Kohana",28.88,"Janhavi"]
# mylist.append("Yash")
# mylist.append("Shrushti")
# print(mylist)
#------------------------------------------------------------------
# mylist = ["Janhavi","Aditi","Kanak",48,"Kohana",28.88,"Janhavi"]
# mylist.insert(4,"Yash")
# print(mylist)
#------------------------------------------------------------------
# mylist = ["Janhavi","Aditi","Kanak",48,"Kohana",28.88,"Janhavi"]
# mylist.remove(28.88)
# print(mylist)
#-------------------------------------------------------------------
# mylist = ["Janhavi","Aditi","Kanak",48,"Kohana",28.88,"Janhavi"]
# newlist = mylist.copy() #cloning the list
# print(newlist)
# print(mylist)
#-------------------------------------------------------------------
# mylist = [["Janhavi","Molkar"],["96.84"],["Aditi","Mishra"],["89.98"]]
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])
#-------------------------------------------------------------------------
# mylist1 = ["Janhavi","Molkar"]
# print(mylist1*2)
#-------------------------------------------------------------------------
# list2 = [48,28.88,56,"Janhavi"]
# del list2[2]
# print(list2)
#-------------------------------------------------------------------------
# list2 = [48,28.88,56,"Janhavi"]
# list2.clear()
# print(list2)
#-------------------------------------------------------------------------
# name = "Janhavi"
# print(name)
# print(type(name))
# myname = list(name) #typecasting 
# print(myname)
#-------------------------------------------------------------------------
#make sure the list should contain homogenous data for sorting
# mylist =[56,31,34,48,26,47]
# mylist.sort() #sorts the list in ascending order
# print(mylist)
#-------------------------------------------------------------------------
# mylist =[56,31,34,48,26,47]
# mylist.sort(reverse = True) #sorts the list in descending order
# print(mylist)
#-------------------------------------------------------------------------
# math = 10
# print(id(math)) id function returns the address of the variable math
#-------------------------------------------------------------------------
# math = 50
# physics = 50
# print(id(math))
# print(id(physics)) #both math and physics are pointing to the same address as they have the same value 
#--------------------------------------------------------------------------------------------------------
#Aliasing: when two or more variables are pointing to the same address in the memory then it is called aliasing
# mylist =[22,44,66,88,0,65,56]
# newlist = mylist
# print(id(mylist))
# print(id(newlist)) #both mylist and newlist are pointing to the same address as they are referring to the same list in the memory
#-----------------------------------------------------------------------------------------------------------------------------------
#Looping
# 1. for loop
#(a)membership operator: in and not in
# name = "Janhavi"
# print("a" in name) #true
# print("a" not in name) #false
#--------------------------------------
# for i in range(1,10,3): ascending order
#  print(i) 
#------------------------------------------------------------------------------------------------------------------------------------
# for i in range(5,0,-1): desending order
#  print(i)
#------------------------------------------------------------------------------------------------------------------------------------
# for i in range(1,11): table of 2
#     print(i*2)
#------------------------------------------------------------------------------------------------------------------------------------
# for i in range(1, 11):      # multiplier (1 to 10)
#     for j in range(2, 11):  # tables (2 to 10)
#         print(i * j, end="\t")
#     print()
#------------------------------------------------------------------------------------------------------------------------------------
# # Tables from 2 to 10
# for i in range(1, 11):
#     for j in range(2, 11):
#         print(i*j, end="\t")
#     print()
# print("--------------------------------------------------------")
# # Tables from 11 to 20
# for i in range(1, 11):
#     for j in range(11, 21):
#         print(i*j, end="\t")
#     print()
#------------------------------------------------------------------------------------------------------------------------------------
# WAP to check if a no.is positive negative or zero
# n= int(input("Enter a number:"))
# if(n>0):
#     print("Positive no.")
# if(n<0):
#     print("Negative no.")
# if(n==0):
#     print("Zero")
#------------------------------------------------------------------------------------------------------------------------------------
#WAP to check if the days are weekdays or weekends
# day = input("Enter the day: ")
# if day.lower() == "saturday" or day.lower() == "sunday":
#     print("Weekend")
# else:
#     print("Working Day")
#------------------------------------------------------------------------------------------------------------------------------------
##WAP to accept three paper marks and calculate total,percentage and if percentage is greater then equal to 60 then he/she is eligible for placement
# m1 = int(input("Enter marks of Paper 1: "))
# m2 = int(input("Enter marks of Paper 2: "))
# m3 = int(input("Enter marks of Paper 3: "))
# total = m1 + m2 + m3
# percentage = total / 3
# print("Total Marks =", total)
# print("Percentage =", percentage)
# if percentage >= 60:
#     print("Eligible for Placement")
# else:
#     print("Not Eligible for Placement")
#----------------------------------------------------------------------------------------
## WAP TO ACCEPT 5 DIFFERNT VALUE IN 5 DIFFERENT VAR AND CHECK MAX VALUE AND PRINT BY USING SIMPLE IF STATEMENT
# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))
# c = int(input("Enter third value: "))
# d = int(input("Enter fourth value: "))
# e = int(input("Enter fifth value: "))
# max = a
# if b > max:
#     max = b
# if c > max:
#     max = c
# if d > max:
#     max = d
# if e > max:
#     max = e
# print("Maximum value is:", max)
#----------------------------------------------------------------------------------------
#2nd Approach to find max value using nested if statement
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
d = int(input("Enter fourth value: "))
e = int(input("Enter fifth value: "))

if a>b and a>c and a>d and a>e:
    print("Maximum value is:", a)

if b>a and b>c and b>d and b>e:
    print("Maximum value is:", b)

if c>a and c>b and c>d and c>e:
    print("Maximum value is:", c)

if d>a and d>b and d>c and d>e:
    print("Maximum value is:", d)
    
if e>a and e>b and e>c and e>d:
    print("Maximum value is:", e)
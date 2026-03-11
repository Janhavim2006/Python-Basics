# math = 40
# pi = 3.14
# name = 'Janhavi'
# print(type(name))
# print(type(pi))
# print(type(math))
#----------------------------------------
# print(2+2)
# print("2"+"2")
# val1 = int(input("enter 1st value"))
# val2= int(input("enter 2nd value"))
# print(val1+val2)
#----------------------------------------
# print(int(3.14)) #int value 3
# print(int(10+5))#adds 2 int values and gives the result
# print(int(True)) #true=1
# print(int(False)) #false=0
#----------------------------------------
# print(float(3)) 
# print(float(50+2))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("4"))
#----------------------------------------
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# print(complex(5,-3))
# print(complex(True,False))
#---------------------------------------------------------------------------------------
#whenever we write 0 or add zero in integer float or any other form it will return false
# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2))
# print(bool(0+0))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
#---------------------------------------------------------------------------------------
#WAP to find simple intrest
# p =(float(input("Enter principal:")))
# r=(float(input("Enter rate:")))
# t=(float(input("Enter Time:")))
# S = p*r*t/100
# print("Simple intrest is:",S)
#---------------------------------------------------------------------------------------
#WAP to convert celcius to farheneit
# c = (float(input("Enter tempreture in centigrade:")))
# f = (c+9/5)+32
# print("Tempreture in Farheneit:", f)
#----------------------------------------------------------------------------------------
#WAP to swap 2 nos. using temp. variable
# a = 4
# b = 6
# temp = a 
# a=b
# b = temp
# print("value of a:",a)
# print("value of b:",b)
#-----------------------------------------------------------------------------------------
#WAP to swap 2 nos. without using temp. variable
# a = 100 
# b = 200
# a =a+b
# b = a-b
# a = a-b
# print("value of a:",a)
# print("value of b:",b)
#------------------------------------------------------------------------------------------
# h = 5
# inch = h*12
# cm = inch*2.54
# print("the height in inch:",inch)
# print("the height in cm:",cm)
#-----------------------------------------------------------------------------------------
#WAP to reverse the no.
# num = 123
# a = num%10 #ans is 3
# print (a)
# num = num // 10 #num = 12
# b = num%10 #b =2
# c = num // 10
# rev = a*100 +b*10 +c*1
# print(rev)
#----------------------------------------------------------------------------------------
num = 1234567
rev =0
while num !=0:
    digit = num%10
    rev = rev*10+digit
    num = num // 10
print("Reversed no.:",rev)
#-----------------------------------------------------------------------------------------
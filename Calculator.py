#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     29-12-2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("*****CALCULATOR*****")
print("In this calculator we can do +,-,*,/,% only so enter your opertor accordingly")
operator=input(print("Which operation do you want to do = "))
a=input(print("Enter your first value = "))
b=input(print("Enter your secound value = "))
if operator=='+':
    print(int(a)+int(b))
elif operator=='-':
    print(int(a)-int(b))
elif operator=='*':
    print(int(a)*int(b))
elif operator=='/':
    print(int(a)/int(b))
elif operator=='%':
    print(int(a)%int(b))
else:
    print("Sorry you entered invalid operator.. ! ")
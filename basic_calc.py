def add(num1,num2):
    return num1+num2
def subs(num1,num2):
    return num1-num2
def mutli(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

select=int(input("select operation from 1,2,3,4:"))
number_1=int(input("enter a value"))
number_2=int(input("enter a value"))

if select==1:
    print("number_1,"+",number_2","=",add(number_1,number_2))
if select==2:
    print("number_1,"-",number_2","=",subs(number_1,number_2))
if select==3:
    print("number_1,"*",number_2","=",multi(number_1,number_2))
if select==4:
    print("number_1,"/",number_2","=",div(number_1,number_2))
else:
    print("invalid input")
    
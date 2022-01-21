#Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5] 
# a=(1,2,3,4,5)
# if 5==a:
#     print("yes")
# else:
#     print("no")

# question2
# a=int(input("Marks of Maths:"))
# b=int(input("Marks of Science:"))
# c=int(input("Marks of English:"))
# d=int(input("Marks of Computer:"))
# Total_marks=(a+b+c+d)/4
# if Total_marks>100:
#     print("Envalid")
# elif Total_marks>=70:
#     print("Distinction")
# elif Total_marks>=60:
#     print("First")
# elif Total_marks>=40:
#     print("Pass")
# else:
#     print("Fail")

# question 3
# a=int(input("Enter the number"))
# if(a%2)==0:
#     print("{0} is a even number".format(a))
# else:
#     print("{0} is a odd number".format(a))

# # question4
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# c=int(input("Enter the third number:"))
# if a<=b and a<=c:
#     print("First number is the smallest")
# elif b<=a and b<=c:
#     print("Second number is the smallest")
# elif c<=a and c<=a:
#     print("Third number is the smallest")

# question 5
# a=int(input("Number:"))
# if a>=1:
#     print("True")
# elif a<=-1:
#     print("False")
# else:
#     print("Zero")

# question 6
# a=int(input("The given number's last number is "))
# last_digit= a%10
# print("The last digit in the given number %d = %d"%(a,last_digit))

# question 7
# a=float(input("Enter the number:"))
# print(a-int(a))

# question 8
number=int(input("NUmber:"))
total=0
while number>0:
    digits=number%10
    total=total+digits
    number=number//10
print("The sum of digits of the number enter is", total)




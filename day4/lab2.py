# write a Python program to reverse a string.
# def reverse(s):
#   str = ""
#   for i in s:
#     str = i + str
#   return str
# s = "Geeksforgeeks"
# print ("The original string  is : ",end="")
# print (s)
# print ("The reversed string(using loops) is : ",end="")
# print (reverse(s))


# Write a function called fizz_buzz that takes a number.
# def fizz_buzz(num):
#     num=int(input("eneter a number"))
#     if num%3==0:
#         return("fizz")
#     elif num%5==0:
#         return("buzz")
#     elif num%5==0 and num%3==0:
#         return fizz_buzz
# print(fizz_buzz)                


# If the number is divisible by 3, it should return “Fizz”.
p=int(input("eneter first number"))
q=int(input("enter second number"))
r=int(input("enter third number"))
def max():
    if p>q and p>r:
        maximum=p
    elif q>p and r>p:
        maximum=r
    print("largest number is:",maximum)
max()            




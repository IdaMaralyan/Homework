"""number"""
# number1 = int(input("Enter the number..."))
# number2 = int(input("Enter the number..."))
# for i in range(number1, (number2 * number1) + 1):
#     if i % number1 == 0 and i % number2 == 0:
#         print(i)
#         break


"""odd or even"""
# kent = 0
# zuyg = 0
# for i in range(1, 100):
#     if i % 2 == 0:
#         zuyg += 1
#     else:
#         kent += 1
# print(kent)
# print(zuyg)



"""fibonacci"""
# number = int(input("enter the number..."))
# n = 0
# n1 = 1
# while number <= 0:
#     number = int(input("mutqagreq drakan tiv..."))
#     continue
# while number == 1:
#     print(n)
#     print(number)
#     break
# else:
#     for i in range(number):
#         print(n)
#         result = n + n1
#         n = n1
#         n1 = result
    

"""letters and numbers"""




"""count"""
# number = int('73421')
# n1 = number // 10000
# n2 = (number // 1000) % 10
# n3 = (number // 100) % 10
# n4 = (number // 10) % 10
# n5 = number % 10
# print(n5 + n4 + n3 + n2 + n1)



'''factorial'''
# number = int(input("enter the number...>>>"))
# f = 1
# if number == 0 or number < 0:
#     while True:
#         if number == 0:
#             print(1)
#             break
#         elif number < 0:
#             number = int(input("enter non negative number...>>>"))
#             continue
# else:
#     while number > 0:  
#         f *= number
#         number -= 1
#     print(f"The factorial is {f}")



"""check"""

# age = int(input('enter your age...'))
# sex = input("enter your sex (F or M)")
# if age >= 18 and age <= 20 and sex == "M":
#     print("Your sex is Mail")
# else:
#     print("ERROR")
    




'''Write a Python program to create the multiplication table (from 1 to 10) of a number, by using input.'''
# number = int(input("enter the number...>>"))
# for i in range(1, 11):
#     print(number, "x", i, "=", i * number)


'''Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born.'''
# year = int(input("enter the year...>>>"))
# if (year - 2000) % 12 == 0:
#     sign = 'Dragon'
# elif (year - 2000) % 12 == 1:
#     sign = 'Snake'
# elif (year - 2000) % 12 == 2:
#     sign = 'Horse'
# elif (year - 2000) % 12 == 3:
#     sign = 'sheep'
# elif (year - 2000) % 12 == 4:
#     sign = 'Monkey'
# elif (year - 2000) % 12 == 5:
#     sign = 'Rooster'
# elif (year - 2000) % 12 == 6:
#     sign = 'Dog'
# elif (year - 2000) % 12 == 7:
#     sign = 'Pig'
# elif (year - 2000) % 12 == 8:
#     sign = 'Rat'
# elif (year - 2000) % 12 == 9:
#     sign = 'Ox'
# elif (year - 2000) % 12 == 10:
#     sign = 'Tiger'
# elif (year - 2000) % 12 == 11:
#     sign = 'Hare'
# print("Your Zodiac sign :", sign)        


"""Write a program to print absolute value of a number entered by user. E.g.-
INPUT: 2        OUTPUT: 2
INPUT: -2       OUTPUT: 2"""

# number = float(input("enter the number...>>>"))
# if number <= 0:
#     print(number * (- 1))
# else:
#     print(number * 1)


"""Write a program to print first 10 integers and their squares using while loop."""
# i = 1
# while i <= 9:
#     i += 1
#     print(i, " ", i ** 2)   


"""FizzBuzz is a well known programming assignment, asked during interviews.
The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
It takes an input n and outputs the numbers from 1 to n.
For each multiple of 3, print "Solo" instead of the number.
For each multiple of 5, prints "Learn" instead of the number.
For numbers which are multiples of both 3 and 5, output "SoloLearn"."""

# n = int(input())
# for x in range(n):
#     if x % 3 == 0:
#         print("Solo")
#     if x % 5 == 0:
#         print("Learn")   
#     elif x %3 and x % 5 == 0:
#         print('SoloLearn')
#     else:
#         print("ERROR")
        


'''գրել Python ծրագիր, որը կհաշվի 1-ից n թվերի թվաբանական միջինը։'''

'''գրել Python ծրագիր, որը կհաշվի աճող երկրաչափական պրոգրեսիայի (b1>0, q>1) n անդամների գումարը։'''


"""Write a program to find the sum of following series"""
"""1 + 4 + 9 + 16 + ... + n"""

 
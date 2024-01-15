# def Division(a,b):
#     if a % b == 0:
#         print ("a is divisible by b")
# Division(6,2)

# Creating a String
# with double Quotes
# String1 = "I'm a Geek"
# print("\nString with the use of Double Quotes: ")
# print(String1)
# print(type(String1))

# Creating a String
# with triple Quotes
# String1 = '''I'm a Geek and I live in a world of "Geeks"'''
# print("\nString with the use of Triple Quotes: ")
# print(String1)
# print(type(String1))

# Creating String with triple
# Quotes allows multiple lines

# String1 = '''Geeks
# For
# Life'''
# print("\nCreating a multiline String: ")
# print(String1)
# """Multiline
# Comment"""
# x=2
# y=7.5
# print (y//x)
# a = 5; b = 5
# print (a is b)
# a = float(input())
# print (type(a))
# s= "this is a string"
# print(s.find('a'))
# print(s.count("s"))
"""Conditional Statements"""
# marks= int(input('Enter your mark '))
# if marks >= 80:
# 	print ('Welcome to A0 batch')
# elif marks >= 60:
# 	print ('Welcome to A1 batch')
# elif marks >= 40:
# 	print ('Welcome to A2 batch')
# else: print ('Better luck next time, you are in A3')
# l=['biru', 'gugulu', 'riya', 'panda']
"""For Loop"""
# l1=[]
# for i in l:
#     print(i)
#     l1.append(i.upper())
# print(l1)
# l1=[1, 2, 3 , 4, 'biru', 'riya', 7, 8.23, 'panda']
# l_num=[]
# l_str=[]
# for i in l1:
#     if type(i) == int or type(i) == float:
#         l_num.append(i)
#     else : l_str.append(i)
# print(l_num, l_str)
# l={'panda', 'biru', 'riya', 'tilva'}
# for i in l:
#     print (i)
"""While Loop"""
# l=[1,2,3,4,5,6]
# i=0
# while i<len(l):
#     print (l[i])
#     i=i+1
# i=int(input("Enter your limit to sum "))
# sum=0
# a=1
# while a<=i:
#     sum=sum+a
#     a=a+1
# print (sum)
# i=int (input("Enter a no "))
# factorial=1
# while i>0:
#     factorial=factorial*i
#     i=i-1
# print (factorial)
# '''fibbonaci series (no of numbers)'''
# number=int(input("Enter the number of fibbonaci series no you want "))
# a,b = 0, 1
# i=0
# while i<number:
#     print(a)
#     c=a+b
#     i=i+1
#     a=b
#     b=c
# '''fibbonaci series upto that number'''
# number=int(input("Enter the number to print fibbonaci series "))
# a,b = 0, 1
# while a<=number:
#     print(a)
#     c=a+b
#     a=b
#     b=c
# yourString=input("enter a word to reverse ")
# reverse=''
# i=len(yourString)
# while i>0:
#     reverse= reverse + yourString[i-1]
#     i=i-1
# print (reverse)
# number=int(input("enter a number "))
# i=1
# while i<=10:
#     print (number , " x ", i, ' = ', number*i)
#     i=i+1
"""Comprehension and Function"""
# l=[1,2,3,4,5]
# print ([i for i in l if i%2 == 1])
# l=[1,2,3,4,5]
# print ([i**2 for i in l])
# l = ["biru", "riya", "panda"]
# print([i.upper() for i in l])
# d = {'k1':1, 'k2':2, 'k3':3, 'k4':4}
# print({k:v for k, v in d.items() if v>1})
"""Function"""
# def fun1():
#     print("function executed")
# fun1()
# def fun2():
#     return "executed"
# print('function ' + fun2())
# def fun3():
#     return 2,9,6,'panda'
# a,b,c,d = fun3()
# print (a, b, c, d)
# def fun4(a, b, c):
#     d = a + b/c
#     return d
# print (fun4(2, 3, 4))
# def fun5(a, b):
#     return a+b
# print(fun5((1,2,3), (3,4,5)))
# def fun6(a):
#     l = []
#     for i in a:
#         if type(i) == list:
#             for j in i:
#                 l.append(j)
#         else:
#             if type (i) == int or type(i) == float:
#                 l.append(i)
#     return l
# l = [4, 5, 7.5, 8, 'biru', [1,2,3], 'riya']
# print(fun6(l))
# def fun7(*args):
#     return args
# print(fun7(1,3,6,'biru',[1,2,3]))
# def fun8(*args, a):
#     return args, a
# print(fun8(1,2,3, a=5))
# def fun9(c,d,a=5,b=8):
#     return a, b, c, d
# print(fun9(1,2,a=8))
# def fun10(**kwargs):
#     return kwargs
# print(fun10(a=[1,2,3], b='biru', c={2,3,4}))
# users = ['panda', 'riya', 'biru', 'motu']
# looper = iter(users)
# while True:
#     try:
#         user = next (looper)
#         print (user)
#     except StopIteration:
#         break
# def testfib(n):
#     a,b = 0,1
#     for i in range(n):
#         yield a
#         a,b = b, a+b
# for i in testfib(10):
#     print (i)
# a = lambda x,y : x+y
# print (a(3,2))
# sq = lambda x: x**2
# print (sq(3))
# max = lambda x,y,z: x if x>y & x>z else y if y>z else z
# print(max(5,14,10))
# l=[1,2,3,4,5] 
# print (list(map(lambda x: x**2, l)))
# s = 'bapi'
# print (list (map(lambda x : x.upper(),s)))
# from functools import reduce
# l = [1,2,3,4,5]
# print (reduce(lambda x,y : x+y, l))
# print (reduce(lambda x,y: x if x>y else y, l))
# print (list(filter(lambda x: x%2 == 0, l)))
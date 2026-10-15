print("Jagadesh Varma")

if(5>2):
    print("True")
else:
    print("False")

a=8
print("a =",a)
a="High five"
print("a =",a)
# variables last which values asigned that one only it will consider

#operators
x=10
y=9

# arithmetic operators

# add two operand
print(x+y)
# subract right operand from the left
print(x-y)
# multiple operator
print(x*y)
# divide left operand by the right one
print(x/y)
# x,y -> operand , +-*/ -> operators

# assignment operator
x=5 
# x variable we asign 5 so this asignment operator
# prevously x have 5 now adding again x so 5+5 = 10
x+=5
print(x) 
# output 10
# now x value 10 if we divide we will get 10/5 = 2
x/=5
print(x)

# getting input from user
# inputString = input("Enter a sentence:")
# print("The inputed string is ",inputString)

# comments
# using # symbol for comment  single line cmnt
# multiline cmnt
"""This is multiline"""
# we can use single quotes or double quotes for multi line comment

# type conversion
# data type convert into another type
num_int = 123 #int type
num_flo = 1.23 #float type
num_new = num_flo+num_int
print("Value of num_new",num_new)
print("Type of num_new",type(num_new)) #float
# using type to know the data type

num_int = 123
num_str = "456"
# print(num_int+num_str) # it will throw unsupported type operand

# so for that we can use type conversion to solve the problem
num_int2 =int(num_str)
print(num_int+num_int2) # now output will come value is 579
# int is a python function

# numeric data types
print(type(5))
print(type(5.0))
c= 5+3j
print(type(c)) # it will give complex data type

# list
# one or more values we can store in variavle []
# empty list
my_list = []

# list of integer
my_list = [1,2,3,4]

# list with mixed data types
my_list=["Jaga",5,9.7,True]
print(my_list)

# acces the values from the list
language = ["French","Germany","English","Tamil"]
print(language)
# using index to acces the list
# acess first element
print(language[0])

print(language[2])

# changing value
language[2] = "Telugu"
print(language[2]) 

# tuples ()
# tuples we can change or modify the values in list we can modify
languages =("French","German","English","Polish")
print(languages)
print(languages[1])
print(languages[3])

# negative index it will comes from last
# -4,-3,-2,-1
# how to delete tuples using del keyword
del languages
# print(languages) # it will throw a error name languages is not defined


# string
# it's a letter
# single quote or double quotes we can use
my_string = "Hello"
print(my_string)
my_string = 'Hello'
print(my_string)
# we can use three double quotes or three single quotes for multi line string
my_string = """Hello,welcome to the
                world of python"""
print(my_string)
my_string = '''Hello'''
print(my_string)

str='jagacode'
print('str =',str)
# we can acces the string by same index numbering as list and tuples
print('str[0] =',str[0])
print('str[0] =',str[-1]) # last element negative index

# slice frts index,last index
# slice 1st to 3rd character
print('str[1:3] =',str[0:3])

# slicing 4th to 6th character
print('str[3,-1] =',str[4:-1])

# string concatination
str1 ="hello"
str2 ="world"
print(str1+str2) # it will print helloworld

# need three time same value we can use * operator
print(str1 * 4) # it will print hellohellohellohello


# sets
# set is a collection of unique values,it won't allow duplicate values
# using curly braces we can create a set
my_set = {1,2,3,4,5}
print(my_set)

# add value
my_set.add(6)
print(my_set)

# now i'm creating duplicates values to check whether it print or not
my_set2={1,2,3,4,5,4,3,2,1,2,3,2,1}
print(my_set2) # output will be {1,2,3,4,5}

# update value
my_set.update([9,7,8])
print(my_set) #output {1,2,3,4,5,6,7,8,9}

# remove value
my_set.remove(7)
print(my_set)

# used for
A ={1,2,3,}
B = {2,3,4,5}

print(A|B) # give combine value like union

print(A&B) # common value of both a and B {2,3} is present both it's intersection

print(A-B) # 1 If A set value not present in B that value will give example 2,3 already present in A and B 1 only not present so it's give 1

print(B-A) # now it's 4,5 bcs 1 doesn't have (),set difference

print(A ^ B) #symetric difference {1,4,5}

# Dictionary
# it has key value pairs
# empty dictinories
my_dict = {}

#dictionary with integer keys
my_dict = {1:"Apple",2:"ball"}

my_dict = {'name':"Jaga",1:[2,3,5]}

# how to acess the dictionaries values
person = {'name':"Jagadesh",'age':26}
# using key to acess
print(person['age'])

# changing age to 36
person['age'] =36
print(person)

# Adding salary key,value pair
person['salary'] = 33000
print(person)

# deleting age
del person['age']
print(person)

# deleting entire dictinaries
person1 = {'name':"Jagadesh",'age':26}

del person1

# range
# python function
print(range(1,10))
# what can we do with range
numbers = range(1,6)
# starting 1 finsihing 5 6 will be ignored
print(list(numbers))
print(tuple(numbers))
print(set(numbers))

print(dict.fromkeys(numbers,99))

# step
numbers1 = range(1,6,1)
# 1-> starting 6 -> finsih 1 -> step
print(list(numbers1)) # [1,2,3,4,5]  

numbers2 = range(1,6,2)
print(list(numbers2)) # if we give step value as 2 output [1,3,5]

# steps value negative
numbers3 = range(5,0,-1)
print(list(numbers3))

# if else conditions
if(5>6):
    print("Yes it's greater!")
else:
    print("It's to less buddy")

inputStr = input("Enter a number")
if(int(inputStr) > 80):
    print("Got A Grade")
elif(int(inputStr) > 65):
    print("Got B Grade")
else:
    print("Average")

num = -1
if(num>1):
    print("Positive number")
elif(num == 0):
    print("Zero")
else:
    print("Negative Number")
# here we are giving false so it won't print goes to outside print
if False:
    print("I'm inside of the Body")
    print("I'm also inside of teh body")
print("I'm outside of the body")


# while loop
n= 100
# +intialize sum and count
sum = 0
i=1
while i<=n:
    sum= sum+i
    i = i+1 # update counter
    print(sum)

# for loop
# no consition
numbers = [5,3,2,6,7,8,9]
sum =0
for val in numbers:
    sum = sum+val
    print("This is sum",sum)

# break
# stop the flow
for val in "string":
    if val == "r":
        break
    print(val)
print("The end")

# continue
# it will skip the current step
for val in "string":
    if val == "r":
        continue
    print(val)
print("This is the end")
# continue skip that particular statement

# functions
# function syntax
def print_lines():
    print("This is Line 1")
    print("This is Line 2")
print_lines()

# 
def add_numbers(a,b):
    sum = a+b
    print(sum)
add_numbers(4,5)  # no need to show but u have to store somewhere

def add_num(a,b):
    sum = a+b
    return sum
# function la irunthu value return panaa use return keyword
result = add_num(6,4)
print(result)

# factorial of number 6
6*5*4*3*2*1
# reccursive func factorial()

def calc_factorial(x):
    if x == 1:
        return 1
    else:
        return (x* calc_factorial(x-1)) #6-1,5-1,4-1,3-1,2-1,1-1 stop return 1 
num = 6
print("The factorial of",num,"is",calc_factorial(num))

# lambda function
# create small function,single line function that time it will be helpfull
square = lambda x:x**2
print(square(5)) 

# Modules
# python function and python files
# exampl.py
def add(a,b):
    return a+b
# add.py
# import example module
# import example
# acess the function
# inside the module use .
# example.add(4,5.5)

# default modules
# math module
import math
result = math.log2(5)
print(result)

# pi
from math import pi
print("The value of PI ",pi)

# open file in current directory
f=open("test.txt")

# specifying full path
f=open("c/;pygu/readme.txt")

# mode also we can send
# r -> file read
# w -> file write,if file not present cret new File
# x->the operation fails
# a->append the dat into exisitng File
# t->open in text Module
# b-> readin binary mode
# + -> file read and update

# equivalent to r or rt
f=open("test.txt")

# write in text mode
f=open("test.txt",'w')

# read and write in binary
f=open("img.bmp",'r+b')

# encode file
f=open("test.txt",encoding="utf-8")

# perform file operaiton close
f.close()

# write file
f =open("demo.txt","a")
f.write("Now thi file has more content")
f.close()

# read file
f=open("test.txt","r",encoding="utf-8")
f.read(4) #read thr first 4 data 4 charcter

# exception handling
# handle errors
import sys

randomList = ['a',0,2]
for entry in randomList:
  try:
    print("The entry is",entry)
    r=1/int(entry)
    break
  except:
    print("oops!",sys.exc_info([0],'occuured'))
    print("Next entry")
    print()
print("The recipocal of",entry,"is",r)

# directory operations
import os
os.getcwd() #present working directory
os.chdir('D:\\Hello') #changing current directory to D:\\Hello
os.listdir() #list all sub directories and files in that path
os.mkdir("test") #making a new directory test
os.rename('test','tasty') # renaming the directory test to tasty
os.remove("old.txt") #deleting old.txt file

# class and object
class MyClass():
    a=10
    def func(self):
        print("Hello")

# why class?
# acess thr clas
print(MyClass.a)
print(MyClass.func)
print(MyClass.__doc__)

# object
obj1 = MyClass()
print(obj1.a)
obj2 = MyClass()
print(obj1.a + 5)

# constructor
class ComplexNumber:
    def __init__(self,r=0,i=0):
        # self -> special keyword 
        self.real = r
        self.imag = i
    def getData(self):
        print("{0}+{1j}".fomat(self.real,self.imag))

    c1= ComplexNumber(2,3)
    c1.getData()

    # inheritance
class Mammal:
        def displayMammalFeatures(self):
            print("Mammal is a warm-blooded animal")
class Dog(Mammal):
        def displayDogFeatures(self):
            print("Dog has 4 legs")
d= Dog()
d.displayDogFeatures()
d.displayMammalFeatures()



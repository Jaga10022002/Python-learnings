# tuples
employees = ("Jaga","Yathi","Sunil")
print(employees)
print(type(employees))

# single element of tuple
a =(10,)
print(type(a)) # if we remove , it's a act as int

# unpacking the tuple
name,age,role = ("Jagadesh",24,"Python devloper")
print(name)
print(age)
print(role)

# advanced tuple unpacking
emp = ("Varma",26,"Backend Devloper")
name,age,role = emp
print(name)
print(age)
print(role)

# you can use also extended unpacking
numbers = (10,20,30,40,50,60)
first,*middle,last,lop = numbers
print(first)
print(middle)
print(last)
# Tuples are useful for fixed collections of values, such as coordinates or a function returning multiple result

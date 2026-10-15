# Part 2 — Conditional statements and loops
# 1. Conditional statements
# Conditions allow your program to make decisions based on data.
# For example, a backend application may need to determine whether a user is active, whether a payment succeeded, or whether a request contains valid information.

# if, elif, and else
age = 18

if(age >= 18):
  print("Eligible to vote")
elif(age >= 13):
  print("Teenager")
else:
  print("Child")

# Python uses indentation to define blocks. A colon begins the block, and the indented statements belong to it.

# example 1 simple if
temperature = 35
if(temperature > 30):
  print("It's to Hot today")

# example 2 if-else
number = 6
if number % 2 == 0:
 print("even number")
else:
  print("odd number")

# example 3 multiple condition
score = 85

if score >= 80:
  print("Got A Grade")
elif score >=65:
  print("Got B Grade")
elif score >= 50:
  print("Got C Grade")
else:
  print("Average")

# Logical operators
# Operator	Meaning	Example
# and	Both conditions must be true	age >= 18 and active
# or	At least one condition is true	role == "admin" or role == "manager"
# not	Reverses a truth value	not is_blocked

# and two condition must satisfied
age =25
has_id = True

if age >= 18 and has_id:
    print("Permitted")

# membership and identify
skills = ["Python","Angular"]

print("Python" in skills)
print("Angular" not in skills)

value = None
print(value is None)

# use in to test membership
# use None to check None 

# Truthy and falsy values
# Python treats certain values as false in conditions:
values = [0,"",[],{},None,False]

for value in values:
  if value:
    print("Truthy: ",value)
  else:
    print("Falsy: ",value)
# Empty strings, empty collections, zero, None, and False are falsy.


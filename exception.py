# exception handling
a=10
b=0
# print(a/b) # it will throw zero division error

# exception is not always a programming mistakes,if user gave invalid input that time it throw

# 3)basic try and except

try:
  # code might raise a error
  result = 10/0
except ZeroDivisionError:
  # handle that specific exception
  print("Unhandled cannot divide by zero")

# Execution proceeds into the matching except block rather than terminating with an unhandled ZeroDivisionError.

# example converting userinput
user_input = "ABC"
try:
  age=int(user_input)
  print("Age is ",age)
except ValueError:
  print("Please provide a integer value")

# hanling multiple exception
try:
  number = int("10")
  result = 100/number
  print("The Result is ",result)
except ValueError:
  print("Please provide a Valid Number")
except ZeroDivisionError:
  print("Cannot divide by Zero")

# Each except block handles a particular exception type. Python selects the first matching handler.

# one handler for multiple exception types
try:
  number = int("ABC")
except(ValueError,TypeError) as error:
  print("Invalid Input: ",error)
# Best practice: Catch the narrowest exception type you can reasonably handle. Avoid catching every exception indiscriminately.

# 4)Exception handling with else
# The else block runs only when the try block completes without raising an exception.

# else block when it execute means if try block completes without exception
try:
  number = int("25")
except ValueError:
  print("Please enter Valid Number")
else:
  print("The number is ",number)
# The else block runs only when the try block completes without raising an exception.

# If conversion fails, except executes and else is skipped.
# Why is else useful? It separates the code that might fail from the code that should run only after successful completion.

# A complete try/except/else example
def divide(a,b):
  try:
    result = a/b
  except ZeroDivisionError:
    print("Denominator can't  be Zero")
  except ValueError:
    print("Please Provide Integer value to divide")
  else:
    print("The Result is : ",result)

divide(100,10)
divide(100,0)
divide(25,5)

# This handles the expected division error and performs the success action only when division succeeds.

# 5)Finaly Block
# it will always executed,if it throw error or not also it's always run
# it commonly used for clean up

try:
  number = 10/2
  print(number)
except ZeroDivisionError:
  print("Value can't divide by zero")
finally:
  print("It always executed")

# Even if division fails, finally normally still executes.

# example file cleanup

file = None
try:
  file = open("sample.txt","r")
  content = file.read()
  print(content)

except FileNotFoundError:
  print("File Not Found")
finally:
  if file is not None:
    file.close()

# The file is closed whether reading succeeds or a handled file-related failure occurs.

# However, modern Python provides a cleaner option for files.

#The with statement uses a context manager to manage the resource and close the file automatically.
try:
  with open("sample.txt","r") as file:
    content = file.open()
    print(content)
except FileNotFoundError:
  print("Hey Jaga the searching file is not Found")

# 6)Raising Exception using raise
# sometime you need to reject the data dileberately.python's raise statements lets you trigger an exception

def withdraw(balance,amount):
  if balance <= 0:
    raise ValueError("Withdrawl amount must be possitive")
  if amount > balance:
    raise ValueError("Insufficient balance")
  return balance - amount

print(withdraw(1000,200)) #800
# Calling withdraw(1000, 1500) raises a ValueError with the message "Insufficient balance".
# print(withdraw(1000,1500))

# Important: Raising an exception and catching an exception are different operations.
# - raise signals that an operation failed.
# - except handles a matching exception.
# - If no matching handler exists, the exception propagates to the caller.

# re-raising a exception
# use a bare raise inside a exception hNDLER TO PROPAGTE
try:
  number = int("abc")
except ValueError:
  print("Please give a integer value")
  raise
# This logs a message and then allows the original ValueError to propagate.

# 7)User defined exceptions
# Built-in exceptions cover many situations, but backend applications often benefit from meaningful, domain-specific exceptions.
# For example, an employee application might need to distinguish an employee that doesn't exist from an invalid salary

class EmployeeNotFoundError(Exception):
  """ Employee is not Found in the company """

def getemployee(emp_id):
  employees= {101: "Jaga",102:"Bubba"}

  if emp_id not in employees:
    raise EmployeeNotFoundError(
      f"Employee {emp_id} is not found in this organization"
    )
  return employees[emp_id]

try:
  print(getemployee(999))
except EmployeeNotFoundError as error:
  print(error)


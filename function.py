# without using function

basic_salary = 33000
annual_salary = basic_salary * 12
print(annual_salary)

basic_salary = 40000
annual_salary = basic_salary * 12
print(annual_salary)

# with function
def cal_anual_salry(monthly_salary):
  return monthly_salary * 12
print("Annual_salary: ",cal_anual_salry(30000))
print("Annual_salary: ",cal_anual_salry(40000))

# The function accepts input, performs a calculation, and returns the result.

# 2)Function definition syntax and naming convention
def function_name(parameters):
  # function body
  return result

# def defines a function.
# function_name identifies the function.
# parameters receive input.
# The indented body contains the logic.
# return sends a result back to the caller.

# example
# f tells Python to evaluate expressions inside {}.

def greet(name):
  message =f"Hello, {name}!"
  return message
result = greet("Jagadesh")
print(result)

# Naming conventions
# Prefer descriptive names in snake_case.

def calculate_total_price():
  pass
def get_emp_details():
  pass
def get_validate_user_email():
  pass

# Avoid unclear names such as f1(), x(), or doit() unless there is a compelling reason.
# Python naming conventions generally recommend:

# Element	Convention	Example
# Function	snake_case	get_user()
# Parameter	snake_case	user_id
# Class	PascalCase	EmployeeService
# Constant	Uppercase	MAX_RETRIES

# 3 parameter vs Argument
# These two terms are related, but they are not the same.
# example
def add(a,b):
  return a+b
print(add(10,45))

# here a,b - >parameters
# 10,45 -> Arguments
# Think of parameters as input placeholders and arguments as the actual values supplied during the call.

# Positional arguments
# Python assigns arguments based on their position
def introduce(name,role):
  print(f"{name} is working on {role} role")
introduce("jaga","developer")

# Keyword arguments
# You can explicitly name the parameters.
introduce(name="Jagadesh",role="Developer")

# Both calls produce the same output.
# Keyword arguments are especially useful when functions have multiple parameters and readability matters.

# return values vs print()

def add(a,b):
  print(a+b)
def return_add(a,b):
  return a+b

result1 = add(10,20)
result2 = return_add(10,20)

print(result1) # none
print(result2) #30

# The first function prints 30, but it returns None because there is no explicit return statement.
# The second returns 30, which can be reused by another function, stored in a variable, or used in a calculation.

# Backend rule: Use return when the caller needs the result. Use print() mainly for demonstrations, debugging, or command-line output.
  
# Multiple return values
def calculate(a,b):
  return a+b,a-b,a*b,a/b

addition,subraction,multiplication,division = calculate(10,5)
print(addition)
print(subraction)
print(multiplication)
print(division)
# Python packages the returned values into a tuple, which can be unpacked by the caller.

# 5)Default argument values
# a default argument provides a value when the caller ommits the parameter

def greet(name,message="Need to Play Cricket"):
  print(f"This is {name} i have one message for you is that {message}")

greet("Bubba")
greet("Jaga","Need to play football")

# A parameter with a default value can be omitted when calling the function.
# Important rule: Parameter order
# Parameters without defaults should normally come before parameters with defaults.

# correct
def create_user(name,role="employee"):
  return {"name":name,"role":role}

# incorrect
# incorrect syntax
# def create_user(role="employee",name):
#   pass

# The mutable default argument trap
# This is a common Python interview and debugging question.
# Avoid this:
def add_skill(skill, skills=[]):
    skills.append(skill)
    return skills

print(add_skill("Python"))
print(add_skill("Django"))
print(add_skill("DRF")) #it will create each time new list

# so we can use None for stop occuring error
def add_skills(skill,skills=None):
    if skills is None:
         skills = []
    skills.append(skill)
    return skills
print(add_skills("Python"))
print(add_skills("Django"))

# This avoids accidentally sharing mutable state between calls.

# 6. Keyword arguments and argument unpacking
# Python supports flexible function calls through *args, **kwargs, and unpacking.
# *args: Variable positional arguments

def cal_total(*numbers):
  return sum(numbers)
print(cal_total(10,20))
print(cal_total(100,20,33,44,55,66))

# *numbers collects positional arguments into a tuple.

# **kwargs: Variable keyword arguments
def display_user(**details):
  for key,value in details.items():
    print(key,":",value)

display_user(name="Jagadesh",age=24,role="Developer")
# **details collects keyword arguments into a dictionary.

# unpacking list or tuple
def multiply(a,b,c,d):
  return a*b*c*d
numbers = [2,3,4,5]
print(multiply(*numbers))

# * -> the * unpack th =e list into individual positiona arguments

# unpacking dictiinaries
def crate_user(name,role):
  return {"name":name ,"role":role}
users = {"name":"Jaga","role":"Developer"}
print(crate_user(**users))

# The ** unpacks dictionary entries into keyword arguments matching the parameter names.

# 7)Docstring - documenting functiond

def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a percentage discount."""
    discount = price * discount_percent / 100
    return price - discount

# accesing to use
print(calculate_discount.__doc__)
help(calculate_discount)

# 8) Variable scopes : local scope and global scope
# local scopes bcs result is inside the calculate function
def calculate():
    result = 100
    print(result)

calculate()
# print(result)  # NameError outside the function

# global scope
company ="ABC Technologies"
def displaycompany():
  print(company)
displaycompany()

# 9)Lambda function
# A lambda is a small anonymous function containing a single expression.

square = lambda number: number ** 2
print(square(5))

# Lambda functions are especially useful as short callbacks or sorting keys.
employees = [
    {"name": "Ravi", "salary": 40000},
    {"name": "Priya", "salary": 60000},
    {"name": "Kumar", "salary": 35000}
]
employees.sort(key=lambda emp:emp['salary'])
print(employees)

# 10)Recursion
# recursion occurs when a function call  itself  to a smaller  version of problem

def factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number <= 1:
        return 1

    return number * factorial(number - 1)

print(factorial(5))  # 120

# Two essential parts:
# - Base case: Stops recursion.
# - Recursive case: Reduces the problem and calls the function again.
# Without a base case, recursion may continue until Python raises RecursionError.
# Recursion is useful for tree traversal and certain divide-and-conquer algorithms, but iterative solutions can be more suitable for simple repetitive tasks.
# dictionaries
# it has key value pairs 
# essentials for backend development
# you can see dictionaries frequently while working on Json data,
# Django views,API requests,and serialized response

employee = {
  "id":1,
  "empName":"Jagadesh Varma",
  "role":"Backend Developer"
}
print(employee)
print(type(employee)) # < class 'dict' >

# acessing the data from dictionaries
print(employee["role"]) # Backend Developer

# add a nes key
employee["department"] = "IT"
print(employee)

# updating a existing key
employee["role"]="Senior Developer"
print("Updated employee",employee)

# safely retrive the value
salary = employee.get("salary",33000)
print(salary)
# get(key,default)

# Advanced: Important dictionary methods
# Method	Purpose
# get(key, default)	Retrieve a value safely
# keys()	View the keys
# values()	View the values
# items()	Iterate over key-value pairs
# update()	Add or update multiple entries
# pop(key)	Remove a key and return its value
# setdefault()	Return an existing value or insert a default

# example
employee = {
  "id":2,
  "name":"Jagadesh varma",
  "skills":["Angular","Python"]
}

print(employee)

for key,value in employee.items():
  print(key,":",value)

# Dictionary comprehensions
square = {
  number:number ** 2
  for number in range(1,6)
}
print(square)

# practical example
users = [
    {"id": 1, "name": "Ravi"},
    {"id": 2, "name": "Priya"}
]

user_by_id = {user["id"]:user for user in users}
print(user_by_id[2])
# This converts a list of user records into a dictionary indexed by user ID.

# nested data structure
# Real backend data is rarely flat. You may receive a list of dictionaries, a dictionary containing lists, or several levels of nested objects.

employees = [
    {
        "id": 101,
        "name": "Ravi",
        "skills": ["Python", "Django"]
    },
    {
        "id": 102,
        "name": "Priya",
        "skills": ["Angular", "TypeScript"]
    }
]

print(employees)
print(employees[0]["name"])
print(employees[1]["skills"])

# This structure is common when processing API data.
# To retrieve all employee names:

for emp in employees:
  print(emp["name"])

# to retrive all skills
for emp in employees:
  print(emp["skills"])

# two for combining
for employee in employees:
    for skill in employee["skills"]:
        print(employee["name"], skill)
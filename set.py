# set
# it's a unique It is particularly useful for removing duplicates and performing membership checks and mathematical set operations.
# eclosed with curly brace
# it won't allow the duplicate values
# creating a set
score = {22,43,56,87,24,67}
print(score)
print(type(score))

skills = {"python","django","drf","python"}
print(skills) # it will remove duplicate values

# remove duplicates
num = {1,2,3,4,5,5,6,4,3,1,2}
print(num)

# membership checking
if "python" in skills:
  print("Python is presenting in the skills")

# add and remove
skills.add("Angular")
print(skills)
skills.discard("drf") #discard doesn't raise a error if the elemnet missing but remove() does
print(skills)

# advanced set operation
frontend = {"HTML","CSS","JavaScript"}
backend = {"JavaScript","Nodejs","Python"}

# intersection
print(frontend & backend) # & ->compare two and give common

# union 
print(frontend | backend) # | ->all unique elements

# difference
print(frontend - backend) # -> give the diffeerence

# Other useful operations include:
# - issubset() — checks whether one set is contained in another.
# - issuperset() — checks whether a set contains another set.
# - symmetric_difference() — returns elements present in either set, but not both.
# Backend use case: Finding unique tags, removing duplicate identifiers, or checking common permissions.
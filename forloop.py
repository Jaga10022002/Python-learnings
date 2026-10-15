# for loop
# A for loop iterates over the elements of an iterable, such as a list, tuple, string, dictionary, set, or range.

skills = ["Python","Django","DRF"]
for skill in skills:
  print(skill)

# range
for number in range(5):
  print(number) # output 0,1,2,3,4  then stop value executed

for number in range(1,5):
 print(number)

for number in range(1,6,2): #1->starting  6-> ending  2-> step
  print(number)

# The syntax is range(start, stop, step).

# example 1 sum of the numbers
total =0
for num in range(0,6):
  total+=num
print("The sum of total is",total)

# iterate over dictionaries
employee= {"id":1,"name":"Jaga","role":"Backend dev"}

for key,value in employee.items():
  print(key,":",value)

# count matching elements
numbers = [10,15,20,25,30]
count = 0

for num in numbers:
  if num % 2 == 0:
    count+=1
print(count)  # output:3
# Remember: The program doesn't count all five numbers. It counts only the numbers that satisfy the condition number % 2 == 0.

# enumerate() and zip()
# These are particularly useful when working with collections.

# enumerate
# enumerate() provides both the index and value.
names = ["Ravi", "Priya", "Kumar"]

for index,name in enumerate(names,start=1):
  print(index,name)

# zip
# zip() pairs corresponding elements. By default, iteration stops when the shortest iterable is exhausted.
names=["Jaga","Bubba"]
scores=[85,92]

for name,score in zip(names,scores):
  print(name,score)

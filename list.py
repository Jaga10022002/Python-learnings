# creating and acessing list
employees = ["Jagadesh","Sunil","Yathi","Sathish"]
print(employees)
# accesing element in the list
print(employees[2])
employees[2] = "Jethin"
# update the value
print(employees)
# append add the values in last of the list
employees.append("Rakki")
print(employees)

# insert we have to mention postion and value
employees.insert(1,"Bubba")
print(employees)
employees.sort()
print(employees)

# append vs extend
# append add one item
a=[1,2]
a.append([3,4])
print(a)

# extend
# add more item
a=[1,2]
a.extend([3,4])
print(a)

# slicing
# [start:end:step]

num = [10,20,30,40,50,60]
print(num[1:5])
print(num[:3])
print(num[:-1])
# first two skipped means last one is step 
print(num[::2])

# advanced list
numbers = [10, 20, 30, 40, 50]
print(numbers[-3:]) #-3 itself starting so 
print(numbers[::-1]) # this one is reverese order no skipping
print(numbers[::1])

print(numbers[::-2])
print(numbers[::2])

print(numbers[1:-1])

# here original array also changing we don;t need that
# this is deep copy
num = [10,20,30]
sftcpy = num
sftcpy.append(40)
print(sftcpy)
print(num)

# we don't nned to modify the original array so we are using copy method
num = [10,20,30]
# so using copy original array is not modifed this is call shallow coppy
sft = num.copy()
sft.append(40)
print(num)
print(sft)
numbers = [5, 10, 15, 25]

for num in numbers:
  if num == 20:
    print("Number Found")
    break
else:
    print("Not Found")




scores = {'Ravi': 80, 'Priya': 95, 'Kumar': 65}

for name,score in scores.items():
  if score >= 80:
    print(name)

# square
square = [n**2 for n in range(1,21) if n%2 != 0]
print(square)

# active user
users = [
    {'name': 'Ravi', 'active': True},
    {'name': 'Priya', 'active': False},
    {'name': 'Kumar', 'active': True},
    {'name': 'Anu', 'active': True}
]

count = 0

for user in users:
  if user['active']:
    print(user['name'])
    count+=1
print("Active user Count: ",count)
# break continue and pass
# These keywords control how your code executes.

# break — exit the loop

for n in range(0,5):
  if n== 3:
    break
  print("Break",n)

# continue skip the cuurent iteration
for n in range(0,6):
  if n == 3:
    continue
  print("Continue",n)

# pass — do nothing
# This is a placeholder for an implementation you will add later.
def process_payment():
   pass


numbers = [2, 4, 6, 8,]

for number in numbers:
    if number % 2 != 0:
        print("Odd number found")
        break
else:
    print("No odd numbers found")
# This is useful for search operations where you want to distinguish between finding an item and exhausting the search.
  
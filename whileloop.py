# while loop
# A while loop repeats as long as its condition is true.

count = 1
while count<=5:
  print(count)
  count+=1
# The most important concept is that the loop must make progress toward ending, unless you intentionally want it to run indefinitely.

# example sum of the digits number
number = 1234
total =0

while number > 0:
  digit = number % 10
  total += digit
  number //=10
print(total)

# 3rd example
attempt = 0
max_attempt =3
while attempt < max_attempt:
  attempt+=1
  print("Attempts: ",attempt)
# In backend applications, bounded retries may be useful for transient failures, but actual network retries should also have appropriate timeouts and error handling.

# for vs while
# for loop                                      	while loop
# Iterates over an iterable	                    Repeats while a condition is true
# Often used when processing collections	    Often used when repetition depends on a condition
# Automatically advances through the iterable	You must update relevant state yourself
# Commonly used for lists and dictionaries	    Commonly used for retry counters and condition-based logic
def gcd(a, b):
  # Base case: if b is 0, then the GCD is a
  if b == 0:
      return a
  # Recursive case: call gcd with b and the remainder of a divided by b
  else:
      return gcd(b, a % b)

# Take input from the user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate the GCD and print the result
result = gcd(a, b)
print(f"The GCD of {a} and {b} is: {result}")


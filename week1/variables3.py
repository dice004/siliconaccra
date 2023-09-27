# Asking for the input from the user for the calculation
x = input("what is x?:  ")
y = input("what is y?: ")

# Converting the user input to operatable objects
x = int(x)
y = int(y)

# Running the various types of operations on the user input
sum = x + y
print(f"the sum of {x} and {y} is {sum}")  

diff = x - y
print(f"the diff between {x} and {y} is {diff}")


mult = x * y
print(f"the product of multiplying {x} and {y} is {mult}")

div = x / y 
print(f"the quotient of dividing {x} by {y} is {div}")

rem = x % y
print(f"the remainder of {x} mod {y} is {rem}")


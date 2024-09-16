# Module 1: Critical Thinking Part 2
 # Get the inputs for num1 and num2
num1 = float(input("First number input: "))
num2 = float(input("Second number input: "))

# Finds the multiplication and division of the two numbers 
product = num1 * num2 
# Checker to avoid divison of 0
if num2 != 0:
    quotient = num1 / num2
else:
    print("Second input number cannot be 0")

# Shows the results
print("The multiplication of the two numbers entered are: ", product)
print("The division of the two numbers entered are: ", quotient)

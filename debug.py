# Python program with 2 errors
# Variable and fixed sum
var = 4
sumvalue = var + 4

# Function to do something with a value
def dosomething(valuetocheck):
    if valuetocheck > 4:
        print("Bad indent")  # Fixed indentation warning message

# Ask the user for a value and confirm the supplied value is greater than 0
def checkvalue(valuetocheck):
    assert (type(valuetocheck) is int), "You must enter a number."  # Fixed quotes
    assert (valuetocheck > 0), "Value entered must be greater than 0"
    
    if valuetocheck > 4:
        print("Value is greater than 4")

# Request input from the user and check value
var = int(input("Enter a number greater than 0: "))
checkvalue(var)


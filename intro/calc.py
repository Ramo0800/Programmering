def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y 
def multiplication(x, y):
    return x * y
def division(x, y):
    return x / y


print("Välj två nummer")
number1 = input()
number2 = input()
number1 = int(number1)
number2 = int(number2)
print("ska de adderas, subtraheras, multipliceras eller divideras?")
equation = input()
if equation == "adderas":
    print("det blir", addition(number1, number2))
elif equation == "subtraheras":
    print("det blir", subtraction(number1, number2))
elif equation == "multipliceras":
    print("det blir", multiplication(number1, number2))
elif equation == "divideras" and number1 or number2== "0":
    print("det blir 0")
else:
    print("det blir", division(number1, number2))


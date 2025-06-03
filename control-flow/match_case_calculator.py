#Simple Calculator with Match Case
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input ("Choose the operation (+, -, *, /): ")


def calculate(num1, num2, operation):
    match operation:
        case "+":
            return (num1+num2)
        case "-":
             return (num1-num2)
        case "*":
             return (num1*num2)
        case "/":
             return (num1/num2)

result = calculate(num1, num2, operation)
print(f'The result is:{result}')
        




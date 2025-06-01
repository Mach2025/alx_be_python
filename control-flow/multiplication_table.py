#Multiplication Table Generator
#prompt the user to enter a number
number= int(input(" Enter a number to see its multiplication table: "))

for i in range (1,10):
    product = number * i
    print (f"{number} * {i} = {product}")


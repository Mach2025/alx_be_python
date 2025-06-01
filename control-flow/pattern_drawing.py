# pattern_drawing.py
# Prompt user for the pattern size
size = int(input("Enter the size of the pattern:"))

row = 0

# Use while loop to iterate through each row
while row < size:
    for col in range(size):
        print("*", end="")  
    print()  # Move to next line after one row is printed
    row += 1

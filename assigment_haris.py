def check_conditions(a, b, c):
    if (a > b or b > c) and (a % 2 == 0 and c % 2 != 0) and (b != c): 
        print("Conditions met") 
    else: 
        print("Conditions not met")

def check_input_types(x, y, z): 
    if isinstance(x, str) and isinstance(y, int) and isinstance(z, float): 
        return "Valid input types" 
    return "Invalid input types"

def logical_operations(x, y): 
    x_bool = bool(x) 
    y_bool = bool(y)

    print(f"x AND y: {x_bool and y_bool}")
    print(f"x OR y: {x_bool or y_bool}")
    print(f"NOT x: {not x_bool}")
    print(f"x XOR y: {x_bool != y_bool}")

#Assignment 1: Complex Conditions

a = int(input("Enter value for a: ")) 
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
check_conditions(a, b, c)

#Assignment 2: Type Checking

x = input("Enter a string: ") 
y = int(input("Enter an integer: ")) 
z = float(input("Enter a float: "))
print(check_input_types(x, y, z))

#Assignment 3: Logical Operators

x = input("Enter value for x: ") 
y = input("Enter value for y: ")
logical_operations(x, y)
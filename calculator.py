a = int(input("Enter the number:"))
op = input("Operation (+, -, *, /): ")
b = float(input("Enter the second number:"))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
        if b == 0:
            print("Error: Division by zero")
        else:
            result = a / b
else:
    print("Unknown operation:")

print(f"(a) {op} (b) = {result}")
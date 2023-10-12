def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b!= 0:
        return a/ b
    else:
        return "Cannot divide by zero"

def calculator():
    print("----- Calculator -----")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter operation number (1-4): ")

    n1 = float(input("Enter n1: "))
    n2 = float(input("Enter n2: "))

    if choice == '1':
        result = add(n1, n2)
    elif choice == '2':
        result = sub(n1, n2)
    elif choice == '3':
        result = mul(n1, n2)
    elif choice == '4':
        result = div(n1, n2)
    else:
        result = "Invalid"

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()

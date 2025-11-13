print("Simple Calculator")
print("-" * 20)

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("\nChoose (1-5): ")
    
    match choice:
        case "1":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            print(f"Result: {a + b}")
        
        case "2":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            print(f"Result: {a - b}")
        
        case "3":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            print(f"Result: {a * b}")
        
        case "4":
            a = float(input("First number: "))
            b = float(input("Second number: "))
            if b != 0:
                print(f"Result: {a / b}")
            else:
                print("Cannot divide by zero!")
        
        case "5":
            print("Goodbye!")
            break
        
        case _:
            print("Invalid choice!")

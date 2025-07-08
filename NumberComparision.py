# NumberComparision.py

def compare_numbers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is smaller than {b}"
    else:
        return f"{a} is equal to {b}"

# Example usage
if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        result = compare_numbers(num1, num2)
        print(result)

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

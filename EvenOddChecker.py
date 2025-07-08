# EvenOddChecker.py

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def main():
    # Check a single number
    try:
        num = int(input("Enter a number to check if it's even or odd: "))
        result = check_even_odd(num)
        print(f"{num} is {result}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    # Check a list of numbers
    print("\nNow checking a list of numbers.")
    try:
        input_list = input("Enter numbers separated by spaces: ")
        numbers = [int(n) for n in input_list.split()]
        
        print("\nResults:")
        for n in numbers:
            print(f"{n} is {check_even_odd(n)}")
    except ValueError:
        print("Please enter valid integers only.")

if __name__ == "__main__":
    main()
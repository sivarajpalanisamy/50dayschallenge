# PersonalGreeting.py

def main():
    name = input("What is your name? ")
    age = input("How old are you? ")
    color = input("What is your favorite color? ")

    print("\n--- Personal Greeting ---")
    print(f"Hello, {name}! You're {age} years old and your favorite color is {color}.")
    print(f"Have a colorful day, {name}!")

if __name__ == "__main__":
    main()
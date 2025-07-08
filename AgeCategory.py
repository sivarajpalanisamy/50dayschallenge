# AgeGroupChecker.py

def determine_age_group(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

def main():
    try:
        age = int(input("Enter the age: "))
        group = determine_age_group(age)
        print(f"The person is a: {group}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

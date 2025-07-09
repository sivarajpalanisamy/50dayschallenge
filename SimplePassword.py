# SimplePassword.py

def check_password_strength(password, min_length=8):
    if len(password) >= min_length:
        return True
    else:
        return False

def main():
    print("=== Simple Password Strength Checker ===")
    password = input("Enter your password: ")

    if check_password_strength(password):
        print("✅ Password is strong enough.")
    else:
        print(f"❌ Password is too short. It must be at least {8} characters long.")

if __name__ == "__main__":
    main()

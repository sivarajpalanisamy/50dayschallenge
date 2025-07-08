# ShoppingBill.py

def calculate_total_with_tax(prices, tax_rate):
    subtotal = sum(prices)
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total

def main():
    print("Enter the prices of 3 items:")

    prices = []
    for i in range(1, 4):
        price = float(input(f"Price of item {i}: ₹"))
        prices.append(price)

    TAX_RATE = 0.18  # 18% tax

    subtotal, tax, total = calculate_total_with_tax(prices, TAX_RATE)

    print("\n------ Shopping Bill ------")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Tax (18%): ₹{tax:.2f}")
    print(f"Total Amount: ₹{total:.2f}")
    print("---------------------------")

if __name__ == "__main__":
    main()

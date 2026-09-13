# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0
portfolio = []

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        total_investment += investment
        portfolio.append((stock, quantity, price, investment))

        print("Investment added:", investment)

    except ValueError:
        print("Please enter a valid number.")

# Display portfolio
print("\n===== Portfolio Summary =====")

for stock, quantity, price, investment in portfolio:
    print(
        stock,
        "| Quantity:", quantity,
        "| Price:", price,
        "| Value:", investment
    )

print("\nTotal Investment Value:", total_investment)

# Optional: Save result to a text file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("=======================\n")

        for stock, quantity, price, investment in portfolio:
            file.write(
                f"{stock} | Quantity: {quantity} | "
                f"Price: {price} | Value: {investment}\n"
            )

        file.write(f"\nTotal Investment Value: {total_investment}")

    print("Portfolio saved successfully in portfolio.txt")
else:
    print("Portfolio was not saved.")
    
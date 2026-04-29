# Task 2: Stock Portfolio Tracker (Improved)

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

print("Available Stocks:")
for key in stocks:
    print(f"- {key} : {stocks[key]} per share")

print("\nType 'exit' to stop\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "EXIT":
        print("Program Ended")
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))
        total = stocks[stock] * quantity
        print("Total Investment:", total)

        with open("portfolio.txt", "a") as file:
            file.write(f"{stock} - {quantity} shares - Total: {total}\n")

    else:
        print("Invalid stock name! Please choose from list above.\n")
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

print("Welcome to Stock Portfolio Tracker!")
print("Available stocks and their prices:")
for s, p in stock_prices.items():
    print(s, "=", "$", p)

portfolio = {}
total_investment = 0

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found! Please choose from the list.")
        continue
    qty = int(input("Enter quantity of " + stock + ": "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

print("\nYour Portfolio Summary:")
for s, q in portfolio.items():
    value = q * stock_prices[s]
    print(s, ":", q, "shares × $", stock_prices[s], "=", "$", value)
    total_investment += value

print("\nTotal Investment Value = $", total_investment)

save = input("\nDo you want to save this in a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for s, q in portfolio.items():
            f.write(f"{s}: {q} shares × ${stock_prices[s]} = ${q * stock_prices[s]}\n")
        f.write(f"\nTotal Investment Value = ${total_investment}")
    print("Portfolio saved to 'portfolio.txt'!")

print("\nThank you for using this program!")
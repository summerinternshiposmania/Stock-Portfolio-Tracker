
# Stock Portfolio Tracker

portfolio = {}

n = int(input("How many stocks do you want to add? "))

for i in range(n):

    print("\nEnter details for stock", i + 1)

    name = input("Enter stock name: ")
    price = float(input("Enter stock price: "))
    quantity = int(input("Enter number of shares: "))

    investment = price * quantity

    portfolio[name] = investment

print("\n----- STOCK PORTFOLIO -----")

total = 0

for name, investment in portfolio.items():

    print(name, "=", investment)

    total = total + investment

print("---------------------------")
print("Total Investment =", total)

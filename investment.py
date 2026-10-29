# Version 2 - Calculate Investment Profit and Return

# Version 1: original investment
shares = 10
price_per_share = 150
total_cost = shares * price_per_share

# Version 2: new stock price
new_share_price = 175

# Current investment value
current_value = shares * new_share_price

# Profit or loss
profit = current_value - total_cost

# Percentage return
percent_return = (profit / total_cost) * 100

# Display the results
print("Stock: Apple")
print("Shares purchased:", shares)
print(f"Original price per share: ${price_per_share}")
print(f"Total investment cost: ${total_cost}")
print(f"New price per share: ${new_share_price}")
print(f"Current investment value: ${current_value}")
print(f"Profit/Loss: ${profit}")
print(f"Percentage return: {percent_return:.2f}%")
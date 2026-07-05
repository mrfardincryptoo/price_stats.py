import statistics

# Calculate Average Entry Price for a portfolio
prices = [120.5, 125.2, 118.8, 122.0]
avg_price = statistics.mean(prices)

print(f"Average Entry Price: {avg_price:.2f} USDT")

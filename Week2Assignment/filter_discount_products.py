# Given a list of product prices, filter out all products below $50
# and apply a 10% discount to the remaining products

prices = [30, 45, 60, 80, 25, 100, 55]

# Filter products priced $50 and above
filtered_prices = list(filter(lambda p: p >= 50, prices))

# Apply 10% discount
discounted_prices = list(map(lambda p: p * 0.9, filtered_prices))

print("Original prices:", prices)
print("Filtered prices (>= $50):", filtered_prices)
print("Discounted prices (10% off):", discounted_prices)

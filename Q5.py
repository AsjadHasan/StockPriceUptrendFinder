days = int(input("Number of days: "))

prices = []

for i in range(days):
    price = int(input("Closing price: "))
    prices.append(price)

longest = 1
current = 1
best_start = 0
current_start = 0

for i in range(1, days):
    if prices[i] > prices[i - 1]:
        current += 1
    else:
        current = 1
        current_start = i

    if current > longest:
        longest = current
        best_start = current_start

uptrend = prices[best_start:best_start + longest]

print(f"Longest uptrend: {longest} days ({', '.join(map(str, uptrend))})")
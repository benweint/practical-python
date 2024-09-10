# pcost.py
#
# Exercise 1.27

path = 'Data/portfolio.csv'
total_cost = 0

with open(path, "rt") as f:
	headers = next(f).strip().split(",")
	shares_idx = headers.index('shares')
	price_idx = headers.index('price')
	for line in f:
		cols = line.split(",")
		shares = int(cols[shares_idx])
		price = float(cols[price_idx])
		cost = price * shares
		total_cost += cost

print(f'Total cost {total_cost:.2f}')

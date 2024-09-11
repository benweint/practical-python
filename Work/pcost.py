# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
	total_cost = 0
	with open(filename, "rt") as f:
		headers = next(f).strip().split(",")
		shares_idx = headers.index('shares')
		price_idx = headers.index('price')
		for line in f:
			cols = line.split(",")
			try:
				shares = int(cols[shares_idx])
				price = float(cols[price_idx])
			except ValueError as e:
				print(f'Skipping line {line} due to error: {e}')
			cost = price * shares
			total_cost += cost
	return total_cost

total_cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost {total_cost:.2f}')


# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
	total_cost = 0
	with open(filename, "rt") as f:
		rows = csv.reader(f)
		headers = next(rows)
		shares_idx = headers.index('shares')
		price_idx = headers.index('price')
		for row in rows:
			try:
				shares = int(row[shares_idx])
				price = float(row[price_idx])
			except ValueError as e:
				print(f'Skipping row {row} due to error: {e}')
			cost = price * shares
			total_cost += cost
	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')


# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
	result = []
	with open(filename, "rt") as f:
		rows = csv.reader(f)
		headers = next(rows)
		name_idx = headers.index('name')
		shares_idx = headers.index('shares')
		price_idx = headers.index('price')
		for row in rows:
			try:
				shares = int(row[shares_idx])
				price = float(row[price_idx])
			except ValueError as e:
				print(f'Skipping row {row} due to error: {e}')
			result.append((row[name_idx], shares, price))
	return result


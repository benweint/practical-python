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
			result.append({
				'name': row[name_idx],
				'shares': shares,
				'price': price,
			})
	return result


def read_prices(filename):
	result = {}
	with open(filename, 'rt') as f:
		rows = csv.reader(f)
		for row in rows:
			if len(row) < 2:
				continue
			result[row[0]] = float(row[1])
	return result


def make_report(portfolio, prices):
	result = []
	for holding in portfolio:
		current_price = prices[holding['name']]
		change = current_price - holding['price']
		result.append((holding['name'], holding['shares'], current_price, change))
	return result


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print(' '.join(['-' * 10] * len(headers)))

for name, shares, price, change in report:
	print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

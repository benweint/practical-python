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
		result.append((holding['name'], holding['shares'], holding['price'], change))
	return result


portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

basis = 0
current_value = 0
for holding in portfolio:
	basis += holding['shares'] * holding['price']
	current_value += holding['shares'] * prices[holding['name']]

print(f'Cost basis:    ${basis:.2f}')
print(f'Current value: ${current_value:.2f}')
print(f'Net change:    ${current_value - basis:.2f}')

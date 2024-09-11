# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
	result = []
	with open(filename, "rt") as f:
		rows = csv.reader(f)
		headers = next(rows)
		for lineno, row in enumerate(rows, start=1):
			record = dict(zip(headers, row))
			try:
				record['shares'] = int(record['shares'])
				record['price'] = float(record['price'])
			except ValueError as e:
				print(f"Row {lineno}: Couldn't convert: {record}')")
			result.append(record)
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


def print_report(report):
	headers = ('Name', 'Shares', 'Price', 'Change')
	print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	print(' '.join(['-' * 10] * len(headers)))

	for name, shares, price, change in report:
		formatted_price = f'${price:.2f}'
		print(f'{name:>10s} {shares:>10d} ${formatted_price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_path, prices_path):
	portfolio = read_portfolio(portfolio_path)
	prices = read_prices(prices_path)
	report = make_report(portfolio, prices)
	print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

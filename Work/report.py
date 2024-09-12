# report.py
#
# Exercise 2.4

import csv
import fileparse
import tableformat
from stock import Stock

def read_portfolio(filename):
	with open(filename, 'rt') as f:
		records = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str,int,float])
	return [Stock(r['name'], r['shares'], r['price']) for r in records]


def read_prices(filename):
	with open(filename, 'rt') as f:
		return dict(fileparse.parse_csv(f, has_headers=False, types=[str,float]))


def make_report(portfolio, prices):
	result = []
	for holding in portfolio:
		current_price = prices[holding.name]
		change = current_price - holding.price
		result.append((holding.name, holding.shares, current_price, change))
	return result


def print_report(report, formatter):
	formatter.headings(['Name', 'Shares', 'Price', 'Change'])
	# print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	# print(' '.join(['-' * 10] * len(headers)))

	for name, shares, price, change in report:
		formatted_price = f'${price:.2f}'
		rowdata = [name, str(shares), formatted_price, f'{change:.2f}']
		formatter.row(rowdata)


def portfolio_report(portfolio_path, prices_path, format='txt'):
	portfolio = read_portfolio(portfolio_path)
	prices = read_prices(prices_path)
	report = make_report(portfolio, prices)
	formatter = tableformat.create_formatter(format)
	print_report(report, formatter)


def main(args):
	if len(args) == 1:
		args = [args[0], 'Data/portfolio.csv', 'Data/prices.csv']
	args.pop(0)
	portfolio_report(*args)


if __name__ == '__main__':
	import sys
	main(sys.argv)

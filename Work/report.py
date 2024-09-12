# report.py
#
# Exercise 2.4

import csv
import fileparse
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


def print_report(report):
	headers = ('Name', 'Shares', 'Price', 'Change')
	print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
	print(' '.join(['-' * 10] * len(headers)))

	for name, shares, price, change in report:
		formatted_price = f'${price:.2f}'
		print(f'{name:>10s} {shares:>10d} {formatted_price:>10s} {change:>10.2f}')


def portfolio_report(portfolio_path, prices_path):
	portfolio = read_portfolio(portfolio_path)
	prices = read_prices(prices_path)
	report = make_report(portfolio, prices)
	print_report(report)


def main(args):
	portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

if __name__ == '__main__':
	import sys
	main(sys.argv)

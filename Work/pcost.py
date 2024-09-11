# pcost.py
#
# Exercise 1.27

import csv
import sys
from report import read_portfolio

def portfolio_cost(filename):
	portfolio = read_portfolio(filename)
	return sum(holding['shares'] * holding['price'] for holding in portfolio)

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')


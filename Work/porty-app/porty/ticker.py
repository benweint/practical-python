from .follow import follow
import csv
from . import tableformat


def parse_stock_data(lines):
	rows = csv.reader(lines)
	rows = ([row[0], row[1], row[4]] for row in rows)
	rows = ([x[0], float(x[1]), float(x[2])] for x in rows)
	rows = ({ 'name': x[0], 'price': x[1], 'change': x[2] } for x in rows)
	return rows


def ticker(portfile, logfile, fmt):
	import report
	portfolio = report.read_portfolio('Data/portfolio.csv')
	rows = parse_stock_data(follow('Data/stocklog.csv'))
	rows = (row for row in rows if row['name'] in portfolio)

	formatter = tableformat.create_formatter(fmt)
	formatter.headings(['Name', 'Price', 'Change'])

	for row in rows:
		formatter.row([row['name'], f'${row["price"]:.2f}', str(row['change'])])


if __name__ == '__main__':
	ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')

import os
import time


def follow(filename):
	f = open(filename)
	f.seek(0, os.SEEK_END)
	while True:
		line = f.readline()
		if line == '':
			continue
		yield line


if __name__ == '__main__':
	import report

	portfolio = report.read_portfolio('Data/portfolio.csv')

	for line in follow('Data/stocklog.csv'):
		fields = line.split(',')
		name = fields[0].strip('"')
		if name in portfolio:
			price = float(fields[1])
			change = float(fields[4])
			print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')


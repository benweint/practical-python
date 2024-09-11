# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
	'''
	Parse a CSV file into a list of records
	'''
	with open(filename) as f:
		rows = csv.reader(f, delimiter=delimiter)

		if has_headers:
			headers = next(rows)
		else:
			headers = None

		records = []
		for row in rows:
			if not row: # Skip rows with no data
				continue

			if types:
				row = [f(x) for f, x in zip(types, row)]

			if select:
				# TODO: select + has_headers=False is invalid!
				record = { k: v for k, v in zip(headers, row) if k in select }
			elif headers:
				record = dict(zip(headers, row))
			else:
				record = tuple(row)

			records.append(record)

	return records
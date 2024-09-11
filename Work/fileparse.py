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
		for line, row in enumerate(rows, start=1):
			if not row: # Skip rows with no data
				continue

			if types:
				try:
					row = [f(x) for f, x in zip(types, row)]
				except ValueError as e:
					print(f"Row {line}: Couldn't convert {row}")
					print(f"Reason: {e}")
					continue

			if select:
				if not has_headers:
					raise RuntimeError('select argument requires column headers')
				record = { k: v for k, v in zip(headers, row) if k in select }
			elif headers:
				record = dict(zip(headers, row))
			else:
				record = tuple(row)

			records.append(record)

	return records
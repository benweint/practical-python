# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(input, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
	'''
	Parse a CSV-like input stream into a list of records
	'''
	rows = csv.reader(input, delimiter=delimiter)

	headers = None
	if has_headers:
		headers = next(rows)

	records = []
	for line, row in enumerate(rows, start=1):
		if not row: # Skip rows with no data
			continue

		if types:
			try:
				row = [f(x) for f, x in zip(types, row)]
			except ValueError as e:
				if not silence_errors:
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
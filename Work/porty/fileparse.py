# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(input, select=None, types=None, has_headers=True, delimiter=','):
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
				log.warning(f"Row {line}: Couldn't convert {row}")
				log.debug(f"Reason: {e}")
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
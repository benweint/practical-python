class TableFormatter:
	def headings(self, headers):
		'''
		Emit the table headings.
		'''
		raise NotImplementedError()

	def row(self, rowdata):
		'''
		Emit a single row of table data.
		'''
		raise NotImplementedError()


class TextTableFormatter(TableFormatter):
	def headings(self, headers):
		for h in headers:
			print(f'{h:>10s}', end=' ')
		print()
		print(('-'*10 + ' ')*len(headers))

	def row(self, rowdata):
		for d in rowdata:
			print(f'{d:>10s}', end=' ')
		print()


class CSVTableFormatter(TableFormatter):
	def headings(self, headers):
		print(','.join(headers))

	def row(self, rowdata):
		print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
	def headings(self, headers):
		print('<tr>' + ''.join([f'<th>{h}</th>' for h in headers]) + '</tr>')

	def row(self, rowdata):
		print('<tr>' + ''.join([f'<td>{d}</td>' for d in rowdata]) + '</tr>')


def create_formatter(name):
	if name == 'txt':
		return TextTableFormatter()
	elif name == 'csv':
		return CSVTableFormatter()
	elif name == 'html':
		return HTMLTableFormatter()
	else:
		raise RuntimeError(f'invalid format {name}')


def print_table(objects, columns, formatter):
	formatter.headings(columns)
	for obj in objects:
		rowdata = [str(getattr(obj, col)) for col in columns]
		formatter.row(rowdata)

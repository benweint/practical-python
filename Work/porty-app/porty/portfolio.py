from collections import Counter
from . import fileparse
from .stock import Stock


class Portfolio:
	def __init__(self):
		self.holdings = []


	@property
	def total_cost(self):
		return sum(s.cost for s in self._holdings)


	def tabulate_shares(self):
		total_shares = Counter()
		for s in self._holdings:
			total_shares[s.name] += s.shares
		return total_shares


	def __iter__(self):
		return self.holdings.__iter__()


	def __len__(self):
		return len(self.holdings)


	def __getitem__(self, index):
		return self.holdings[index]


	def __contains__(self, name):
		return any(s.name == name for s in self._holdings)


	def append(self, stock):
		if not isinstance(stock, Stock):
			raise TypeError('Expected a Stock instance')
		self.holdings.append(stock)


	@classmethod
	def from_csv(cls, lines, **opts):
		self = cls()
		dicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float], **opts)

		for d in dicts:
			self.append(Stock(**d))

		return self

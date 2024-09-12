class Stock:
	__slots__ = ['name', '_shares', 'price']

	def __init__(self, name, shares, price):
		self.name = name
		self._shares = shares
		self.price = price


	@property
	def cost(self):
		return self.shares * self.price


	def sell(self, shares):
		self.shares -= shares


	def __repr__(self):
		return f"Stock('{self.name}', {self.shares}, {self.price})"


	@property
	def shares(self):
		return self._shares


	@shares.setter
	def shares(self, value):
		if not isinstance(value, int):
			raise TypeError('must be an int')
		self._shares = value

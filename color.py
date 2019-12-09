"""Docstring..."""
class color_t:
	"""Docstring..."""
	def __init__(self ,r ,g ,b):
		"""Docstring..."""
		self.r = r
		self.g = g
		self.b = b

	def __str__(self):
		return (str(self.r) + " " +
				str(self.g) + " " +
				str(self.b))

	def equals(self, other):
		"""Docstring..."""
		return(self.r == other.r and self.g == other.g and self.b == other.b)

	def not_equal(self, other):
		"""Docstring..."""
		return(self.r != other.r or self.g != other.g or self.b != other.b)

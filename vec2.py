"""Docstring..."""

class vec2_t:
	"""Docstring..."""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		"""Docstring..."""
		return(str(self.x) + " " + str(self.y))

	def not_equal(self, other):
		"""Docstring..."""
		return(self.x != other.x or self.y != other.y)

"""Reading color from the screen."""
class color_t:
	"""Class to control the color reading capability."""
	def __init__(self ,r ,g ,b):
		"""Set rgb values."""
		self.r = r
		self.g = g
		self.b = b

	def __str__(self):
		"""Return values."""
		return (str(self.r) + " " +
				str(self.g) + " " +
				str(self.b))

	def equals(self, other):
		"""Determines if values are equal."""
		return(self.r == other.r and self.g == other.g and self.b == other.b)

	def not_equal(self, other):
		"""Determines if values are not equal."""
		return(self.r != other.r or self.g != other.g or self.b != other.b)

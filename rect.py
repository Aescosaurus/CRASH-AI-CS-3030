"""Docstring..."""

class rect_t:
	"""Docstring..."""
	def __init__(self, left, right, top, bot):
		"""Docstring..."""
		self.left = left
		self.right = right
		self.top = top
		self.bot = bot

	def get_width(self):
		"""Docstring..."""
		return(self.right - self.left)

	def get_height(self):
		"""Docstring..."""
		return(self.bot - self.top)

	def __str__(self):
		"""Docstring..."""
		return(str( self.left) + " " + str(self.right) + " " +
               str(self.top) + " " + str(self.bot))

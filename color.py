class color_t:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return(str(self.r) + " " +
               str(self.g) + " " +
               str(self.b))
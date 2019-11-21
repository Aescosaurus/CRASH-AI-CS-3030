class rect_t:
    def __init__(self, left, right, top, bot):
        self.left = left
        self.right = right
        self.top = top
        self.bot = bot

    def __str__(self):
        detail_string = "{} {} {} {}".format(self.left,
                                             self.right,
                                             self.top,
                                             self.bot)
        return detail_string


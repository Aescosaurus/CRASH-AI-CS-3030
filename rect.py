class rect_t:
    def __init__( self,left,right,top,bot ):
        self.left = left
        self.right = right
        self.top = top
        self.bot = bot

    def __str__( self ):
        return( str( self.left ) + " " +
               str( self.right ) + " " +
               str( self.top ) + " " +
               str( self.bot ) )
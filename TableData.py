class Table:
    def __init__(self, row, column, seats):
        self.row = row
        self.column = column
        self.seats = seats
        self.status = 'S'

    def TableIdent(self):
        return str(self.row)+str(self.column)

    def StatusChange(self, status):
        self.status = status


    #Overload-olni kell a komparációt hogy az ülőhelyeket ne vegye figyelembe!
    def __eq__(self, other):
        if not isinstance(other, Table):
            raise NotImplementedError
        return self.row == other.row and self.column == other.column
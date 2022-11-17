class Table:
    def __init__(self, row, column, seats):
        self.row = int(row)
        self.column = int(column)
        self.seats = int(seats)
        self.status = 'S'
        self.order = []

    def TableIdent(self):
        return str(self.row)+str(self.column)

    def SIdent(self):
        return str(self.status)+str(self.seats)

    def StatusChange(self, status):
        self.status = status

    def __eq__(self, other):
        return self.row == other.row and self.column is other.column

    def __ne__(self, other):
        return not self.__eq__(other)
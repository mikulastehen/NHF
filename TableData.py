class Table:
    def __init__(self, *args):

        if len(args) == 4:
            self.row = int(args[0])
            self.column = int(args[1])
            self.status = args[2]
            self.seats = int(args[3])

        elif len(args) == 3:
            self.row = int(args[0])
            self.column = int(args[1])
            self.seats = int(args[2])
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

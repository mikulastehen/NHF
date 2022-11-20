class Table:
    # A konstruktor overloadolva van 3 különböző állapotú objektum felépítésére; Teljesen új asztal létrehozása, meglévő
    # rendelés nélküli asztal létrehozása, meglévő, rendeléssel rendelkező asztal létrehozása
    def __init__(self, *args):

        # Rendeléses asztal (a példány feltölti a hozzá tartozó rendelésekkel a listáját)
        if len(args) == 5:
            self.order = []
            self.row = int(args[0])
            self.column = int(args[1])
            self.status = args[2]
            self.seats = int(args[3])
            orders = args[4].split('.')
            for x in orders:
                self.order.append(x)

        # új asztal (minden új asztal státusza automatikusan 'S' értéket kap)
        elif len(args) == 3:
            self.row = int(args[0])
            self.column = int(args[1])
            self.seats = int(args[2])
            self.status = 'S'
            self.order = []

        # üres asztal (a példány megkapja a paramétereit, és üres rendelés listát készít)
        elif len(args) == 4:
            self.row = int(args[0])
            self.column = int(args[1])
            self.status = args[2]
            self.seats = int(args[3])
            self.order = []

    # Függvény az asztal számának kivonására, ennyi kell csak az asztal egyezések ellenőrzésére
    def TableIdent(self):
        return str(self.row)+str(self.column)

    # Függvény az asztal állapot és ülőhely visszaadárása, ez csak a rajzolási formázáshoz szükséges
    def SIdent(self):
        return str(self.status)+str(self.seats)

    # Override az egyenlőség vizsgálatra, hiszen az asztaloknak csak a pozícióját kell ellenőrizni, a státusz
    # és az ülőhelyszám irreleváns
    def __eq__(self, other):
        return self.row is other.row and self.column is other.column

    # Kompatibilitási okokból a not equals vizsgálatot is felül kell írni!
    def __ne__(self, other):
        return not self.__eq__(other)

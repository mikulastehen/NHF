from time import sleep

import TableData

#Table functions
def TableAdd(Tables):
    print("Adja meg az asztal pocícióját, majd ülőhelyeinek számát!")
    row = input("Sor: ")
    column = input("Oszlop: ")
    seats = input("Ülőhelyek száma: ")
    ntable = TableData.Table(row, column, seats)
    if ntable in Tables:
        print("Hiba! A megadott asztal már létezik")
        sleep(2)
        return None
    else:
        print("Az asztal felvétele sikeres!")
        sleep(2)
        return ntable

def TableRemove(Tables):
    print("Írja be a törölni kívánt asztal számát! (sor és oszlop)")
    rm = input()
    for x in Tables:
        if x.TableIdent() == str(rm):
            Tables.remove(x)
            print("Az asztal törlése sikeres")
            sleep(1)
            break
        else:
            print("A megadott asztal nem található!")
            sleep(1)
            break
    return Tables

#FoodMenu Functions
def PrintMenu():
    pass

#Foglaltsági Térkép Functions
def PrintRestaurant(Tables: TableData):
    maxrow = 20
    maxcolumn = 20
    for x in Tables:
        if x.row > maxrow:
            maxrow == x.row
        if x.column > maxcolumn:
            maxcolumn == x.column
    print('*'*maxcolumn*3+2)
    for x in range(3, maxrow*3+3):
        if x % 3 == 0:
            print('*'+' '*maxcolumn+'*')
        elif x % 3 == 1:
            print('*')



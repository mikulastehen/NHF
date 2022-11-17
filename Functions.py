import os
from time import sleep

import TableData
import pyconio


#Table functions
def TableAdd(Tables):
    print("Adja meg az asztal pocícióját, majd ülőhelyeinek számát!")

    #sorbekérés
    rerow = True
    while rerow == True:
        row = input("Sor: ").strip()
        if int(row) in range(1, 10):
            rerow = False
        else:
            print('A megadott sorszám érvénytelen!')

    #oszlopbekérés
    recol = True
    while recol == True:
        column = input("Oszlop: ").strip()
        if int(column) in range(1, 10):
            recol = False
        else:
            print('A megadott oszlopszám érvénytelen!')

    #ülőhelybekérés
    reseat = True
    while reseat == True:
        seats = input("Ülőhelyek száma: ").strip()
        if int(seats) in range(1, 10):
            reseat = False
        else:
            print('A megadott ülőhelyszám érvénytelen!')

    #új asztal inicializálása (és egyben hibakeresés egyező sor/oszlopszámú asztalra)
    ntable = TableData.Table(row, column, seats)
    if ntable in Tables:
        print("Hiba! A megadott asztal már létezik")
        input()
        return Tables
    else:
        print("Az asztal felvétele sikeres!")
        input()
        Tables.append(ntable)
        return Tables

def TableRemove(Tables):
    print("Írja be a törölni kívánt asztal számát! (sor és oszlop)")
    rm = input().strip()
    talalt = False
    for x in Tables:
        if x.TableIdent() == rm:
            Tables.remove(x)
            return Tables
    if not talalt:
        print('A megadott asztal nem található')
        return Tables

#FoodMenu Functions (WIP)
def ShowMenu(Menu):
    pyconio.clrscr()
    format = 'Napi menü:'
    pyconio.write(f'|{format:^25}|\n')
    for x in Menu:
        pyconio.write(f'|{x:^25}|\n')
    pyconio.flush()
    input()

def SetMenu():
    Menu = []
    print('Írja be a napi menüt!')
    setter = True
    while setter == True:
        kaja = input()
        if kaja != '':
            Menu.append(kaja)
        else:
            return Menu

#Foglaltsági Térkép Functions
def PrintRestaurant(Tables: TableData):
    os.system('mode con: cols=30 lines=31')
    pyconio.clrscr()
    pyconio.gotoxy(0, 0)
    print('*'*30)
    for x in range(1, 29):
        pyconio.gotoxy(0, x)
        print('|')
        pyconio.gotoxy(29, x)
        print('|')
    print('*'*30)

    pyconio.textbackground(pyconio.BROWN)
    pyconio.textcolor(pyconio.BLACK)
    for x in Tables:
        pyconio.gotoxy(3*x.column-1, 3*x.row-1)
        print(x.TableIdent())
        pyconio.gotoxy(3*x.column-1, 3*x.row)
        print(x.SIdent())
    pyconio.textbackground(pyconio.BLACK)
    pyconio.textcolor(pyconio.LIGHTGRAY)
    input()

#Asztalfoglalás Functions
def ReserveTable(Tables):
    reserve = input('Írja be a foglalni kívánt asztal számát: ')
    fail = True
    for x in Tables:
        if x.row == int(reserve[0]) and x.column == int(reserve[1]) and x.status not in ['F', 'R']:
            x.status = 'F'
            print(f'A {reserve} számú asztal foglalása sikeres!')
            input()
            return Tables
    print('Az asztal foglalása sikertelen!')
    input()
    return Tables

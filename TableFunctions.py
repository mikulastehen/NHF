# Ide tartoznak azok a függvények amelyek közvetlenül manipulálják az asztalokat, azaz beveszik paraméternek az egész
# adatszerkezetet és vissza is térnek vele. Az összes függvény használatára igaz a "Tables = Függvény(Tables)"
# szintaxis (kivéve a fájlba mentést és a kirajzolást, azoknak értelemszerűen nincs visszatérési értéke)!
import TableData
import os
import pyconio

helyi_konyvtar = os.path.dirname(os.path.realpath(__file__))
menufile = os.path.join(helyi_konyvtar, 'menus.txt')
tablefile = os.path.join(helyi_konyvtar, 'tables.txt')


# Asztal hozzáadása az adatszerkezethez
def TableAdd(Tables):
    print("Adja meg az asztal pocícióját,\nmajd ülőhelyeinek számát!")

    # Az asztal paramétereinek bekérése szövegformázással
    def Adatbeker(szoveg):
        while True:
            try:
                adat = input(f'{szoveg}: ').strip()
                if int(adat) in range(1, 10):
                    return adat
                else:
                    print(f'A megadott {szoveg} érvénytelen')
            except:
                print('Érvénytelen formátum!')

    # új asztal inicializálása (és egyben hibakeresés egyező sor/oszlopszámú asztalra)
    ntable = TableData.Table(Adatbeker('sor'), Adatbeker('oszlop'), Adatbeker('ülőhely'))
    if ntable in Tables:
        print("Hiba! A megadott asztal már létezik")
        input()
        return Tables
    else:
        print("Az asztal felvétele sikeres!")
        input()
        Tables.append(ntable)
        SaveTables(Tables, tablefile)
        return Tables


# Asztal törlése az adatszerkezetből
def TableRemove(Tables):
    rm = input("Írja be a törölni kívánt asztal számát: ").strip()
    talalt = False
    for x in Tables:
        if x.TableIdent() == rm:
            Tables.remove(x)
            SaveTables(Tables, tablefile)
            print('Az asztal törlése sikeres!')
            input()
            return Tables
    if not talalt:
        print('A megadott asztal nem található!')
        input()
        return Tables


# Asztal foglalása (státusz paraméter módosítása 'F' értékre)
def ReserveTable(Tables):
    reserve = input('Írja be a foglalni kívánt\nasztal számát: ')
    for x in Tables:
        # x.row == int(reserve[0]) and x.column == int(reserve[1])
        if x.TableIdent() == reserve and x.status not in ['F', 'R']:
            x.status = 'F'
            SaveTables(Tables, tablefile)
            print(f'A {reserve} számú asztal foglalása sikeres!')
            input()
            return Tables
    print('Az asztal foglalása sikertelen!')
    input()
    return Tables


# Asztal foglalás törlése (státusz paraméter módossítása 'S' értékre)
def DeleteReservation(Tables):
    reserve = input('Írja be az asztalszámát\na törölni kívánt foglalásnak!')
    for x in Tables:
        if x.TableIdent() == reserve and x.status not in ['S', 'R']:
            x.status = 'S'
            SaveTables(Tables, tablefile)
            print(f'A {reserve} számú asztal foglalásának törlése\nsikeres!')
            input()
            return Tables
    print('Az asztal foglalásának törlése sikertelen!')
    input()
    return Tables


# Rendelés felvétele asztalhoz
def OrderToTable(Tables):
    asztalbe = input('Írja be az asztalszámot a rendeléshez!')
    for x in Tables:
        if x.TableIdent() == asztalbe:
            print('Írja be a rendelt étket\nés kötőjellel elválasztva az árát!')
            while True:
                kaja = input('Írja be a tételt: ')
                if kaja == '':
                    SaveTables(Tables, tablefile)
                    return Tables
                else:
                    try:
                        if len(kaja.split('-')[0]) > 0 and int(kaja.split('-')[1]) > 0:
                            x.order.append(kaja)
                            x.status = 'R'
                        else:
                            print('Hibás formátum!')
                            return Tables
                    except (ValueError, IndexError):
                        print('Hibás formátum!')


# Számla nyomtatása, egyben asztal felszabadítása
def PrintTotal(Tables):
    tablein = input('Írja be a számlázni kívánt asztal számát!')
    found = False
    for x in Tables:
        if x.TableIdent() == tablein:
            found = True
            if x.status == 'R':
                os.system(f'mode con: cols=42 lines={len(x.order) + 6}')
                pyconio.clrscr()
                header = 'Számla a ' + x.TableIdent() + ' számú asztalhoz:'
                print('*' * 42)
                pyconio.write(f"|{header:^40}|")
                pyconio.write(f"|{'':^40}|")
                total = 0
                for y in x.order:
                    total += int(y.split('-')[1])
                    elements = y.split('-')[0] + ' --- ' + y.split('-')[1] + ' Ft'
                    pyconio.write(f"|{elements:^40}|")
                pyconio.write(f"|{'':^40}|")
                totalformatted = 'Végösszeg: ' + str(total) + ' Ft'
                pyconio.write(f"|{totalformatted:^40}|")
                pyconio.write('*' * 42)
                pyconio.flush()
                pyconio.getch()
                x.order = []
                x.status = 'S'
                SaveTables(Tables, tablefile)
                return Tables
            elif x.status in ['S', 'F']:
                print('Ehhez az asztalhoz nincs rendelés!')
                pyconio.getch()
                return Tables
    if not found:
        print('A megadott asztal nincs a nyilvántartásban!')
        pyconio.getch()
        return Tables


# Asztalok kirajzolása
def PrintRestaurant(Tables):
    def PrintTable(x):
        if x.status == 'S':
            pyconio.textbackground(pyconio.BROWN)
            pyconio.textcolor(pyconio.BLACK)
        elif x.status == 'F':
            pyconio.textbackground(pyconio.RED)
            pyconio.textcolor(pyconio.BLACK)
        elif x.status == 'R':
            pyconio.textbackground(pyconio.CYAN)
            pyconio.textcolor(pyconio.BLACK)
        pyconio.gotoxy(3 * x.column - 1, 3 * x.row - 1)
        pyconio.write(x.TableIdent())
        pyconio.gotoxy(3 * x.column - 1, 3 * x.row)
        pyconio.write(x.SIdent())
        pyconio.textbackground(pyconio.BLACK)
        pyconio.textcolor(pyconio.LIGHTGRAY)

    os.system('mode con: cols=30 lines=31')
    pyconio.clrscr()
    pyconio.gotoxy(0, 0)
    pyconio.write('*' * 30)
    for x in range(1, 29):
        pyconio.write(f"|{'':^28}|")
    pyconio.write('*' * 30)

    for x in Tables:
        PrintTable(x)
    pyconio.flush()
    pyconio.getch()
    return


# Asztal adatszerkezet kimentése fájlba
def SaveTables(Tables, tablefile):
    with open(tablefile, 'wt') as file:
        for x in Tables:
            orderlist = ''
            for y in x.order:
                orderlist += '.' + y
            file.write(x.TableIdent() + x.SIdent() + orderlist + ',')


# Asztal adatszerkezet betöltése fájlból
def LoadTables(Tables, tablefile):
    try:
        with open(tablefile, 'rt') as beasztalok:
            tableload = beasztalok.read().split(',')
            for table in tableload:
                if table is not '' and len(table.split('.')) > 1:
                    Tables.append(TableData.Table(table[0], table[1], table[2], table[3], table[5:]))
                elif table is not '':
                    Tables.append(TableData.Table(table[0], table[1], table[2], table[3]))
        return Tables
    except FileNotFoundError:
        ujfile = open(tablefile, 'wt')
        ujfile.close()
        return Tables

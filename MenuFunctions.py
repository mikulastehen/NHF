# Ide tartoznak a napi menüvel kapcsolatos függvények
import pyconio


# A napi menü kiírása
def ShowMenu(Menu):
    pyconio.clrscr()
    format = 'Napi menü:'
    pyconio.write(f'|{format:^40}|\n')
    for x in Menu:
        pyconio.write(f'|{x:^40}|\n')
    pyconio.flush()
    input()

# A napi menü megadása
def SetMenu(Menu):
    print('Írja be a napi menüt!')
    while True:
        kaja = input()
        if kaja != '':
            Menu.append(kaja)
        else:
            return Menu

# A napi menü kimentése fájlba
def SaveMenu(Menu, menufile):
    with open(menufile, 'wt') as file:
        for x in Menu:
            file.write(x+',')

# A napi menü betöltése fájlból
def LoadMenu(Menu, menufile):
    try:
        with open(menufile, 'rt') as bemenu:
            menuload = bemenu.read().split(',')
            for x in menuload:
                if x is not '':
                    Menu.append(x)
        return Menu
    except FileNotFoundError:
        bemenu = open(menufile, 'wt')
        bemenu.close()
        return Menu






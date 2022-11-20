# Menü osztály a menü megjelenítéséért és kezeléséért; A menü bemeneti paraméternek vár egy kezdeti menükurzor
# pozíciót, elemlistát, címet és visszatér egy menüpont index-el
import pyconio
class Navigation:

    # A konstruktor egy navigációs értékszámból, a menü elemeinek listájából és a menü fejlécének megadásával
    # készít menü példányt
    def __init__(self, navseq, menuelements, menutitle):
        self.navseq = navseq
        self.exit = False
        self.menuelements = menuelements
        self.menutitle = menutitle

    # A FormatMenu függvény a menü keretezését, elemeinek megjelenítését végzi feltételes paraméter segítségével
    def FormatMenu(self):
        menuelements = self.menuelements
        menutitle = self.menutitle
        pyconio.clrscr()
        pyconio.write(f'|{menutitle:^40}|\n')

        for x in menuelements:
            if menuelements[self.navseq] == x:
                pyconio.textbackground(pyconio.LIGHTGRAY), pyconio.textcolor(pyconio.BLACK)
                pyconio.write(f'|{x:^40}|\n')
                pyconio.textbackground(pyconio.BLACK), pyconio.textcolor(pyconio.LIGHTGRAY)
            else:
                pyconio.write(f'|{x:^40}|\n')
        pyconio.flush()

    # A PrintMenu függvény végzi a menüben való navigáció kezelését, a fel és le billentyűkkel
    # a navseq értékét csökkentve. Az értékváltoztatás után meghívódik a FormatMenu függvény az új
    # navigációs paraméter értékével
    def PrintMenu(self):
        menuelements = self.menuelements
        pyconio.rawmode()
        while True:
            self.FormatMenu()
            key = pyconio.getch()
            if key == pyconio.DOWN:
                    if self.navseq < len(menuelements)-1:
                        self.navseq += 1
                    elif self.navseq == len(menuelements)-1:
                        self.navseq = 0
            elif key == pyconio.UP:
                if self.navseq > 0:
                    self.navseq -= 1
                elif self.navseq == 0:
                    self.navseq = len(menuelements)-1
            elif key == pyconio.ENTER:
                return self.navseq

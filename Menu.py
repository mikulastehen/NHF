import pyconio

#Menü osztály a menü megjelenítéséért és kezeléséért; A menü bemeneti paraméternek vár egy kezdeti menükurzor pozíciót, és visszatér egy menüpont index-el
class Menu:
    def __init__(self, navseq):
        self.navseq = navseq
        self.exit = False

#A függvény tömbben tárolja a menüpontokat, viszont módosítás esetén a navigációs logika indexelését is módosítani kell!!
    def PrintMenu(self):
        pyconio.clrscr()
        pyconio.write(f'|{"Étteremkezelő Rendszer":^25}|\n')
        menupontok = ['Asztalok megadása', 'Menü rögzítése', 'Új asztal nyitása', 'Rendelés felvétele',
                      'Számla nyomtatása', 'Foglaltsági térkép', 'Kilépés']
        for x in menupontok:
            if menupontok[self.navseq] == x:
                pyconio.textbackground(pyconio.LIGHTGRAY), pyconio.textcolor(pyconio.BLACK)
                pyconio.write(f'|{x:^25}|\n')
                pyconio.textbackground(pyconio.BLACK), pyconio.textcolor(pyconio.LIGHTGRAY)
            else:
                pyconio.write(f'|{x:^25}|\n')
        pyconio.flush()


#Menü navigációs függvény; mindig vár egy billentyűleütést, és indexeléssel vált menüpontot, enter lenyomására visszatér a menüindex-el
    def NavMenu(self):
        pyconio.rawmode()
        exit = False
        while not exit:
            self.PrintMenu()
            key = pyconio.getch()
            if key == pyconio.DOWN and self.navseq < 6:
                self.navseq+=1
            elif key == pyconio.UP and self.navseq > 0:
                self.navseq -= 1
            elif key == pyconio.ENTER:
                return self.navseq




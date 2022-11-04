
import MenuService


MainSections = ['Asztalok megadása', 'Menü rögzítése', 'Új asztal nyitása', 'Rendelés felvétele',
                      'Számla nyomtatása', 'Foglaltsági térkép', 'Kilépés']
FoodSections = ['Napi menü megjelenítése', 'Napi menü módosítása', 'Napi menü törlése', 'Vissza']


MainMenu = MenuService.Menu(0, MainSections, 'Kajaa')
FoodMenu = MenuService.Menu(0, FoodSections, 'Napi menü')

while True:
    navseq = MainMenu.PrintMenu()
    if navseq == 1:
        FoodMenu.PrintMenu()
    elif navseq == 6:
        exit()



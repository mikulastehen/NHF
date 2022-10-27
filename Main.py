import Menu
import NavFunctions

MainSections = ['Asztalok megadása', 'Menü rögzítése', 'Új asztal nyitása', 'Rendelés felvétele',
                      'Számla nyomtatása', 'Foglaltsági térkép', 'Kilépés']
FoodSections = ['Napi menü megjelenítése', 'Napi menü módosítása', 'Napi menü törlése', 'Vissza']


MainMenu = Menu.Menu(0, MainSections, 'Kajaa')
FoodMenu = Menu.Menu(0, FoodSections, 'Napi menü')


navi = NavFunctions.NavFunction(MainMenu, FoodMenu)
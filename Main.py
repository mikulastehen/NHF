import MenuFunctions
import NavigationService
import NavigationLayouts
import os
import TableFunctions

def Main():

    # A menük, almenük inicializása
    MainNavigation = NavigationService.Navigation(0, NavigationLayouts.MainSections, 'Éttermi Kezelőfelület')
    FoodNavigation = NavigationService.Navigation(0, NavigationLayouts.FoodSections, 'Napi menü')
    TableNavigation = NavigationService.Navigation(0, NavigationLayouts.TableSection, 'Asztalok beállítása')
    ReserveNavigation = NavigationService.Navigation(0, NavigationLayouts.ReserveSection, 'Asztalfoglalások')

    # Az adatszerkezetek deklarálása
    Tables = []
    Menu = []

    # A fájlkezeléshez szükséges elérési utak definiálása
    helyi_konyvtar = os.path.dirname(os.path.realpath(__file__))
    menufile = os.path.join(helyi_konyvtar, 'menus.txt')
    tablefile = os.path.join(helyi_konyvtar, 'tables.txt')

    # Asztalok betöltése fájlból
    Tables = TableFunctions.LoadTables(Tables, tablefile)

    # Napi menü betöltése fájlból
    Menu = MenuFunctions.LoadMenu(Menu, menufile)

    # Főprogram vezérlési logika
    while True:

        # főmenü kiírása
        os.system('mode con: cols=42 lines=20')
        navseq = MainNavigation.PrintMenu()
        if navseq == 0:
            # Asztal almenü
            while True:
                os.system('mode con: cols=42 lines=20')
                navseq = TableNavigation.PrintMenu()
                if navseq == 0:
                    Tables = TableFunctions.TableAdd(Tables)
                elif navseq == 1:
                    Tables = TableFunctions.TableRemove(Tables)
                elif navseq == 2:
                    break

        elif navseq == 1:
            # Napi menü almenü
            while True:
                navseq = FoodNavigation.PrintMenu()
                if navseq == 0:
                    MenuFunctions.ShowMenu(Menu)
                elif navseq == 1:
                    Menu = MenuFunctions.SetMenu(Menu)
                elif navseq == 2:
                    Menu = []
                if navseq == 3:
                    break

        elif navseq == 2:
            # Asztalfoglalás almenü
            while True:
                navseq = ReserveNavigation.PrintMenu()
                if navseq == 0:
                    Tables = TableFunctions.ReserveTable(Tables)
                elif navseq == 1:
                    Tables = TableFunctions.DeleteReservation(Tables)
                elif navseq == 2:
                    break

        elif navseq == 3:
            # Rendelés felvétele
            Tables = TableFunctions.OrderToTable(Tables)

        elif navseq == 4:
            # Számla nyomtatása
            TableFunctions.PrintTotal(Tables)

        elif navseq == 5:
            # Asztalok kirajzolása
            TableFunctions.PrintRestaurant(Tables)

        elif navseq == 6:
            # Adatok mentése és kilépés
            TableFunctions.SaveTables(Tables, tablefile)
            MenuFunctions.SaveMenu(Menu, menufile)
            exit()

Main()
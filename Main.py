import Functions
import NavigationService
import NavigationLayouts
import os

import TableData

MainNavigation = NavigationService.Navigation(0, NavigationLayouts.MainSections, 'Éttermi Kezelőfelület')
FoodNavigation = NavigationService.Navigation(0, NavigationLayouts.FoodSections, 'Napi menü')
TableNavigation = NavigationService.Navigation(0, NavigationLayouts.TableSection, 'Asztalok beállítása')
ReserveNavigation = NavigationService.Navigation(0, NavigationLayouts.ReserveSection, 'Asztalfoglalások')
Tables = []
Menu = []
helyi_konyvtar = os.path.dirname(os.path.realpath(__file__))
load_data = os.path.join(helyi_konyvtar, 'adatbetoltes.txt')
tablefile = os.path.join(helyi_konyvtar, 'tables.txt')

with open(tablefile, 'rt') as file:
    load = file.read().split(',')
    for x in load:
        if x is not '':
            Tables.append(TableData.Table(x[0], x[1], x[2], x[3]))

while True:

    #főmenü kiírása
    os.system('mode con: cols=27 lines=20')
    navseq = MainNavigation.PrintMenu()
    #navseq = 6
    if navseq == 0:
        #Asztal almenü
        while True:
            os.system('mode con: cols=27 lines=20')
            navseq = TableNavigation.PrintMenu()
            if navseq == 0:
                Tables = Functions.TableAdd(Tables)
            elif navseq == 1:
                Tables = Functions.TableRemove(Tables)
            elif navseq == 2:
                break

    elif navseq == 1:
        #Napi menü almenü
        while True:
            navseq = FoodNavigation.PrintMenu()
            if navseq == 0:
                Functions.ShowMenu(Menu)
            elif navseq == 1:
                Menu = Functions.SetMenu()
            elif navseq == 2:
                Menu = []
            if navseq == 3:
                break

    elif navseq == 2:
        #Asztalfoglalás almenü
        while True:
            navseq = ReserveNavigation.PrintMenu()
            if navseq == 0:
                Tables = Functions.ReserveTable(Tables)
            elif navseq == 1:
                pass
            elif navseq == 2:
                break


    elif navseq == 5:
        Functions.PrintRestaurant(Tables)

    elif navseq == 6:
        Functions.SaveTables(Tables)
        exit()



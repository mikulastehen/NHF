import Functions
import NavigationService
import NavigationLayouts


MainNavigation = NavigationService.Navigation(0, NavigationLayouts.MainSections, 'Éttermi Kezelőfelület')
FoodNavigation = NavigationService.Navigation(0, NavigationLayouts.FoodSections, 'Napi menü')
TableNavigation = NavigationService.Navigation(0, NavigationLayouts.TableSection, 'Asztal menü')
Tables = []
Menu = []

#Ezt még függvénybe kell rendezni!!!
while True:
    navseq = MainNavigation.PrintMenu()
    if navseq == 0:
        while True:
            navseq = TableNavigation.PrintMenu()
            if navseq == 0:
                # Ellenőrizni kell hogy van e visszatérési értéke az asztalnak, mert hiba esetén none-al tér vissza, és problémát okoz a listában!!
                newtable = Functions.TableAdd(Tables)
                if newtable is not None:
                    Tables.append(newtable)
            elif navseq == 1:
                Tables = Functions.TableRemove(Tables)
            elif navseq == 2:
                break

    elif navseq == 1:
        while True:
            navseq = FoodNavigation.PrintMenu()
            if navseq == 0:
                pass
            if navseq == 3:
                break

    elif navseq == 5:
        pass

    elif navseq == 6:
        exit()



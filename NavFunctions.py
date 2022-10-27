class NavFunction:
    def __init__(self, MainMenu, FoodMenu):
        self.MainMenu = MainMenu
        self.FoodMenu = FoodMenu
    def BackToMain(self, MainMenu):
        valasztas = MainMenu.NavMenu()
        if valasztas == 1:
            self.NavToFoodMenu()


    def NavToFoodMenu(self, FoodMenu):
        if FoodMenu.NavMenu() == 3:
            self.BackToMain()
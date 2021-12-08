#Надеюсь, это хоть немного смешно
class Alcohol:
    def __init__(self, krepost, name, country):
        self.krepost = krepost
        self.name = name
        self.__country = country

class BEER (Alcohol):
    def drink(self):
        print(f'{self.krepost}, {self.name}, Убьет после 4х литров')

class VINO(Alcohol):
    def use(self):
        print(f'{self.krepost}, {self.name}, Убьет после 1,5 литров')

class VODKA(Alcohol):
    def pit(self):
        print(f'{self.krepost}, {self.name}, Убьет после 1 литра')

beer_1 = BEER('4.6%', 'Blanc', 'Germ' )
vino_1 = VINO('16%', 'Старая Келья', 'Bel')
vodka_1 = VODKA('40%', 'Бульбаш', 'Bel')
beer_1.drink()
vino_1.use()
vodka_1.pit()

from amogus_poo.ship import Ship

class Amogus(Ship):
    def __init__(self, impostor , colour):
        Ship.__init__(self)
        self.impostor = impostor
        self.colour = colour
        self.alive = True

    def show_amogus(self):
        return f'Sus, {self.colour} amogus'

class AmogusAlter(Amogus):
    def __init__(self, impostor , colour):
        Amogus.__init__(self, impostor , colour)
    
    def show_amogus(self):
        return f'Sus, this is an alter {self.colour} amogus'
    
from amogus_poo.amogus import Amogus, AmogusAlter

def main():
    amogus = Amogus(impostor = True, colour = "red")
    amogus_alter = AmogusAlter(impostor = True, colour = "red")
    print(amogus.give_task())
    print(amogus_alter.give_task())
    print(amogus.show_amogus())
    print(amogus_alter.show_amogus())

if __name__ == '__main__':
    main()
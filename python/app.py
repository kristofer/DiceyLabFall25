class Bin:
    pass

class Dice:
    def roll(self):
        print("roll!")

    def display(self):
        print("rolled! thanks!")


class Simulation:
    pass

if __name__ == "__main__":
    die = Dice()
    die.roll()
    die.display()

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} Unit created".format(self.name))
        print("Physical {0}, Attack {1}".format(self.hp, self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)

wraith1 = Unit("Wraith", 80, 5)
print("Unit name : {0}, Physical : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("Taken Wraith", 80, 5)
wraith2.clocking = True


if wraith2.clocking == True:
    print("{0} is clocking".format(wraith2.name))
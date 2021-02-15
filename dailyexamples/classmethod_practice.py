class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} Unit created".format(self.name))
        print("Physical {0}, Attack {1}".format(self.hp, self.damage))

class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print("Enemy troops are attacking to the {0} : {1} direction and [Power {2} "\
                .format(self.name, location, self.damage))

    def damaged(self, damage):
        print(" {0} : {1} Got Damage".format(self.name, self.damage))
        self.hp -= damage
        print("{0} : current Physical Energy is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed!!!".format(self.name))


firebat1 = AttackUnit("Firebat", 50, 16)
firebat1.attack("5 o'clock")

firebat1.damaged(25)
firebat1.damaged(25)
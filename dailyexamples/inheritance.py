class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage
        
    def attack(self, location):
        print("Enemy troops are attacking to the {0} : {1} direction and [Power {2} "\
                .format(self.name, location, self.damage))

    def damaged(self, damage):
        print(" {0} : {1} Damaged".format(self.name, self.damage))
        self.hp -= damage
        print("{0} : current Physical Energy is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destroyed!!!".format(self.name))


#dropship (x attack)
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : flying to {1} way. [speed {2}]"\
            .format(name, location, self.flying_speed))
    
#Attack in the air
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# Attack in the air unit
valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3 o'clock")

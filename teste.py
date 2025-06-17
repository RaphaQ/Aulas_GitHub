import random
class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def damage(self, num):
        self.health -= num
    def heal(self, num):
        self.health += num

class Hero(Character):
    def __init__(self, name, health, power, items=[]):
        super().__init__(name, health, power)
        self.bag = []
        for item in items:
            self.bag.append(item)
    def addToBag(self, item):
        self.bag.append(item)
class Villain(Character):
    def __init__(self, name, heatlh, power):
        super().__init__(name, health, power)
    def steal(self, victim):
        victim.bag.remove(random.choice(victim.bag))

rick = Hero("rick", 100, 80, ["sword", "potion", "spoon"])
rick.damage(5)
print(rick.health)
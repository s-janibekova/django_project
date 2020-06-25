from random import random, randint


class Samurai:
    def __init__(self, hp, armor, strength, accuracy, agility):
        self.hp = hp
        self.armor = armor
        self.strength = strength
        self.accuracy = accuracy
        self.agility = agility

    def attack(self, another):
        if isinstance(another, Samurai):
            another.damage(self.strength * randint(0, self.accuracy))

    def damage(self, strength):
        reduction = randint(0, self.agility)
        if self.armor > 0:
            strength, self.armor = strength - self.armor + reduction,\
                                   self.armor - strength + reduction

        if strength > 0:
            self.hp -= strength

        if self.hp <= 0:
            raise Exception

    def __repr__(self):
        return f"hp: {self.hp}\tarmor: {self.armor}"


class Game:
    def __init__(self):
        self.first = Samurai(10, 2, 5, 1, 2)
        self.second = Samurai(3, 13, 2, 20, 1)

    def start(self):
        try:
            while True:
                self.first.attack(self.second)
                self.second.attack(self.first)

                print(f"First: {self.first}\n",
                      f"Second: {self.second}")
        except Exception as exc:
            if self.first.hp > 0:
                print("First won!")
            else:
                print("Second won!")


if
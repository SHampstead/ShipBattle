class Ship:
    def __init__(self, name, make, weapon, support, health = 100, shield = 100):
        self.name = name
        self.make = make
        self.weapon = weapon
        self.support = support
        self.health = health
        self.shield = shield

    def ship_input():
        name = input("What is your ships name? ")
        make = input("What type of ship would you like, Frigate, Destroyer, or Battleship? ")
        weapon = Weapon.weapon_input()
        support = Support.support_input()

    def __repr__(self):
        print("""
        {name} is a {make} class with a large {large}, and medium {medium}, and a samll {small}. It is supported by a {support} module and has {health} HP and {shield} SP.
        """.format(name=self.name, make=self.make, large=self.large, medium=self.medium, small=self.small, support=self.support, health=self.health, shield=self.shield))

class Weapon:
    def __init__(self, size, name, damage, effect):
        self.size = size
        self.name = name
        self.damage = damage
        self.effect = effect

    def weapon_input():
        pass

    def __repr__(self):
        print("""
        {name} does {damage} points of {effect} damage
        """.format(name=self.name, damage=self.damage, effect=self.effect))

class Support:
    def __init__(self, name, effect, system):
        self.name = name
        self.effect = effect
        self.system = system

    def support_input():
        pass

    def __repr__(self):
        print("""
        {name} is a support module that increases {system} points by {effect}
        """.format(name=self.name, system=self.system, effect=self.effect))

class Player:
    def __init__(self, name, ship):
        self.name = name
        self.ship = ship

    def __repr__(self):
        print("""
        {name} is captaining {ship}.
        """.format(name=self.name, ship=self.ship))        
class Ship:
    def __init__(self, name, make, large, medium, small, support, health = 100, shield = 100):
        self.name = name
        self.make = make
        self.large = large
        self.medium = medium
        self.small = small
        self.support = support
        self.health = health
        self.shield = shield

    def __repr__(self):
        print("""
        {name} is a {make} class with a large {large}, and medium {medium}, and a samll {small}. It is supported by a {support} module and has {health} HP and {shield} SP.
        """.format(name=self.name, make=self.make, large=self.large, medium=self.medium, small=self.small, support=self.support, health=self.health, shield=self.shield))

class Weapon:
    def __init__(self, name, damage, effect):
        self.name = name
        self.damage = damage
        self.effect = effect

    def __repr__(self):
        print("""
        {name} does {damage} points of {effect} damage
        """.format(name=self.name, damage=self.damage, effect=self.effect))

class Support:
    def __init__(self, name, effect, system):
        self.name = name
        self.effect = effect
        self.system = system

    def __repr__(self):
        print("""
        {name} is a support module that increases {system} points by {effect}
        """)
        
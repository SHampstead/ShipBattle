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
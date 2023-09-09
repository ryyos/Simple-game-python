class Hero:

    jum_hero = 0
    all_hero = []

    def __init__(self, name, health, damage, defend, mana, energy):
        self.name = name
        self.health = health
        self.damage = damage
        self.defend = defend
        self.mana = mana
        self.energy = energy
        Hero.all_hero.append(name)
        Hero.jum_hero += 1

    def health_up(self, plus):
        self.health += plus

    def damage_up(self, plus):
        self.damage += plus

    def defend_up(self, plus):
        self.defend += plus

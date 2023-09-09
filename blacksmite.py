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

        def health_up(plus):
            self.health += plus

        def damage_up(plus):
            self.damage += plus

        def defend_up(plus):
            self.defend += plus

        print(f'New Hero : {name}')
        jum_hero += 1
        Hero.all_hero.append(name)
        print(f'All Hero : {Hero.all_hero}')

        # def new_hero(name):


class Weapon:
    def __init__(self, plus):
        Hero.damage_up(plus)


class Armor:
    def __init__(self, plus, healthup):
        hero.defend_up(plus)
        hero.health_up(healthup)


alexa = Hero('Alexa', 100, 17, 10, 50, 50)
zoldyck = Hero('Zoldyck', 120, 15, 7, 50, 50)
print(alexa.__dict__)

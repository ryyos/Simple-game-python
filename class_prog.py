class Hero:

    jum_hero = 0
    all_hero = []
    # health = 0

    def __init__(self, name, health, damage, defend, mana, energy):
        self.name = name
        self.health = health
        self.damage = damage
        self.defend = defend
        self.mana = mana
        self.energy = energy
        Hero.all_hero.append(name)
        Hero.jum_hero += 1

    def damage_up(self, plus):
        self.damage += plus

    def defend_up(self, health, armor):
        self.defend += armor
        self.health += health

    def attack(self, enemy):
        enemy.attacked(self)
        print('='*50)
        print(f'Your attack {enemy.name}')
        print('STATUS')
        print(f'Damage dault : {self.damage - enemy.defend}')
        print(f'Your energy  : {self.energy}')
        print(f'Your mana    : {self.mana}')
        print(f'Enemy health remaining : {enemy.health}')
        print(f'Your Health Remaining : {self.health}')
        print('='*50)

    def attacked(self, enemy):
        self.health -= (enemy.damage - self.defend)

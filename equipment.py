from class_prog import Hero
from random import randint


class user:
    def weapon_switch(chose, hero):
        print('='*50)
        print('Chose Your Weapon : ')
        print('1. Bow          (Damage + 14 | Energy - 9)')
        print('2. Sword        (Damage + 16 | Energy - 11)')
        print('3. Magic Ball   (Damage + 20 | Mana   - 13)')
        chose = int(input('Input Your Choise : '))
        match chose:
            case 1:
                # BOW
                damage = 14
            case 2:
                # SWORD
                damage = 16
            case 3:
                # MAGIC BALL
                damage = 20
        return damage

    def armor_switch(chose, hero):
        print('='*50)
        print('Chose Your armor : ')
        print('1. Radiant       (Defend + 14 | Health + 23)')
        print('2. Guardiant     (Defend +  6 | Health + 35)')
        print('3. Antiquiras    (Defend + 18 | Health + 19)')
        chose = int(input('Input Your Choise : '))
        match chose:
            case 1:
                # Radiant
                defend = 14
                health = 23
            case 2:
                # Guardiant
                defend = 6
                health = 35
            case 3:
                # Antiquiras
                defend = 18
                health = 19
        return [health, defend]

    def fundamental(chose, name):
        name.damage_up(user.weapon_switch(chose, name))
        [health, armor] = user.armor_switch(chose, name)
        name.defend_up(health, armor)
        print(f'Atrribute Your Hero : \n{name.__dict__}')
        return name


class comp:
    def weapon_switch(chose, hero):
        chose = randint(1, 3)
        match chose:
            case 1:
                # BOW
                damage = 14
            case 2:
                # SWORD
                damage = 16
            case 3:
                # MAGIC BALL
                damage = 20
        return damage

    def armor_switch(chose, hero):
        chose = randint(1, 3)
        match chose:
            case 1:
                # Radiant
                defend = 14
                health = 23
            case 2:
                # Guardiant
                defend = 6
                health = 35
            case 3:
                # Antiquiras
                defend = 18
                health = 19
        return [health, defend]

    def fundamental(chose, name):
        name.damage_up(comp.weapon_switch(chose, name))
        [health, armor] = comp.armor_switch(chose, name)
        name.defend_up(health, armor)
        print(f'Atrribute Your Hero : \n{name.__dict__}')
        return name

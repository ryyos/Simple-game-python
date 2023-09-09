def weapon_switch(chose, hero):
    print('='*50)
    print('Chose Your Weapon : ')
    print('1. Bow \n2. Sword \n3. Magic Ball\n' + '=' * 50)
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
    print('1. Radiant \n2. Guardiant \n3. Antiquiras\n' + '=' * 50)
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
    return [defend, health]

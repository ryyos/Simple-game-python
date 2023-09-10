from equipment import user
from equipment import comp
from class_prog import Hero
from computer import computer
from random import randint


class Armor:
    def __init__(self, plus, healthup):
        hero.defend_up(plus)
        hero.health_up(healthup)


print('='*50)
print('Chose Hero')
print('1. Alexa \n2. Zoldyck \n3. Lux \n' + '=' * 50)
chose = int(input('Input Your Choise : '))

match chose:
    case 1:
        alexa = Hero('Alexa', 100, 17, 10, 50, 50)
        yusha = user.fundamental(chose, alexa)
    case 2:
        zoldyck = Hero('Zoldyck', 120, 15, 7, 50, 50)
        yusha = user.fundamental(chose, zoldyck)

    case 3:
        lux = Hero('Lux', 90, 20, 10, 60, 30)
        yusha = user.fundamental(chose, lux)

print('='*50)
print(f'Computer turn..')
enemy = computer()

while True:
    print('='*50)
    print('1. Attack')
    print('2. Recovery')
    turn = int(input('Choise : '))

    if turn == 1:
        print('ME')
        yusha.attack(enemy)

    com = randint(1, 2)
    if com == 1:
        print('ENEMY')
        enemy.attack(yusha)

    else:
        print('ENEMY')
        enemy.attack(yusha)

    if (yusha.health <= 0 or enemy.health <= 0):
        if yusha.health <= 0:
            print('COMPUTER WIN!')
        elif enemy.health <= 0:
            print('YOU WIN!')
        break

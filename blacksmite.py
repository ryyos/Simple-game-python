from equipment import user
from class_prog import Hero
from computer import computer


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
        user.fundamental(chose, alexa)
    case 2:
        zoldyck = Hero('Zoldyck', 120, 15, 7, 50, 50)
        user.fundamental(chose, zoldyck)

    case 3:
        lux = Hero('Lux', 90, 20, 10, 60, 30)
        user.fundamental(chose, lux)

print(f'Computer turn..')
computer()

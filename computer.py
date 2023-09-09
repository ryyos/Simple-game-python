from equipment import comp
from class_prog import Hero
from random import randint


def computer():
    chose = randint(1, 3)

    match chose:
        case 1:
            alexa = Hero('Alexa', 100, 17, 10, 50, 50)
            comp.fundamental(chose, alexa)
        case 2:
            zoldyck = Hero('Zoldyck', 120, 15, 7, 50, 50)
            comp.fundamental(chose, zoldyck)

        case 3:
            lux = Hero('Lux', 90, 20, 10, 60, 30)
            comp.fundamental(chose, lux)

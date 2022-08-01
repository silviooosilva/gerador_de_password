import os
import random

folder = './saved-password'

if os.path.isdir(folder):
    pass
else:
    os.mkdir(folder)

def generateName(level: str):

    allLeters = 'abcdefghijklmnopqrstuvwxyz1234567890'
    randomNum = random.randint(5, 10)
    generateName = "".join(random.sample(allLeters, randomNum))
    trueName = f'Password-{level}[{generateName}].txt'
    return trueName

def savePassword(password: str, level: str):
    nameFile = generateName(level)
    file = f'./saved-password/{nameFile}'

    writePassword = open(file, 'w+')
    writePassword.write(password)
    writePassword.close()
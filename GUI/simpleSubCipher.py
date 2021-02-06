# ******************************************************************************
#  Direitos Autorais (c) 2019-2021 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

# Simple Substitution Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import random
import sys

LETTERS_NUMBERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&'


def main():
    print('\n***Simples Cifra de Substituição***')
    while True:
        myMode = input('\nDefina o Modo (e)ncriptar-(d)esencriptar:\n> ')  # set to 'encrypt' or 'decrypt'
        myMessage = input('\nIntroduza a Mensagem:\n> ')
        translated = ''

        if myMode == 'e':
            myKey = getRandomKey()
            checkValidKey(myKey)
            translated = encryptMessage(myKey, myMessage)
            print(f'\nUsando a chave {myKey}')
            print(f'A mensagem encriptada é: {translated}')
            print('\n\033[1;31m[!] - ATENÇÃO: PARA DESENCRIPTAR A MENSAGEM ACONSELHO\n\tA COPIAR TAMBÉM A CHAVE USADA NO PROCESSO DE ENCRIPTAÇÃO..\033[m')
            break
        elif myMode == 'd':
            myKey = input('\nIntroduza a chave usada para encriptar:\n> ')
            checkValidKey(myKey)
            translated = decryptMessage(myKey, myMessage)
            print(f'\nUsando a chave {myKey}')
            print(f'A mensagem desencriptada é: {translated}')
            break
        else:
            print('\nAlgo de errado aconteceu! Tente novamente..')


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS_NUMBERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key: None, message: str):
    if key is None:
        key = getRandomKey()
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key: str, message: str):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS_NUMBERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
    
    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            symbol = '_'
            translated += symbol
    
    return translated


def getRandomKey():
    key = list(LETTERS_NUMBERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()

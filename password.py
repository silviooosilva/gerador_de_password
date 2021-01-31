import random
import os
import time
from platform import system

os.system("clear")
lower = "abcdefghijklmnopqrstuvwxyz"
Upper = lower.upper()
numbers = "0123456789"
junto = lower + Upper
forte = lower + numbers + Upper


def nivel_one():
    r = ''
    while r != 'N':

        print('\033[1;30mNOTA: SERÁ GERADA UMA PASSWORD MAIS FRACA\033[m')
        time.sleep(2)
        print('-' * 30)
        tamanho = int(input('QUER UMA PASSWORD COM QUANTOS CARACTERES? :\t'))
        print('-' * 30)
        if tamanho < 1:
            print('\033[1;31mIMPOSSÍVEL GERAR PASSWORD COM 0 CARACTERES\033[m')
            break
        else:

            password = "".join(random.sample(lower, tamanho))
            print('GERANDO A PASSWORD... ')
            time.sleep(3)
            print('-' * 30)
            print('\033[1;32mPASSWORD GERADA COM SUCESSO\033[m')
            print('=' * 30)
            print(f'PALAVRA PASSE: {password}')
            print('=' * 30)
            r = str(input('DESEJA CONTINUAR?[S/N]:')).strip().upper()[0]
    os.system('clear')
    print('\n\033[1;33mBy: SÍLVIO SILVA\033[m')


def nivel_two():
    r = ''
    while r != 'N':
        print('\033[1;30mNOTA: SERÁ GERADA UMA PASSWORD MEIO FORTE\033[m')
        time.sleep(2)
        print('-' * 30)
        tamanho = int(input('QUER UMA PASSWORD COM QUANTOS CARACTERES? :\t'))
        print('-' * 30)
        password = "".join(random.sample(junto, tamanho))
        print('GERANDO A PASSWORD... ')
        time.sleep(3)
        print('-' * 30)
        print('\033[1;32mPASSWORD GERADA COM SUCESSO\033[m')
        print('=' * 30)
        print(f'PALAVRA PASSE: {password}')
        print('=' * 30)
        r = str(input('DESEJA CONTINUAR?[S/N]:')).strip().upper()[0]
        os.system('clear')
    print('\n\033[1;33mBy: SÍLVIO SILVA\033[m')


def nivel_three():
    r = ''
    while r != 'N':
        print('\033[1;31mNOTA: SERÁ GERADA UMA PASSWORD FORTE\033[m')
        time.sleep(2)
        print('-' * 30)
        tamanho = int(input('QUER UMA PASSWORD COM QUANTOS CARACTERES? :\t'))
        print('-' * 30)
        password = "".join(random.sample(forte, tamanho))
        print('GERANDO A PASSWORD... ')
        time.sleep(3)
        print('-' * 30)
        print('\033[1;32mPASSWORD GERADA COM SUCESSO\033[m')
        print('=' * 30)
        print(f'PALAVRA PASSE: {password}')
        print('=' * 30)
        r = str(input('DESEJA CONTINUAR?[S/N]:')).strip().upper()[0]
        os.system('clear')
    print('\n\033[1;33mBy: SÍLVIO SILVA\033[m')


def ajuda():
    r = "\033[1;31m"
    print('-' * 30)
    print('\tAJUDA')
    print('-' * 30)
    print('COMO CRIAR PASSWORDS SEGURAS')
    print('-' * 30)
    time.sleep(3)
    print(f'{r}[1] - NÃO USE SEU NOME PRÓPRIO OU DE ALGUM FAMILIAR\033[m')
    time.sleep(3)
    print(f'{r}[2] - UTILIZE CARACTERES ESPECIAIS (SE PERMITIDO) COMO O @ NAS SUAS PASSWORDS\033[m')
    time.sleep(3)
    print(f'{r}[3] - FAÇA A JUNÇÃO DE LETRAS MAIÚSCULAS E MINÚSCULAS NAS SUAS PASSWORDS\033[m')
    time.sleep(3)
    print(f'{r}[4] - UTILIZE NÚMEROS\033[m')
    time.sleep(3)
    print('-' * 30)
    print('CRIE BOAS PASSWORDS E SALVE SUAS INFORMAÇÕES PESSOAIS!!!')


def vp():
    print('-' * 30)
    print('VERIFICAR PASSWORD')
    print('-' * 30)
    print('\033[1;30mNOTA: DIGITE A SUA PASSWORD \nE O PROGRAMA LHE DIRÁ SE É SEGURA OU NÃO\033[m')
    print('-' * 36)
    psw = str(input('DIGITE A SUA PALAVRA - PASSE:'))
    print('VERIFICANDO...')
    time.sleep(3)
    if len(psw) >= 6 or psw in forte:
        print('\033[1;32mA SUA PALAVRA - PASSE É SEGURA\033[m')
    else:
        print('\033[1;31mA SUA PALAVRA - PASSE NÃO É SEGURA\033[m')


print('\033[1;32;40m-\033[m' * 30)
print('\033[1;32;40mGERADOR DE PASSWORDS\033[m')
print('\033[1;32;40m-\033[m' * 30)
print('-' * 30)
print('MENU')
print('-' * 30)
print('[0] - PASSWORD NÍVEL 1')
print('[1] - PASSWORD NÍVEL 2')
print('[2] - PASSWORD NÍVEL 3')
print('[3] - AJUDA')
print('[4] - VERIFICAR PASSWORD')
print('[5] - SAIR')
print('-' * 30)
op = int(input('SUA OPÇÃO:'))
if op == 0:
    nivel_one()
if op == 1:
    nivel_two()
if op == 2:
    nivel_three()
if op == 3:
    ajuda()
if op == 4:
    vp()
if op == 5:
    time.sleep(2)
    print(' - TENHA UM BOM DIA!!! ')

import random
import os
import time
from platform import system
from colorama import *
init(autoreset=True)


letras = "abcdefghijklmnopqrstuvwxyz"
maiusculas = letras.upper()
numeros = "0123456789"
simbolos = "~!@#$%^&*()_+=-[]|}{:;/?><"

junto = letras + maiusculas + numeros
forte = letras + numeros + maiusculas + simbolos


def psw(plvra: str, tmnho: int):
    password = "".join(random.sample(plvra, tmnho))
    return password


def nivel_one():
    r = ''
    while r != 'N':
        print('=' * 30)
        print(f'{Fore.CYAN}NOTA: SERÁ GERADA UMA PASSWORD MAIS FRACA')
        time.sleep(2)
        tamanho = random.randint(6, 10)
        password = psw(letras, tamanho)
        print('=' * 30)
        print('\tGERANDO A PASSWORD...')
        time.sleep(3)
        print('=' * 30)
        print(f'{Fore.GREEN}PASSWORD GERADA COM SUCESSO')
        print('=' * 30)
        print(f'PALAVRA PASSE: {Fore.CYAN}{password}')
        print('=' * 30)
        r = str(input('DESEJA GERAR UMA NOVA?[S/N]:')).upper()
    print(f'\n{Fore.YELLOW}By: SÍLVIO SILVA')


def nivel_two():
    r = ''
    while r != 'N':
        print('=' * 30)
        print(f'{Fore.CYAN}NOTA: SERÁ GERADA UMA PASSWORD MEIO FORTE')
        time.sleep(2)
        tamanho = random.randint(6, 15)
        print('=' * 30)
        password = psw(junto, tamanho)
        print('\tGERANDO A PASSWORD... ')
        time.sleep(3)
        print('=' * 30)
        print(f'{Fore.GREEN}PASSWORD GERADA COM SUCESSO')
        print('=' * 30)
        print(f'PALAVRA PASSE: {password}')
        print('=' * 30)
        r = str(input('DESEJA GERAR UMA NOVA?[S/N]:\n> ')).upper()
    print(f'\n{Fore.YELLOW}By: SÍLVIO SILVA')


def nivel_three():
    r = ''
    while r != 'N':
        print('=' * 30)
        print(f'{Fore.CYAN}NOTA: SERÁ GERADA UMA PASSWORD FORTE')
        time.sleep(2)
        tamanho = random.randint(6, 20)
        print('=' * 30)
        password = psw(forte, tamanho)
        print('\tGERANDO A PASSWORD... ')
        time.sleep(3)
        print('=' * 30)
        print(f'{Fore.GREEN}PASSWORD GERADA COM SUCESSO')
        print('=' * 30)
        print(f'PALAVRA PASSE: {Fore.CYAN}{password}')
        print('=' * 30)
        r = str(input('DESEJA GERAR UMA NOVA?[S/N]:\n> ')).upper()
    print(f'\n{Fore.YELLOW}By: SÍLVIO SILVA')


def ajuda():
    r = "\033[1;31m"
    print(f"""{Fore.GREEN}
    --------------------------------
    |            AJUDA             |
    --------------------------------
    | COMO CRIAR PASSWORDS SEGURAS |
    --------------------------------
""")
    time.sleep(3)
    print(f'{r}[1] - NÃO USE SEU NOME PRÓPRIO OU DE ALGUM FAMILIAR')
    time.sleep(3)
    print(f'{r}[2] - UTILIZE CARACTERES ESPECIAIS (SE PERMITIDO) COMO O @ NAS SUAS PASSWORDS')
    time.sleep(3)
    print(f'{r}[3] - FAÇA A JUNÇÃO DE LETRAS MAIÚSCULAS E MINÚSCULAS NAS SUAS PASSWORDS')
    time.sleep(3)
    print(f'{r}[4] - UTILIZE NÚMEROS')
    time.sleep(3)
    print(f'{r}[5] - UTILIZE SENHAS MAIORES OU IGUAIS A SEIS(6) CARÁCTERES')
    time.sleep(3)
    print('-' * 30)
    print('CRIE BOAS PASSWORDS E SALVE SUAS INFORMAÇÕES PESSOAIS!!!')


def vp():
    print(f"""{Fore.CYAN}
    ----------------------
    | VERIFICAR PASSWORD |
    ----------------------

NOTA: DIGITE A SUA PASSWORD
E O PROGRAMA LHE DIRÁ SE É SEGURA OU NÃO
---------------------------------------
""")
    psword = str(input('DIGITE A SUA PALAVRA - PASSE:\n> '))
    print('VERIFICANDO...')
    time.sleep(3)
    if len(psword) >= 6 or psw in forte:
        print('\033[1;32mA SUA PALAVRA - PASSE É SEGURA\033[m')
    else:
        print('\033[1;31mA SUA PALAVRA - PASSE NÃO É SEGURA\033[m')


if __name__ == '__main__':
    print(f"""{Fore.GREEN}
        ----------------------------
        |   GERADOR DE PASSWORDS   |
        ----------------------------
        |           MENU           |
        ----------------------------
        | [0] - PASSWORD NÍVEL 1   |
        | [1] - PASSWORD NÍVEL 2   |
        | [2] - PASSWORD NÍVEL 3   |
        | [3] - AJUDA              |
        | [4] - VERIFICAR PASSWORD |
        | [5] - SAIR               |
        ----------------------------
    """)
    op = int(input('SUA OPÇÃO:\n> '))
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
        print('\t- TENHA UM OTIMO DIA!!!')

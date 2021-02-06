import random as rd

incluir_minusculas = True
incluir_maiusculas = True
incluir_digitos = True
incluir_simbolos = True
# Satisfaz requerimentos mínimos

maiusculas = [chr(j) for j in range(65, 91)]
minusculas = [chr(j) for j in range(97, 123)]
digitos = [str(j) for j in range(0, 10)]
senha = []
universo = []

if incluir_minusculas:
    senha.append(rd.choice(minusculas))
    universo += minusculas

if incluir_maiusculas:
    senha.append(rd.choice(maiusculas))
    universo += maiusculas

if incluir_digitos:
    senha.append(rd.choice(digitos))
    universo += digitos

if incluir_simbolos:
    senha.append(rd.choice(simbolos))
    universo += simbolos

# Aqui temos uma senha com um caracter de cada tipo escolhido.

'''for n in range(n_caracteres_adicionais):
    senha.append(rd.choice(universo))'''

rd.shuffle(senha)  # embaralha os algarismos para evitar a ordem
# preterminada nos primeiros caracteres.
senha = "".join(senha)

print(f"A senha gerada é {senha}")

# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

nome = str(input('Qual o nome da cidade que você nasceu? ')).strip()
print(nome[:5].upper() == 'SANTO')


# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome começa com Silva? {}'.format(nome[:5].upper() == 'SILVA'))
print('Seu nome tem Silva? {}'.format('SILVA'in nome.upper()))
print('Seu nome tem Silva? {}'.format('silva'in nome.lower()))

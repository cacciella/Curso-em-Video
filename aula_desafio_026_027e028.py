# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
#  letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).strip().upper()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "a" apreceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra "a" apareceu na posição {}'.format(frase.rfind('A')+1))


# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em
#  seguida o primeiro e o último nome separadamente.

n = str(input('Qual o seu nome completo? ')).strip()
nome = n.split()
print(nome)
print(nome [0])
print(nome[1])

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))

# Exercício Python 028: Escreva um programa que faça o computador "pensar" em
# um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
#  computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint (0, 5)  # faz o computador pensar em numero aleatório
print('-=' *28)
print('Descubra qual o número que estou pensando, entre 0 e 5 ?')
print('-=' *28)

jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(1)
print('.......................')
sleep(0)

# if (se isso for verdadeiro) então
if jogador == computador:
    print('PARABÉNS, você conseguiu me vencer!!')
# else (senão)
else:
    print('GANHEI! Eu pensei no numero {} e você no {}' .format(computador,jogador))

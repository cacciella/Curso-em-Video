# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Informe o número:'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o numero {}' .format(numero))
print('Unidade é: {}' .format(u))
print('Dezena é: {}' .format(d))
print('Centena é: {}' .format(c))
print('Milhar é: {}' .format(m))

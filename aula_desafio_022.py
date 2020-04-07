# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras aotodo (sem considerar espaços) e Quantas letras tem o primeiro nome.


nome = str(input('Digite seu nome completo: ')).strip()
print(nome,' ,analisando seu nome.....')
print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')),'letras')
print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))

dividido = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))
print('Seu sobrenome nome é {} ele tem {} letras , seu nome é {} e ele tem {} letras'.format(dividido[1],len(dividido[1]),dividido[0], len(dividido[0])))

print(dividido)
print('Seu primeiro nome é {} e tem {} letras ' .format(dividido[0], len(dividido[0])))

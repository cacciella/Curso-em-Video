# leia um numero inteiro e mostre sua tabuada

n=int(input('Informe um numero da Tabuada do: '))
n1=n*1
print('{} x  1 = {}'.format(n,n1))
n2=n*2
print('{} x  2 = {}'.format(n,n2))
n3=n*3
print('{} x  3 = {}'.format(n,n3))
n4=n*4
print('{} x  4 = {}'.format(n,n4))
n5=n*5
print('{} x  5 = {}'.format(n,n5))
n6=n*6
print('{} x  6 = {}'.format(n,n6))
n7=n*7
print('{} x  7 = {}'.format(n,n7))
n8=n*8
print('{} x  8 = {}'.format(n,n8))
n9=n*9
print('{} x  9 = {}'.format(n,n9))
n10=n*10
print('{} x 10 = {}'.format(n,n10))

# Conversão de moeda em
print()

n=float(input('Conversão de Real para Dolar ( cotação de Maio 2018).  \n Informe o valor em Real: R$ '))
n1=(n/3.27)
print('O valor em Dolar é: US$ {:.2f}'.format(n1))
print()
n=float(input('Conversão de Real para Dolar ( cotação de Abril 2020).  \n Informe o valor em Real: R$ '))
n1=(n/5.33)
print('O valor em Dolar é: US$ {:.2f}'.format(n1))

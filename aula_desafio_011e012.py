lar=float(input('Informe a largura(m): '))
alt=float(input('Informe a altura(m): '))
area=(lar*alt)
tint=(area/2)
print('Vai precisar de {} litros de tinta para pintar {}m2'.format(tint,area))

print()
print(' -'*20)
print()

n=float(input('Desconto em todos os produtos da loja. Insira o valor do produto: '))
des=(n*0.05)
valorf=(n-des)
print('O valor do produto com desconto é: R$ {:.2f}'.format(valorf))
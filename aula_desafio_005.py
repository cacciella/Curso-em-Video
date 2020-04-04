n1=int(input('informe um numero: '))
n2=int(int(1))
n3=int(int(1))
ant=n1-n2
suc=n1+n3
print('o numero antecessor é: {} o sucessor é {}' .format(ant,suc))

print(' - '*20)
print()

print('  -  Correção  - ')
print()

n1=float(input('informe um numero: '))
ant= n1-1
suc= n1+1
print('Antecessor do numero {} é o numero {:.2f} o sucessor é {:.2f}' .format(n1,ant,suc))
# é importante ter variáveis para futuramente utlizar no programa como "ant" e "suc"
print('Antecessor do numero {} é o numero {} o sucessor é {:.2f}' .format(n1,(n1-1),(n1+1)))
# podemos tambem usar metodos mais simple só mostrar o resultado e fim de programa como no exemplo acima
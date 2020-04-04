# Operações aritméticas
# soma + subtração - multiplicação * e divisão /
# potencia **  divisão inteira //  resto da divisão %  raiz quadrada n**(1/2) raiz ao cubo n**(1/3)
# ordem de precedencia:  1o () , 2o **,  3o * ,/, //, % ,  4o  + e -

print('-=' * 40)

nome = str( input('Qual é o seu nome? '))
print('prazer em te conhecer {}'.format(nome))
print('prazer em te conhecer {:>20}'.format(nome))
print('prazer em te conhecer {:<20}'.format(nome))
print('prazer em te conhecer {:^20}'.format(nome))
print('prazer em te conhecer {:=^20}'.format(nome))

print(pow(4,2))
print(4 ** 2)

print('-=' * 40)
print('-=' * 40)


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
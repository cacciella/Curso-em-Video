# import math  -  raiz quadrada e arredondamento

import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num,raiz))

print('A raiz quadrada de {} é igual a {:.2f}'.format(num,raiz))

# math.ceil  arredondamento do numero para cima
print('A raiz quadrada de {} é igual a {}'.format(num,math.ceil(raiz)))

# math.floor  arredondamento do numero para baixo
print('A raiz quadrada de {} é igual a {}'.format(num,math.floor(raiz)))

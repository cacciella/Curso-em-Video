a = input('Digite algo: ')
print('O tipo primitivo de {} é: '.format(a),type(a))

# mostra se o valor é numerico, verdadeiro ou falso
print('{} é numero? '.format(a), a.isnumeric())

# mostra se o valor é letra, verdadeiro ou falso
print('é alfabético? ', a.isalpha())

# mostra se o valor é alfanumerico, verdadeiro ou falso
print('é alfanumérico? ', a.isalnum())

# mostra se tem letra maiuscula, verdadeiro ou falso
print('tem letra maíuscula? ', a.isupper())
print('Com letras minusculas o "{}" ? '.format(a), a.islower())

# Letras minusculas e maiusculas juntas "estão capitalizdas"
print('Está capitalizada? ', a.istitle())
print('é numero é decimal o "{}"? '.format(a), a.isdecimal())

#mostra se tem espaços, verdadeiro ou falso
print('Tem espaços em branco: ', a.isspace())

# é importante ter variáveis para futuramente utlizar no programa como "ant" e "suc"
n1=float(input('informe um numero: '))
ant= n1-1
suc= n1+1
print('Antecessor do numero {} é o numero {:.2f} o sucessor é {:.2f}' .format(n1,ant,suc))

# podemos tambem usar metodos mais simple só mostrar o resultado e fim de programa como no exemplo acima
print('Antecessor do numero {} é o numero {} o sucessor é {:.2f}' .format(n1,(n1-1),(n1+1)))

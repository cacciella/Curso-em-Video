
n =str( input('Digite um valor: '))
print(type(n))
# mostra se o valor é numerico, verdadeiro ou falso
print('é numero? ')
print(n.isnumeric())
# mostra se o valor é letra, verdadeiro ou falso
print('é letra? ')
print(n.isalpha())
# mostra se o valor é alfanumerico, verdadeiro ou falso
print('é alfanumérico? ')
print(n.isalnum())
# mostra se tem letra maiuscula, verdadeiro ou falso
print('tem letra maíuscula? ')
print(n.isupper())
print('tem letra minuscula? ')
print(n.islower())
print('tem letra minuscula? ')
print(n.isdecimal())
print(n.isspace())

print(' - '*20)
print()

print('  -  Correção  - ')
print()

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

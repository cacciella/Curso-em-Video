

n1=int(input('Um valor: '))
n2=int(input('Outro valor: '))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma vale: {}, \n o produto vale {}, \n e a divisão {:.2f} ' .format(s,m,d) ,end=' <<< >>> ')
print('divisão inteira {} e potencia {}'.format(di,e))


n=int(input('Informe um numero: '))
doub = n * 2
trip = n * 3
raiz = n**(1/2)
print('Esse é o dobro {}, o triplo {} e a raiz quadrada {}, do numero {} informado' .format(doub,trip,raiz,n))
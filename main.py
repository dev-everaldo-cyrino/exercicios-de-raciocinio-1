quant = int(input('quantos numeros na pesquisa: '))
nnumero = 1
totalpar=0
totalimpar=0
listapar = []
listaimpar = []
for x in range(quant):
    num = int(input('qual o {}° numero:  '.format(nnumero)))
    
    if num % 2 ==1:
        listaimpar.append(num)
        totalimpar +=num
        
        nnumero +=1
        
    if num % 2 ==0:
        listapar.append(num)
        totalpar +=num
        nnumero +=1
print('-----FIM-----')
print('foram usados um total de {} numeros'.format(nnumero-1))
print('os numeros {} são pares, e somando todos temos {}'.format(listapar,totalpar))
print('e os numeros {} são impares, e somando todos temos {}'.format(listaimpar,totalimpar))
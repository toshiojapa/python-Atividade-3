núm =[[],[]]
valor = 0
print('Digite 7 números sendo o ultimo 0')
for c   in range(1,8):
    valor= int(input(f'Digite o {c}º. valor:'))
    if valor <=0 == 0:
        núm[0].append(valor)
    else:
         núm[1].append(valor)
print('-='* 30)
núm.sort()
soma = sum(núm[1])
print ('A soma dos valores possitivos e inteiros é:',(soma))
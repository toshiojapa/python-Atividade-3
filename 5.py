listanum = []
mai = 0
men = 0

for c  in range(0,10):
    listanum.append(int(input(f'Exercício 5 Digite o {c}º. valor:')))
    if c == 0:
     mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print ('O valor mais alto :',(mai)) 
     
print ('O valor mais baixo :',(men))
   
        


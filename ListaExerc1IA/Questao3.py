#3. Faça um programa que leia e preencha uma matriz de 10x10. No final, imprima
#a matriz.
matriz=[]
for i in range (0,10):
    local=[]
    for i in range(0,10):
        local.append(int(input('Digite um número:')))#escrever e ler
    matriz.append(local)
for i in range (0,10):
    print(matriz[i])
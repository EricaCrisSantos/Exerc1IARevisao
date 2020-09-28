#4. Faça um programa que leia 10 números, insira em uma pilha. O programa deve
#remover os dados da pilha e imprimi-los na tela.
#pilha ultimo elemento que entra  e o primeiro que sai LIFO
pilha=[]
for i in range(0,10):
    pilha.append(int(input('Digite um número: ')))
for i in range(0,10):
    print(pilha.pop())
    

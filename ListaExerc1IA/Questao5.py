#5. Faça um programa que leia 10 números, insira em uma fila. O programa deve
#remover os dados da fila e imprimi-los na tela.
#fila primeiro a entrar primeiro a sair
from collections import deque
fila=deque([])
for i in range(0,10):
    fila.append(int(input('Digite um número: ')))
for i in range(0,10):
    print(fila.popleft())


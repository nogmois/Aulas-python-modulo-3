'''Faça um programa que leia 5 valores numericoa e guarde-os em uma lista.
No final, mostre e o menor valores digitados e as sus respectivas posições na lista'''

valores = list()
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
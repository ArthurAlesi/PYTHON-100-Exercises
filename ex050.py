'''
faça um programa que leia varios numeros inteiros e
mostre a soma apenas daqueles que sao pares
'''

soma = 0
for i in range(6):
    num = int(input("Diga um numero"))
    if num % 2 == 0:
        soma += num

print("A soma foi ",soma)
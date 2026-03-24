"""
Faça um programa que calcule a soma dos números de 1 a 100 utilizando o comando for e while.
"""

sum = 0
for num in range(1, 101):
    sum += num

print(f'A soma com "for" de 1 a 100 é {sum}')


max = 100
count = 1
sum = 0

while count <= max:
    sum += count
    count += 1

print(f'A soma com "while" de 1 a 100 é {sum}')

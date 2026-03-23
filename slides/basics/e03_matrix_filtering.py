"""
3. Filtragem de Dados em Matriz

Dada uma lista de listas (uma matriz) contendo números inteiros, utilize laços
for aninhados para percorrer todos os elementos. O programa deve criar uma nova
lista contendo apenas os números que são múltiplos de 3 e maiores que 10.

Exemplo de entrada: [[5, 12, 18], [7, 9, 21], [30, 4, 2]]
Saída esperada: [12, 18, 21, 30]
"""

# TODO: implementar exercício
try:
    # Constants / Configuration
    MATRIX = [[5, 12, 18], [7, 9, 21], [30, 4, 2]]

    # Variables
    selected_numbers = []

    # Business Rules
    for list in MATRIX:
        for number in list:
            if number % 3 == 0 and number > 10:
                selected_numbers.append(number)

    # Output
    print(f"Dada a lista {MATRIX}")
    print(f"Esses são os número múltiplos de 3 e maiores que 10:")
    print(selected_numbers)


except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")

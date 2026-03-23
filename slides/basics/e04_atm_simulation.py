"""
4. Simulação de Caixa Eletrônico

Desenvolva um programa que simule um saque em um caixa eletrônico. O usuário
deve informar o valor que deseja sacar (inteiro). O programa deve utilizar um
laço while para calcular o menor número de cédulas possíveis para entregar o
valor, utilizando notas de R$ 50, R$ 20, R$ 10 e R$ 1.

Dica: a cada iteração, verifique se o valor restante é maior ou igual à nota
atual; se for, subtraia o valor da nota e conte uma cédula. Quando não for mais
possível usar a nota atual, passe para a próxima nota menor.
"""

# TODO: implementar exercício
from time import sleep

from shared.text import normalize_number

try:
    print("---| Simulador de Caixa Eletrônico |---\n")

    # Constants / Configuration
    BILL_OF_50 = 50
    BILL_OF_20 = 20
    BILL_OF_10 = 10
    BILL_OF_01 = 1

    # Variables
    remaining_value = 0
    withdraw_bills = {
        50: 0,
        20: 0,
        10: 0,
        1: 0
    }

    # Inputs
    print("Bem vindo ao ATM Python")
    raw_withdraw = input("Informe o valor que deseja sacar: € ")

    # Sanitization
    withdraw = normalize_number(raw_withdraw)

    # Validation
    if withdraw is None:
        print("É preciso informar um valor válido")

    elif withdraw < 1:
        print("É preciso sacar um valor igual ou maior a € 1")

    else:
        try:
            withdraw = int(withdraw)
        except ValueError:
            print("É preciso informar um número inteiro. Esse ATM não possui cêntimos.")

        remaining_value = withdraw
        while remaining_value > 0:
            if remaining_value // BILL_OF_50 > 0:
                bill = BILL_OF_50
            elif remaining_value // BILL_OF_20 > 0:
                bill = BILL_OF_20
            elif remaining_value // BILL_OF_10 > 0:
                bill = BILL_OF_10
            else:
                bill = BILL_OF_01

            withdraw_bills[bill] = remaining_value // bill
            remaining_value -= withdraw_bills[bill] * bill

    # Output
        print("Calculando notas...")
        sleep(1)
        print("Saque realizado com sucesso. Retire seu dinheiro abaixo:")
        sleep(0.2)
        for bill in withdraw_bills.keys():
            if withdraw_bills[bill] > 0:
                sleep(0.2)
                print(f"NOTAS DE €{bill}: {withdraw_bills[bill]}")
        sleep(0.2)
        print(f"Saque de €{withdraw} finalizado.")
        sleep(0.2)
        print("Volte sempre")


except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")

except ValueError as error:
    print(f"Entrada inválida: {error}")

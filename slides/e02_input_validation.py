"""
Faça um programa que solicite ao usuário que informe a senha. Enquanto a senha informada for diferente de "python123", o programa deve solicitar novamente a senha. 
Quando a senha correta for informada, o programa deve exibir a mensagem "Acesso Permitido" e encerrar.
"""
MASTER_PASSWORD = "python123"
MAX_ATTEMPTS = 3
access_validated = False
attempts = 0

while not access_validated and attempts < MAX_ATTEMPTS:
    pwd = input("Informe a senha: ")
    attempts += 1
    
    if pwd == MASTER_PASSWORD:
        access_validated = True
        print("Acesso Permitido")
    else:
        print("Senha incorreta. Tente novamente.")

if not access_validated:
    print("Número máximo de tentativas excedido.")

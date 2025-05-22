import datetime

# Variáveis iniciais
saldo = 0.0
extrato = []
LIMITE_SAQUE = 500.00
LIMITE_SAQUES_DIARIOS = 3
saques_realizados_hoje = 0
data_hoje = datetime.date.today()

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito. Tente novamente.")

def sacar(valor):
    global saldo, saques_realizados_hoje, data_hoje

    # Zerar saques se o dia mudou
    if datetime.date.today() != data_hoje:
        saques_realizados_hoje = 0
        data_hoje = datetime.date.today()

    if saques_realizados_hoje >= LIMITE_SAQUES_DIARIOS:
        print("Limite diário de saques atingido.")
    elif valor > LIMITE_SAQUE:
        print(f"Limite por saque é de R$ {LIMITE_SAQUE:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente para saque.")
    elif valor <= 0:
        print("Valor de saque inválido.")
    else:
        saldo -= valor
        saques_realizados_hoje += 1
        extrato.append(f"Saque: R$ {valor:.2f}")
        print("Saque realizado com sucesso!")

def exibir_extrato():
    print("\n=== EXTRATO ===")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for operacao in extrato:
            print(operacao)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=================\n")

def menu():
    while True:
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Informe o valor para depósito: R$ "))
                depositar(valor)
            except ValueError:
                print("Entrada inválida. Digite um número.")
        elif opcao == "2":
            try:
                valor = float(input("Informe o valor para saque: R$ "))
                sacar(valor)
            except ValueError:
                print("Entrada inválida. Digite um número.")
        elif opcao == "3":
            exibir_extrato()
        elif opcao == "4":
            print("Obrigado por usar nosso sistema bancário!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o programa
menu()
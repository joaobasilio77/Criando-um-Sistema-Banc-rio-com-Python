menu = """
[d] Depositar   

[s] Sacar

[e] Extrato

[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Valor inválido")
    elif opcao == "s":
        valor = float(input("informe o valor do saque"))

        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f} \n"
            numero_saques += 1

        elif  valor > limite:
            print(" valor excedeu o limite")

        elif numero_saques >= LIMITE_SAQUES:
            print ("falha. Numero de saques excedido")

        else:
            print ("valor inválido")

    elif opcao == "e":
        print ("\n ======== EXTRATO =========")
        print(" Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")



    elif opcao == "q":
        break

    else:
        print("Operação inválida")






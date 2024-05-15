menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> 
'''


saldo = 0
num_saques = 0
LIMITE_SAQUES = 3
extrato = ""
limite = 500


def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R${valor:.2f}\n"
    else:
        print("O valor informado é inválido")


def sacar(valor):
    global saldo, num_saques, limite, extrato

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        return print("Você não tem saldo suficiente.")

    if excedeu_limite:
        return print("O valor de saque é maior que o limite.")

    if excedeu_saques:
        return print("Você excedeu o número de saques permitidos.")

    if valor > 0:
        saldo -= valor
        num_saques += 1
        extrato += f"Saque de R${valor:.2f}\n"
        return
    else:
        return print("O valor informado é inválido")

def  exibir_extrato():
    print("Extrato:")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"R${saldo:.2f}")


if __name__ == '__main__':
    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = int(input("Valor a ser depositado: "))
            depositar(valor)
            continue

        if opcao == "s":
            valor = int(input("Valor a ser sacado: "))
            sacar(valor)
            continue

        if opcao == "e":
            exibir_extrato()
            continue

        if opcao == "q":
            break

        print("Operação inválida")


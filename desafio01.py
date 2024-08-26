menu = """

[1] = Sacar
[2] = Depositar
[3] = Extrato
[4] = Sair
Escolha uma opção:"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    escolha = input(menu)
    
    if escolha == '1':
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

        
    elif escolha == '2':
        valor = float(input('Digite o valor a ser depositado: '))
        
        if valor <= 0:
            print('Valor inválido, insira um valor maior que 0')
        else:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'     
        
    elif escolha == '3':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        print('Extrato')
          
    elif escolha == '4':
        print('Sair')
        break
    
    else:
        print('Opção inválida')
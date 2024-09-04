print("======= Bem vindo ao Banco do Macauli =======")
#agora com sistema de login e cadastro de contas

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES= 3

usuarios= {
    "pessoa1": "senha",
    "pessoa2": "senha2"
}

def cadastrar_usuario():
    print("\n======= Cadastro de Conta =======")
    usuario = input("Digite um nome de usuário: ")
    
    if usuario in usuarios:
        print("Usuário já existe! Tente outro nome.")
    else:
        senha = input("Digite uma senha: ")
        confirmar_senha = input("Confirme a senha: ")
        
        if senha == confirmar_senha:
            usuarios[usuario] = senha
            print(f"Usuário {usuario} cadastrado com sucesso!")
        else:
            print("As senhas não coincidem. Tente novamente.")

def validar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        return True
    return False

while True:
    print("\n======= Menu Principal =======")
    opcao_inicial = input("[c] cadastrar nova conta\n[l] Login\n[q] Sair\nEscolha uma opção: ")

    if opcao_inicial== "c":
        cadastrar_usuario()
    elif opcao_inicial == "l":
        print("\n======= Login =======")
        usuario = input("Nome de usuário: ")
        senha= input("Senha: ")
        
        if validar_login(usuario, senha):
            print(f"Seja bem-vindo, {usuario}!")
            break
        else:
            print("Nome de usuário ou senha incorretos. Tente novamente.")
    elif opcao_inicial == "q":
        print("Saindo")
        exit()
    else:
        print("Opção inválida! Tente novamente.")

while True:
    print("\n======= Menu =======")
    opcao = input("[d] Deposito\n[s] Saque\n[e] Extrato\n[q] Sair\nEscolha uma opção: ")

    if opcao == "d":
        valorDeposito = float(input("Qual valor você gostaria de depositar? "))
        
        if valorDeposito > 0:
            saldo += valorDeposito
            extrato += f"Deposito: R$ {valorDeposito:.2f}\n"
            print(f"Depósito de R$ {valorDeposito:.2f} realizado com sucesso!")
        else:
            print("Operação inválida! O valor do depósito deve ser positivo.")

    elif opcao== "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você já atingiu o limite de saques diários.")
        else:
            valorSaque = float(input(f"Quanto você deseja sacar? Seu saldo atual é de R$ {saldo:.2f}\n"))
            
            if valorSaque > saldo:
                print("Saldo insuficiente!")
            elif valorSaque > limite:
                print(f"O valor do saque excede o limite de R$ {limite:.2f}")
            elif valorSaque > 0:
                saldo -= valorSaque
                extrato += f"Saque: R$ {valorSaque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valorSaque:.2f} realizado com sucesso! Seu saldo atual agora é R$ {saldo}")
            else:
                print("Operação inválida! O valor do saque deve ser positivo.")

    elif opcao== "e":
        print("\n========== Extrato ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==============================")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida! selecione novamente a operação desejada.")


from datetime import datetime

def verificar_cadastro(cpf_login, numero_conta_login, cliente, conta):

    for dado in range(len(conta)):
        if conta[dado]["cpf"] == cpf_login and cliente[dado]["cpf"] == cpf_login and conta[dado]["N_conta"] == numero_conta_login :
            return False
    return True

def cadastro_cliente(agencia, N_conta, cliente, conta):

    def verificar_data(data):
        try:
            dia, mes, ano = map(int, data.split('/'))
            if (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12) and (ano >= 1900 and ano <= 2022):
                return True
            else:
                return False
        except ValueError:
            return False

    tentativa_cadastro = True
    while tentativa_cadastro == True:

        nome = input("Digite seu nome:\n")
        if not nome.isalpha():
            print("Insira seu nome com somente LETRAS\n")
            print("Recomeçando o cadastro...\n\n")
            continue
        
        nascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa:\n")
        if not verificar_data(nascimento):
            print("\nInsira a data corretamente, no formato dd/mm/aaaa\n")
            print("Recomeçando o cadastro...\n\n")
            continue

        cpf = input("Digite seu cpf com somente números:\n")
        if not cpf.isnumeric():
            print("Insira seu CPF com somente NÚMEROS\n")
            print("Recomeçando o cadastro...\n\n")
            continue
        cpf = int(cpf)

        endereço = input("Digite seu endereço:\n")
        N_casa = input("Digite o número da sua casa:\n")
        if not N_casa.isnumeric():
            print("Insira o NÚMERO DA CASA com somente NÚMEROS\n")
            print("Recomeçando o cadastro...\n\n")
            continue
        N_casa = int(N_casa)

        bairro = input("Digite o seu Bairro:\n")
        cidade = input("Digite sua cidade:\n")
        estado = input("Digite o estado:\n").upper()
        if not estado.isalpha():
            print("Insira o nome do seu ESTADO com somente LETRAS\n")
            print("Recomeçando o cadastro...\n\n")
            continue

        movimentacao = ()
        saldo = 0
        MAXIMO_SAQUE_DIARIO = 3
        logadouro = [endereço, N_casa, bairro, cidade, estado]
        clientes_dados = {"cpf":cpf, "nome":nome, "nascimento":nascimento, "logadouro":logadouro}
        conta_dados = {"cpf": cpf, "N_conta":N_conta, "agencia":agencia, "saldo":saldo, "movimentacao":movimentacao, 
                    "saques_diario":MAXIMO_SAQUE_DIARIO}
        
        for i in range(len(cliente)):
            if cpf == cliente[i]["cpf"]:
                print("Dados do usuário já forma cadastrados anteiormente.\n")
                tentativa_cadastro == True 
        tentativa_cadastro = False

    cliente.append(clientes_dados)
    conta.append(conta_dados)
    print(f"\nUsuário cadastrado com sucesso!\n DADOS DE LOGIN\n  Login  -  {cpf} \n  Senha  -  {N_conta}\n")
    
    return cliente, conta
            
def verificar_extrato(indice_conta_banco_de_dados,conta):
    movimentos = conta[indice_conta_banco_de_dados]["movimentacao"]
    qntd = len(movimentos)
    return qntd

def verificar_saldo(valor_saque, conta, indice_conta_banco_de_dados):

    saldo_atual = conta[indice_conta_banco_de_dados]["saldo"]
    if saldo_atual < valor_saque:
        return False, saldo_atual
    return True , saldo_atual
    
def verificar_max_saque_diario(conta, indice_conta_banco_de_dados):
    qntd_saque_diario = conta[indice_conta_banco_de_dados]["saques_diario"]
    
    if qntd_saque_diario > 0 and qntd_saque_diario <= 3:
        return True
    return False

def funcao_indices_dados_clientes(conta, cliente, cpf_login, numero_conta_login):
    for dado in range(len(conta)):
        if conta[dado]["cpf"] == cpf_login and clientes[dado]["cpf"] == cpf_login and numero_conta_login == conta[dado]["N_conta"]:
            indice_conta = dado
            primeiro_nome_cliente = cliente[dado]["nome"].split(" ")
            return (indice_conta, primeiro_nome_cliente[0])

def funcao_extrato(indice_conta_banco_de_dados,conta):

    print("MOVIMENTAÇÃO DO DIA\n")
    movimentos = conta[indice_conta_banco_de_dados]["movimentacao"]
    for apresentar in movimentos:
        print(f" - {apresentar}")
    print("\n\n")  

def funcao_saque(*,valor_saque, conta, indice_conta_banco_de_dados):
    
    conta[indice_conta_banco_de_dados]["saldo"] -= valor_saque
    conta[indice_conta_banco_de_dados]["saques_diario"] -= 1
    conta[indice_conta_banco_de_dados]["movimentacao"] += (f"Saque     -  R$ {valor_deposito}",)
    saldo_atualizado = conta[indice_conta_banco_de_dados]["saldo"]
    print(f"\nValor sacado! \nSeu saldo atual é de R$ {saldo_atualizado}")

    return conta

def funcao_deposito(valor_deposito, conta, indice_conta_banco_de_dados,/):

    conta[indice_conta_banco_de_dados]["saldo"] +=  valor_deposito
    conta[indice_conta_banco_de_dados]["movimentacao"] += (f"Deposito  -  R$ {valor_deposito}",)
    saldo_atualizado = conta[indice_conta_banco_de_dados]["saldo"]
    print(f"\nValor depositado! \nSeu saldo atual é R$ {saldo_atualizado}\n")

    return conta

#Dados estaticos e espécie de banco de dados
AGENCIA = "0001"
LIMITE = 500
clientes = []
conta = []
gerador_conta = 2
cadastrado = "S"

while cadastrado == "S":

    print("BEM VINDO USUÁRIO!")
    cadastrado = input("Você possui cadastro? \n"
                    " [S] - Tenho cadastro\n"
                    " [N] - Não tenho cadastro\n").upper()
    
    if cadastrado == "N":
        criar_conta = input("Gostaria de criar sua conta agora?\n"
                            " [S] - Sim, gostaria de criar\n"
                            " [N] - Não, desejo sair\n").upper()
        
        if criar_conta == "S":
            print("Vamos iniciar o seu cadastro...\n")
            cadastro_cliente(AGENCIA, gerador_conta, clientes, conta)
            gerador_conta += 1
            cadastrado = "S"
            
        elif criar_conta == "N":
            break

        else:
            print("Digite uma opção existente.\n")
            cadastrado = "S"

    elif cadastrado == "S":
        print("Por favor insira seus dados para acessar a conta...\n")
        cpf_login = input("Digite o seu CPF (somente números):\n") 
        numero_conta_login = input("Digite o número da sua conta:\n")
        
        if cpf_login.isnumeric() and numero_conta_login.isnumeric():
            cpf_login, numero_conta_login = int(cpf_login), int(numero_conta_login)

            if verificar_cadastro(cpf_login, numero_conta_login, clientes, conta) == True:
                print("Conta não existe\n")
                
                criar_conta = input("Gostaria de criar sua conta agora?\n"
                                    " [S] - Sim, gostaria de criar\n"
                                    " [N] - Não, desejo sair\n"
                                    " [T] - Tentar logar novamente\n").upper()
                
                if criar_conta == "S":
                    print("Vamos iniciar o seu cadastro...\n")
                    cadastro_cliente(AGENCIA, gerador_conta, clientes, conta)
                    gerador_conta += 1
                    cadastrado == "S"

                elif criar_conta == "T":
                    continue
                
                elif criar_conta == "N":
                    break

                else:
                    print("Comando inválido.\n")
                    continue
                
            else:
                indice_conta_banco_de_dados, nome_cliente = funcao_indices_dados_clientes(conta, clientes, cpf_login, numero_conta_login)
                print(f"Seja Bem-vindo {nome_cliente}!\n")
                
                operacao = ""
                while operacao != "F":

                    operacao = (input("Qual operação deseja executar:\n"
                                        "          [D] - DEPOSITO\n"
                                        "          [E] - EXTRATO \n"
                                        "          [S] - SAQUE   \n"
                                        "          [F] - Finalizar atendimento\n")).upper()
                    
                    if (operacao == "D" or operacao == "E" or operacao == "S" or operacao == "E" or operacao == "F") and operacao.isalpha():
                        
                        if operacao == "D":
                            valor_deposito = input("Digite o valor para depositar:\n") 
                            if valor_deposito.isnumeric():
                                valor_deposito = int(valor_deposito)

                                if valor_deposito > 0:
                                    funcao_deposito(valor_deposito, conta, indice_conta_banco_de_dados)
                                
                                else:
                                    print("Erro ao depositar, tente novamente.\n")
                                    continue
                            
                            else:
                                print("\nDigite apenas números.\n")
                                continue

                        elif operacao == "S":
                            valor_saque = input("Digite o valor que deseja sacar:\n")  #tem que verificar a entrada
                            
                            if valor_saque.isnumeric():
                                valor_saque = int(valor_saque)

                                if valor_saque <= LIMITE:
                                    Saque_permitido, saldo_conta = verificar_saldo(valor_saque, conta, indice_conta_banco_de_dados)
                                    
                                    if Saque_permitido == True:
                                        analise_limite_diario = verificar_max_saque_diario(conta, indice_conta_banco_de_dados)
                                        
                                        if analise_limite_diario == True:
                                            funcao_saque(valor_saque = valor_saque, conta = conta, indice_conta_banco_de_dados = indice_conta_banco_de_dados)   
                                        
                                        else:
                                            print("Saque não permitido, limite de saques excedido.\n")
                                            continue   
                                    
                                    else:
                                        print(f"Saldo INSUFICIENTE para sacar \nSaldo atual R$ {saldo_conta}\n")
                                        continue
                                
                                else:
                                    print(f"O valor máximo por saque é de R$ {LIMITE}.\n Tente novamente\n")
                                    continue
                            else:
                                print("\nDigite apenas números.\n")
                                continue
                        
                        elif operacao == "E":
                            qntd_movimentos  = verificar_extrato(indice_conta_banco_de_dados, conta) 
                            
                            if qntd_movimentos != 0:
                                funcao_extrato(indice_conta_banco_de_dados, conta)                     
                            
                            else:
                                print("\nAinda não houve movimentação em sua conta.\n")
                                continue                        
                    else:
                        print("Comando inválido, tente novamente.\n")
                        continue
        else:
            print("\nLOGIN ou NÚMERO DA CONTA incorretos. Por favo insira seus dados de LOGIN corretamente\n")
            continue
    else:
        print("Por favor digite uma sigla válida.\n")
        cadastrado = "S"
        continue   
print("Encerrando serviços...")

# --Falta função que verifica se o valor de saque e deposito é permitido
#   Somente valores que possam usar notas (2,5,10,20,50,100,200)

# -- Em cadastro (CPF) e CPF_login não foi colocado um valor minimo e maximo
#    de qntd de numeros do CPF a fim de facilitar o teste.


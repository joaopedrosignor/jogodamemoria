# Verificação de valor numérico    
def verificaValorNumerico(msg):
    elemento = input(msg)
    while not elemento.isnumeric():
        print("Digite um valor numérico!")
        elemento = input(msg)
    return int(elemento)

# Verificação de valor entre 1 e 4    
def verificaValorCerto(num, msg): 
    while not(num > 0 and num < 5):
        print("Digite um valor entre 1 e 4!")
        num = verificaValorNumerico(msg)
    return num

# Início do jogo
def inicioDoJogo():
    # Cartas do jogo
    primeiraFileira = ['MAHINDRA RACING', 'JAGUAR TCS RACING', 'MASERATI MSG RACING', 'NISSAN FORMULA E TEAM']
    segundaFileira = ['JAGUAR TCS RACING', 'NEOM MCLAREN FORMULA E TEAM', 'DS PENSKE', 'MAHINDRA RACING']
    terceiraFileira = ['MASERATI MSG RACING', 'NISSAN FORMULA E TEAM', 'NEOM MCLAREN FORMULA E TEAM', 'DS PENSKE']
    quartaFileira = ['ENVISION RACING', 'ERT FORMULA E TEAM', 'ENVISION RACING', 'ERT FORMULA E TEAM']
    resposta = ['Continuar', 'Encerrar']
    
    # Tabela visual do jogo
    def imprimirTabela(cartas_descobertas):
        print("Tabela do Jogo:")
        print("-------------------------")
        for i in range(4):
            print("|", end=" ")
            for j in range(4):
                if (i,j) in cartas_descobertas:
                    carta = verificarCarta(i+1, j)
                    print(f"|{carta}|", end=" ")
                else:
                    print("|     ?     |", end=" ")
            print("|")
        print("-------------------------")

    # Declaração dos pares corretos e das cartas descobertas
    pares_corretos = 0
    cartas_descobertas = []
    imprimirTabela(cartas_descobertas)
    while pares_corretos < 8:  # Total de pares é 8
        print("\nEscolha a primeira carta!")
        # Input da primeira linha, verifica se é numérico e está entre 1 e 4
        linhaPE = verificaValorCerto(verificaValorNumerico("Digite a linha: "), "Digite a linha: ")
        # Input da primeira coluna, verifica se é numérico e está entre 1 e 4
        colunaPE = verificaValorCerto(verificaValorNumerico("Digite a coluna: "), "Digite a coluna: ")
        # Subtrai 1 da coluna, por causa do índice
        colunaFinalPE = colunaPE - 1
        # Chama a função para obter o valor da carta(elemento da lista)
        carta1 = verificarCarta(linhaPE, colunaFinalPE)
        print("Carta escolhida:", carta1)

        # Se a carta já foi descoberta, pede para escolher outra
        if (linhaPE - 1, colunaFinalPE) in cartas_descobertas:
            print("Esta carta já foi descoberta. Escolha novamente.")
            continue

        print("\nEscolha a segunda carta!")    
        # Input da segunda linha, verifica se é numérico e está entre 1 e 4
        linhaSE = verificaValorCerto(verificaValorNumerico("Digite a linha: "), "Digite a linha: ")
        # Input da segunda coluna, verifica se é numérico e está entre 1 e 4
        colunaSE = verificaValorCerto(verificaValorNumerico("Digite a coluna: "), "Digite a coluna: ")
        
        # Verifica se o usuário escolheu a mesma carta ou uma carta já descoberta
        while (linhaSE == linhaPE and colunaSE == colunaPE) or (linhaSE - 1, colunaSE - 1) in cartas_descobertas:
            print("Você escolheu a mesma carta ou uma carta já descoberta. Escolha a segunda carta novamente.")
            linhaSE = verificaValorCerto(verificaValorNumerico("Digite a linha: "), "Digite a linha: ")
            colunaSE = verificaValorCerto(verificaValorNumerico("Digite a coluna: "), "Digite a coluna: ")
        
        # Subtrai 1 da coluna, por causa do índice
        colunaFinalSE = colunaSE - 1
        # Chama a função para obter o valor da carta(elemento da lista)
        carta2 = verificarCarta(linhaSE, colunaFinalSE)
        print("Carta escolhida:", carta2)

        # Verifica se os pares são correspondentes
        if carta1 == carta2:
            print("Par correspondente encontrado!")
            print(carta1)
            pares_corretos += 1
            cartas_descobertas.append((linhaPE - 1, colunaFinalPE))
            cartas_descobertas.append((linhaSE - 1, colunaFinalSE))
        else:
            print("As cartas não formam um par correspondente.")
        imprimirTabela(cartas_descobertas)
    # Após o encontro de todos os pares
    print("\nParabéns! Você encontrou todos os pares correspondentes.")
    # Pede a resposta e obriga a digitar 'Continuar' ou 'Encerrar'
    continuar = forcaOpcao(resposta,"Deseja jogar novamente? (Continuar/Encerrar): ")
    if continuar == resposta[0]:
        inicioDoJogo()
    else:
        print("Obrigado por jogar!")

# Função para devolver o elemento(valor) da carta através da linha e coluna(índice)
def verificarCarta(linha, coluna):
    primeiraFileira = ['MAHINDRA', 'JAGUAR', 'MASERATI', 'NISSAN']
    segundaFileira = ['JAGUAR', 'MCLAREN', 'DS PENSKE', 'MAHINDRA']
    terceiraFileira = ['MASERATI', 'NISSAN', 'MCLAREN', 'DS PENSKE']
    quartaFileira = ['ENVISION', 'ERT', 'ENVISION', 'ERT']
    if linha == 1:
        return primeiraFileira[coluna]
    elif linha == 2:
        return segundaFileira[coluna]
    elif linha == 3:
        return terceiraFileira[coluna]
    else:
        return quartaFileira[coluna]

# Verifica se um elemento está presente em uma lista
def verificaIndice(lista,elemento):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == elemento:
            return True
    return False

# Forçar uma resposta presente em uma lista
def forcaOpcao(lista,msg):
    resp = input(msg)
    msgErro = '\n'.join(lista)
    while not verificaIndice(lista,resp):
        print(f"Opção inválida! Somente essas:\n{msgErro}")
        resp = input(msg)
    return resp

# Chamada para iniciar o jogo
print("Bem-vindo ao jogo da memória da Fórmula E!!")
inicioDoJogo()

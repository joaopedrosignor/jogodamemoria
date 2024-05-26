def tabela():
    print("_________________")
    print("|   |   |   |   |")
    print("_________________")
    print("|   |   |   |   |")
    print("_________________")
    print("|   |   |   |   |")
    print("_________________")
    print("|   |   |   |   |")
    print("_________________")

#Verificação de valor numérico    
def verificaValorNumerico(msg):
    elemento = input(msg)
    while not elemento.isnumeric():
        print("Digite um valor numérico!")
        elemento = input(msg)
    return int(elemento)

#Verificação de valor entre 1 e 4    
def verificaValorCerto(num,msg): 
    while not(num>0 and num<5):
        print("Digite um valor entre 1 e 4!")
        num = verificaValorNumerico(msg)
    return num

#Escolha de um espaço    
def escolha():
    print("Escolha um espaço!")
    #Input da linha, verifica se é numérico e está entre 1 e 4
    linha = verificaValorCerto(verificaValorNumerico("Digite a linha: "),"Digite a linha:")
    #Input da coluna, verifica se é numérico e está entre 1 e 4
    coluna = verificaValorCerto(verificaValorNumerico("Digite a coluna: "),"Digite a coluna: ")
    #Subtrai 1 da coluna, por causa do indíce
    coluna -= 1
    if linha == 1:
        return (primeiraFileira[coluna])
    elif linha ==2:
        return (segundaFileira[coluna])
    elif linha ==3:
        return (terceiraFileira[coluna])
    else:
        return (quartaFileira[coluna])
    
primeiraFileira = ['banana','maça','uva','mexerica']
segundaFileira = ['maça','pera','mamão','banana']
terceiraFileira = ['uva','mexerica','pera','mamão']
quartaFileira = ['melancia','morango','melancia','morango']
print("Bem vindo ao jogo da memória da Fórmula E!!")
print (escolha())
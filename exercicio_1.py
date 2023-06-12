# Exercício da Ficha de Trabalho 3

lista_perfis=[]
perfil1 = { 
        "Nome": "Eduardo",
        "Idade": 13,
        "Profissão": "bombeiro",
        "Hobbies": "natação",
        "Descrição": "é um gajo fixe"
        }

perfil2 = { 
        "Nome": "Cris",
        "Idade": 25,
        "Profissão": "policia",
        "Hobbies": "jogos",
        "Descrição": "é um tipo"
        }

lista_perfis.append(perfil1)
lista_perfis.append(perfil2)

def criar_perfil():
    
    nome = input("Insira o nome da persoagem: ")
    idade = input("Insira a idade da persoagem: ")
    profissao = input("Insira a profissão da persoagem: ")
    hobbies = input("Insira hobbies da persoagem: ")
    descricao = input("Insira uma breve descriçãon da sua nova personagem:\n")

    novo_perfil = {
        "Nome": nome,
        "Idade": idade,
        "Profissão": profissao,
        "Hobbies": hobbies,
        "Descrição": descricao
        }
      
    return novo_perfil 

def modificar_personagem(lista_dicionario):
    chave=str(input("Qual o nome da personagem que pretende mudar o perfil? "))
    i = 0

    while True:
        try:
            for campos,dados in lista_dicionario[i].items():
                if dados == chave:
                    compo_a_mudar = str(input("Qual o campo a mudar? "))
                    lista_dicionario[i][compo_a_mudar] = input("Qual o novo valor de {}? ".format(compo_a_mudar))
                    perfil_mudado = lista_dicionario[i]
                    break
            i = i + 1
        except:
            break
    return perfil_mudado

def visualizar_personagem(lista_dicionario):
    contador = 1
    for personagem in lista_dicionario:
        print("Personagem nº ", contador)
        print("Nome: ", personagem["Nome"])
        print("Idade: ", personagem["Idade"])
        print("Profissão: ", personagem["Profissão"]) 
        print("Hobbies: ", personagem["Hobbies"]) 
        print("Descrição: ", personagem["Descrição"])
        contador = contador +1
    return

def remover_personagem(lista_dicionario):
    chave=str(input("Qual o nome da personagem que pretende remover? "))
    i = 0
    while True:
        try:
            for campos, dados in lista_dicionario[i].items():
                if dados == chave:
                    lista_dicionario.pop(i)
            i = i + 1
        except:
            break
    return

def pesquisar_personagem(lista_dicionario):
    chave=str(input("Qual o nome da personagem que pretende mostrar o perfil? "))
    i = 0
    while True:
        try:
            for campos,dados in lista_dicionario[i].items():
                if dados == chave:
                    print("Nome: ", lista_dicionario[i]["Nome"])
                    print("Idade: ", lista_dicionario[i]["Idade"])
                    print("Profissão: ", lista_dicionario[i]["Profissão"]) 
                    print("Hobbies: ", lista_dicionario[i]["Hobbies"]) 
                    print("Descrição: ", lista_dicionario[i]["Descrição"])
                    break
            i = i + 1
        except:
            break
    return

while True:

    menu = int(input("\n1 - Adicionar um novo perfil de personagem;\n"
                    "2 - Modificar um perfil de personagem existente;\n"
                    "3 - Remover um perfil de personagem;\n"
                    "4 - Visualizar a lista completa de personagens;\n"
                    "5 - Pesquisar um personagem específico pelo nome;\n"
                    "6 - Sair.\n"
                    "Escolha uma opção: "))

    if menu == 1:
        novo_perfil = criar_perfil()
        lista_perfis.append(novo_perfil)
        print(lista_perfis)
        menu = 0
    
    elif menu == 2:
        modificar_personagem(lista_perfis)
        print(lista_perfis)
        menu = 0
    
    elif menu == 3:
        remover_personagem(lista_perfis)
        print(lista_perfis)
        menu = 0

    elif menu == 4:
        visualizar_personagem(lista_perfis)
        menu = 0

    elif menu == 5:
        pesquisar_personagem(lista_perfis)
        menu = 0
    
    elif menu == 6:
        break
    
    else:
        print("Opção inválida. Tente novamente.")
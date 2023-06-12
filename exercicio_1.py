# Exercício da Ficha de Trabalho 3
# código Python é um programa que permite criar, modificar, visualizar, remover e pesquisar perfis de personagens

lista_perfis=[] # lista vazia para conter os dicionários das personagens
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

lista_perfis.append(perfil1) # Adição dos perfis de perosnagens pré-definidos
lista_perfis.append(perfil2)

#Função criar_perfil(), que solicita ao usuário que insira informações sobre um novo personagem e cria um novo dicionário de perfil com essas informações.
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
    print("Novo perfil criado com sucesso.")
    print("Nome: ", novo_perfil["Nome"])
    print("Idade: ", novo_perfil["Idade"])
    print("Profissão: ", novo_perfil["Profissão"]) 
    print("Hobbies: ", novo_perfil["Hobbies"]) 
    print("Descrição: ", novo_perfil["Descrição"])      
    return
#Função modificar os campos permite modificar um perfil de personagem existente perguntado pelo Nome
def modificar_personagem(lista_dicionario):
    chave=str(input("Qual o nome da personagem que pretende mudar o perfil? "))
    
    for personagem in lista_dicionario:
        if personagem["Nome"] == chave:
            compo_a_mudar = str(input("Qual o campo a mudar? "))
            personagem[compo_a_mudar] = input("Qual o novo valor de {}? ".format(compo_a_mudar))
            print("A personagem {} foi alterada com sucesso.".format(chave))
    return
#Função que exibe na tela todos os perfis de personagens presentes na lista fornecida como argumento
def visualizar_personagem(lista_dicionario):
    contador = 1
    for personagem in lista_dicionario:
        print("\nPersonagem nº {}:".format(contador))
        print("Nome: ", personagem["Nome"])
        print("Idade: ", personagem["Idade"])
        print("Profissão: ", personagem["Profissão"]) 
        print("Hobbies: ", personagem["Hobbies"]) 
        print("Descrição: ", personagem["Descrição"])
        contador = contador +1
    return
# Função remover_personagem(), que remove um perfil de personagem da lista fornecida como argumento com base no nome do personagem.
def remover_personagem(lista_dicionario):
    chave=str(input("Qual o nome da personagem que pretende remover? "))
    i=0
    for personagem in lista_dicionario:
        if personagem["Nome"] == chave:
            lista_dicionario.pop(i)
            print("A perosnagem {} foi removida com sucesso.".format(chave))
        i=i+1
    return
# Função pesquisar_personagem(), que procura uma personagem específica pelo nome e exibe na tela todas as informações dessa personagem.
def pesquisar_personagem(lista_dicionario):
    chave=str(input("Qual o nome da personagem que pretende mostrar o perfil? "))
    for personagem in lista_dicionario:
        if personagem["Nome"] == chave:
            print("Nome: ", personagem["Nome"])
            print("Idade: ", personagem["Idade"])
            print("Profissão: ", personagem["Profissão"]) 
            print("Hobbies: ", personagem["Hobbies"]) 
            print("Descrição: ", personagem["Descrição"])
    return

# Neste loop While exibe-se o menu para o usuário e executa as ações correspondentes com base na opção selecionada. O loop continua indefinidamente até que a opção "6" seja escolhida
# o número selecionado corresponde a cada função deifinida anteriormente
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
        input("\nClique ENTER para voltar ao MENU.")
        menu = 0
    
    elif menu == 2:
        modificar_personagem(lista_perfis)
        input("\nClique ENTER para voltar ao MENU.")
        menu = 0
    
    elif menu == 3:
        remover_personagem(lista_perfis)
        input("\nClique ENTER para voltar ao MENU.")
        menu = 0

    elif menu == 4:
        visualizar_personagem(lista_perfis)
        input("\nClique ENTER para voltar ao MENU.")
        menu = 0

    elif menu == 5:
        pesquisar_personagem(lista_perfis)
        print("\nClique ENTER para voltar ao MENU.")
        menu = 0
    
    elif menu == 6:
        break
    
    else:
        print("Opção inválida. Tente novamente.")
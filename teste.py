
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

for personagem in lista_perfis:
    print(personagem)
    print("Nome: ", personagem["Nome"])
    print("Idade: ", personagem["Idade"])
    print("Profissão: ", personagem["Profissão"]) 
    print("Hobbies: ", personagem["Hobbies"]) 
    print("Descrição: ", personagem["Descrição"])
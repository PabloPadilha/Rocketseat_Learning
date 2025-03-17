import os

def main():
    contatos = [{"nome":"martin waldmuller", "telefone":"55912345678", "email":"cartografosDePlantao@Portugal.com", "favorito":True}, {"nome":"Fernando Pessoa", "telefone":"55987654321", "email":"LivroMensagem@Abril_colecoes.com", "favorito":False}]

    os.system("clear")
    while True:
        print("\nMENU DO GERENCIADOR DE TAREFAS:")
        print("1. Adicionar contato")
        print("2. Visualizar contatos")
        print("3. Atualizar contato")
        print("4. Marcar/Desmarcar contato como favorito")
        print("5. Visualizar lista de contatos favoritos")
        print("6. Apagar contato")
        print("7. Sair")

        escolha = input("Digite sua escolha: ")
        escolha = int(escolha)

        if escolha == 1:
            print("\n Vamos adicionar um contato:")
            nome = str(input("Digite o nome do contato: "))
            telefone = str(input("Digite o telefone do contato: "))
            email = str(input("Digite o email do contato: "))
            adicionar_contato(contatos, nome, telefone, email)
        
        elif escolha == 2:
            ver_contatos(contatos)
        
        elif escolha == 3:
            ver_contatos(contatos)
            indice = int(input("Digite o indice do contato que deseja atualizar: "))        
            atualizar_contatos(contatos, indice)
        
        elif escolha == 4:
            ver_contatos(contatos)
            indice = int(input("Digite o indice do contato que deseja marcar ou desmarcar dos favoritos: "))
            favoritar_contato(contatos, indice)
        
        elif escolha == 5:
            for i, contato in enumerate(contatos):
                if contato["favorito"] == True:
                    print(f"{i}º contato como favorito: [✓] Nome:{contato["nome"]} | Telefone:{contato["telefone"]} | Email:{contato["email"]}")                

        elif escolha == 6:        
            deletar_contato(contatos)

        elif escolha == 7:
            break

        elif escolha not in range(1,7):
            print("Numero incompatível com as escolhas disponíveis! Escolha novamente.")

        escolha = input("Digite sua escolha: ")
        escolha = int(escolha)

        if escolha == 1:
            print("\n Vamos adicionar um contato:")
            nome = str(input("Digite o nome do contato: "))
            telefone = str(input("Digite o telefone do contato: "))
            email = str(input("Digite o email do contato: "))
            adicionar_contato(contatos, nome, telefone, email)
        
        elif escolha == 2:
            ver_contatos(contatos)
        
        elif escolha == 3:
            ver_contatos(contatos)
            indice = int(input("Digite o indice do contato que deseja atualizar: "))        
            atualizar_contatos(contatos, indice)
        
        elif escolha == 4:
            ver_contatos(contatos)
            indice = int(input("Digite o indice do contato que deseja marcar ou desmarcar dos favoritos: "))
            favoritar_contato(contatos, indice)
        
        elif escolha == 5:
            visualizar_favoritos(contatos)               

        elif escolha == 6:        
            deletar_contato(contatos)

        elif escolha == 7:
            break

        elif escolha not in range(1,7):
            print("Numero incompatível com as escolhas disponíveis! Escolha novamente.")    


def adicionar_contato(contatos, nome, telefone, email):
    contato = {"nome":nome, "telefone":telefone, "email":email, "favorito":False}
    contatos.append(contato)
    os.system("clear")
    print("Contato adicionado com sucesso! \n")
    return

def ver_contatos(contatos):
    os.system("clear")
    print("Lista de contatos: ")
    for indice, contato in enumerate(contatos,start=1):
        if contato["favorito"]:    
            print(f"{indice}º  Nome:{contato["nome"]} | Telefone:{contato["telefone"]} | Email:{contato["email"]} | Favorito:[✓] \n")            
        else:
            print(f"{indice}º  Nome:{contato["nome"]} | Telefone:{contato["telefone"]} | Email:{contato["email"]} | Favorito:[ ] \n")
    return    

def atualizar_contatos(contatos, indice):
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        print(f"Contato :: {str(indice)} - {contatos[indice_ajustado]["nome"]} | {contatos[indice_ajustado]["telefone"]} | {contatos[indice_ajustado]["email"]} | {contatos[indice_ajustado]["favorito"]} ")    
        print("\n Qual informação deseja atualizar deste contato?")
        print("\n Opções de edição:")
        print("1 - Nome")
        print("2 - Telefone")
        print("3 - Email")
        print("4 - Marcacao como favorito")
        resposta_elemento_editavel = input()
        resposta_elemento_editavel = int(resposta_elemento_editavel)
        #while True:
        if resposta_elemento_editavel == 1:
                nome = str(input(f"Digite o novo nome do contato {contatos[indice_ajustado]["nome"]}: "))
                contatos[indice_ajustado]["nome"] = nome
                print("Informação ajustada")
        elif resposta_elemento_editavel == 2:
                telefone = str(input(f"Digite o novo nome do contato {contatos[indice_ajustado]["telefone"]}: "))
                contatos[indice_ajustado]["telefone"] = telefone
                print("Informação ajustada")
        elif resposta_elemento_editavel == 3:
                email = str(input(f"Digite o novo nome do contato {contatos[indice_ajustado]["email"]}: "))
                contatos[indice_ajustado]["email"] = email
                print("Informação ajustada")
        elif resposta_elemento_editavel == 4:
                favoritar_contato()    
        elif resposta_elemento_editavel not in range(1,4):
                print("Numero incompatível com as escolhas disponíveis! Escolha novamente.")             
    #else:
    #    print("Numero errado! Contato inexistente.")
    return

def favoritar_contato(contatos, indice):
    os.system("clear")
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        resposta = int(input("Deseja marcar ou desmarcar o contato como favorito? [1] Marcar | [2] Desmarcar: "))
        if resposta == 1:
            contatos[indice_ajustado]["favorito"] = True
            print(f"Contato :: {str(indice)}º - {contatos[indice_ajustado]["nome"]} | foi marcado como favorito!")
        elif resposta == 2:    
            print(f"Contato :: {str(indice)}º - {contatos[indice_ajustado]["nome"]} | foi desmarcado como favorito!")    
            contatos[indice_ajustado]["favorito"] = False
        elif resposta not in range(1,2):
            print("Numero incompatível com as escolhas disponíveis! Escolha novamente.")      
    return

def visualizar_favoritos(contatos):
    for i, contato in enumerate(contatos):
        if contato["favorito"] == True:
            print(f"{i}º contato como favorito: [✓] Nome:{contato["nome"]} | Telefone:{contato["telefone"]} | Email:{contato["email"]}")
    return             

def deletar_contato(contatos):
    os.system("clear")
    ver_contatos(contatos)
    indice = int(input("Digite o indice do contato que deseja apagar: "))
    if indice < 1 or indice > len(contatos):
        print("Índice inválido!")
        return
    while True:
        print(f"Tem certeza que deseja apagar o contato de {contatos[indice-1]['nome']}? [1] Sim | [2] Não")
        resposta = int(input()) 
        if resposta == 1: 
            contatos.remove(contatos[indice-1])
            os.system("clear")
            print("\n Contato apagado com sucesso!") 
            return
        elif resposta == 2:
            os.system("clear") 
            print("\n Operação cancelada") 
            return
        elif resposta not in range(1,3): 
            os.system("clear")
            pass
            
    




        
if __name__ == "__main__":
    main()        

def adicionar_contato(contatos, nome_contato, numero_telefone, email_contato):
    contato = {
        "contato": nome_contato,
        "telefone": numero_telefone,
        "email": email_contato,
        "favorito": False,
    }
    contatos.append(contato)
    return

def ver_lista_contatos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        nome_contato = contato["contato"]
        email_contato = contato["email"]
        numero_telefone = contato["telefone"]
        print(f"{indice}. [{status}] {nome_contato} | {email_contato} | {numero_telefone}")
    return

def editar_contato(contatos, indice_contato, novo_nome_contato, novo_numero_telefone, novo_email_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        contatos[indice_contato_ajustado]["telefone"] = novo_numero_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email_contato
    else:
        print("Indice de contato inválido.")    
    return

def marcar_contato_favorito(contatos, indice_contato):
    indice_contato_ajustado =  int(indice_contato) - 1
    if contatos[indice_contato_ajustado]["favorito"] == False:
        contatos[indice_contato_ajustado]["favorito"] = True  
        print(f"Contato {indice_contato} marcado como favorito.")
    else:
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {indice_contato} desmarcado como favorito.")
    return

def ver_contatos_favoritos(contatos):
    favoritos = [contato for contato in contatos if contato["favorito"]]
    for indice, contato in enumerate (favoritos, start=1):
        print(f"{indice}.[✓] {contato["contato"]} | {contato["telefone"]} | {contato["email"]}")
    return

contatos = []
while True:
    print("\nSeja Bem vindo a sua Agenda!\n")

    print("1. Adicionar um contato")
    print("2. Visualizar a lista de contatos")
    print("3. Editar um contato")
    print("4. Marcar/Desmarca um contato como favorito")
    print("5. Ver contatos favoritos")
    print("6. Deletar um contato\n")

    escolha = input("Digite o numero da opção desejada!\n")
    if escolha == "1":
        print("Adicionando contato: \n")
        nome_contato = input("Digite o nome do contato: \n")
        numero_telefone = input("Digite o numero de telefone do contato: \n")
        email_contato = input("Digite o email de contato: \n")
        adicionar_contato(contatos, nome_contato, numero_telefone, email_contato)
        print(f"Contato {nome_contato} adicionado com sucesso.\n")
    elif escolha == "2":
        print(f"Listas de contatos: \n")
        ver_lista_contatos(contatos)   
    elif escolha == "3":
        ver_lista_contatos(contatos)
        indice_contato=input("Digite o numero do indice que você deseja editar: ")
        novo_nome=input("Digite o novo nome: \n")
        novo_email=input(f"Digite um novo email: \n")
        novo_telefone=input(f"Digite um novo telefone: \n")
        print(f"Contato {indice_contato} atualizado para {novo_nome}, {novo_email}, {novo_telefone}")
        editar_contato(contatos, indice_contato, novo_nome, novo_email, novo_telefone)
    elif escolha == "4":
        ver_lista_contatos(contatos)
        indice_contato = input("Indique qual contato você deseja favoritar: ")
        marcar_contato_favorito(contatos, indice_contato)
    elif escolha == "5":
        print(f"Listas de contatos favoritos: \n")
        ver_contatos_favoritos(contatos)
    elif escolha == "6":
        break


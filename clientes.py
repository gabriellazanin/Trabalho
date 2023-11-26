from io_terminal import imprime_lista

nome_ficheiro_lista_de_clientes = "lista_de_clientes.pk"
    
def criar_novo_cliente():
    """Pedir os dados de um novo cliente

    :return: dicionario com o novo cliente, {"nome": <<nome>>, "nif": <<nif>>, ...}
    """     
     print ("Dados do novo cliente: ")
    
    nome = input("Nome: ")
    nascimento = input("Ano de nascimento: ")
    nif = input ("NIF: ")
    morada = input ("Morada: ")
    telemovel = input("Telemóvel: ")
    email = input ("E-mail: ")
    
    novocliente: {"Nome": nome, 
                  "Ano de nascimento: ": nascimento,
                  "Nif": nif, 
                  "Morada": morada, 
                  "Telemovel": telemovel, 
                  "Email": email}

    return novocliente

def imprime_lista_de_clientes(lista_de_clientes):
    if not lista_de_clientes:
        print("Nenhum cliente na lista.")
    else:
        for cliente in lista_de_clientes:
            print("\nNome: ", cliente["nome"])
            print("Nascimento: ", cliente["nascimento"])
            print("NIF: ", cliente["nif"])
            print("Morada: ", cliente["morada"])
            print("E-mail: ", cliente["email"])
            print("Telemovel: ", cliente["telemovel"])

    imprime_lista(cabecalho="Lista de Clintes", lista=lista_de_clientes)

  

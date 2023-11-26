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
                  "NIF": nif, 
                  "Morada": morada, 
                  "Telemóvel": telemovel, 
                  "E-mail": email}

    return novocliente

def imprime_lista_de_clientes(lista_de_clientes):
   
    for novo_cliente in lista_de_clientes:
        print novo_cliente

  

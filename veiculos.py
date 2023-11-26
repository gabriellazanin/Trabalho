from io_terminal import imprime_lista

nome_ficheiro_lista_de_veiculos = "lista_de_veiculos.pk"

def cria_novo_veiculo():
    
    print("Dados do novo veículo: ")            """Pede ao utilizador para introduzir um novo veiculo
                                                    :return: dicionario com um veiculo na forma
                                                    {"marca": <<marca>>, "matricula": <<matricula>>, ...}     """

    marca = input("Marca: ")
    matricula = input("Matricula: ").upper()
    ano = input("Ano: ")
    cor = input("Cor: ")
    
    
    veiculo = {"Marca: ": marca,
               "Matricula: ": matricula,
               "Ano: ": ano,
               "Cor: ": cor}

    return veiculo

def imprime_lista_de_veiculos(lista_de_veiculos):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de Veiculos", lista=lista_de_veiculos)
    

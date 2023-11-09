def cria_novo_veiculo():
    novoveiculo = "Insira "
    """Pede ao utilizador para introduzir um novo veiculo

    :return: dicionario com um veiculo na forma
        {"marca": <<marca>>, "matricula": <<matricula>>, ...}
    """

    marca = input("Marca: ")
    matricula = input("Matricula: ").upper()
    ano = input("Ano: ")
    cor = input("Cor: ")
    
    # TODO: Pedir o resto dos dados do veiculo, e não esquecer de os guardar no dicionario
    # ...

    veiculo = {"Marca: ": marca,
               "Matricula: ": matricula,
               "Ano: ": ano,
               "Cor: ": cor}

    return veiculo

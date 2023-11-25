from datetime import date

from io_terminal import imprime_lista, pergunta_id

nome_ficheiro_lista_de_faturas = "lista_de_faturas.pk"


def cria_nova_fatura(lista_de_clientes, lista_de_veiculos):
   
    id_cliente = pergunta_id(questao="Qual o id do cliente?", lista=lista_de_clientes, mostra_lista=True)
    id_veiculo = pergunta_id(questao="Qual o id do veiculo?", lista=lista_de_veiculos, mostra_lista=True)
    id_modelo = pergunta_id(questao= "Qual o modelo?", lista=lista_de_veiculos, mostra_lista=True)
    SMS = pergunta_id(questao= "Autoriza atualizações do veículo através de SMS? (S/N)", lista=lista_de_clientes, mostra_lista=True)
    
    fatura = {"Cliente: ": id_cliente,
              "Vecíulo: ": id_veiculo,
              "Modelo: ": id_modelo,
              "SMS: ": SMS, 
              "Data": date.today()}

    return fatura


def imprime_lista_de_faturas(lista_de_faturas):
    """TODO: documentação"""

    imprime_lista(cabecalho="Lista de Faturas", lista=lista_de_faturas)
    
    pass
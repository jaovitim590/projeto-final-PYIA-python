from datetime import date
from acoes.produtos import add_produto
from acoes.listar import listar
from acoes.listar_id_nome import listar_id
from acoes.remover import remover
from acoes.vendas import add_venda
from acoes.update import atualizar

class Estoque:
  def __init__(self):
    tabelas = ("produtos", "vendas")

  def adicionar_produto(self,nome: str, descricao: str, quantidade: int = 0, preco: float = 0):
    return add_produto(nome,descricao,quantidade,preco)
  
  def list(self,tabela:str):
    if tabela in tabelas:
      return listar(tabela)
    else:
      return "insira uma tabela valida!"

  def adicionar_venda(self):
    listar_id("produtos")
    try:
        id_produto = int(input("insira o ID do produto que deseja comprar: "))
        quantidade = int(input("insira a quantidade que deseja comprar: "))
        data_feita = date(input("insira a data da compra: (YYYY,M,D)"))
    except err:
      print("valores inseridos incorretamente!")
      break
    
    finally:
      return add_venda(id_produto, quantidade,data_feita)
  

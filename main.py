from datetime import date
from acoes.produtos import add_produto
from acoes.listar import listar
from acoes.listar_id_nome import listar_id
from acoes.remover import remover
from acoes.vendas import add_venda
from acoes.update import atualizar

class Estoque:
    def __init__(self):
        self.tabelas = ("produtos", "vendas")

    def adicionar_produto(self, nome: str, descricao: str, quantidade: int = 0, preco: float = 0):
        return add_produto(nome, descricao, quantidade, preco)

    def list(self, tabela: str):
        if tabela in self.tabelas:
            return listar(tabela)
        else:
            return "Insira uma tabela válida!"

    def adicionar_venda(self):
        listar_id("produtos")
        try:
            id_produto = int(input("Insira o ID do produto que deseja comprar: "))
            quantidade = int(input("Insira a quantidade que deseja comprar: "))
            ano, mes, dia = map(int, input("Insira a data da compra (YYYY,M,D): ").split(","))
            data_feita = date(ano, mes, dia)
        except Exception as err:
            print(f"❌ Valores inseridos incorretamente: {err}")
            return

        return add_venda(id_produto, quantidade, data_feita)

    def drop_produto(self, key: str, tabela: str):
        if tabela in self.tabelas:
            return remover(key, tabela)
        else:
            return "Insira uma tabela válida!"

    def atualizar_quantia(self, tabela: str):
      if tabela in self.tabelas:
            return atualizar(tabela)
      else:
            return "Insira uma tabela válida!"

loja = Estoque()
loja.atualizar_quantia("produtos")
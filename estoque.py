from datetime import date
from acoes.produtos import add_produto
from acoes.listar import listar
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
            return {"erro": "Insira uma tabela válida!"}

    def adicionar_venda(self, id_produto: int, quantidade: int, data_feita: date):
        return add_venda(id_produto, quantidade, data_feita)

    def drop_produto(self, key: str, tabela: str, produto_id: int, remover_vendas_associadas: bool = False):
        if tabela in self.tabelas:
            return remover(key, tabela, produto_id, remover_vendas_associadas)
        else:
            return {"erro": "Insira uma tabela válida!"}

    def atualizar_quantia(self, tabela: str, produto_id: int, nova_quantidade: int, confirmar: bool = False):
        if tabela in self.tabelas:
            return atualizar(tabela, produto_id, nova_quantidade, confirmar)
        else:
            return {"erro": "Insira uma tabela válida!"}

loja = Estoque()

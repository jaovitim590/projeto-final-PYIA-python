from flask import Flask, request, jsonify
from flask_cors import CORS
from acoes.update import atualizar
from acoes.remover import remover
from acoes.produtos import add_produto
from acoes.vendas import add_venda
from acoes.listar import listar
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Rota para listar produtos
@app.route('/listar/produtos', methods=['GET'])
def listar_produtos():
    resultados = listar("produtos")
    # Verifica se ocorreu algum erro (listar retorna dict com "erro" em falha)
    if isinstance(resultados, dict) and "erro" in resultados:
        return jsonify(resultados), 500
    return jsonify(resultados), 200

# Rota para adicionar produto
@app.route('/produto/adicionar', methods=['POST'])
def adicionar_produto():
    dados = request.get_json()
    nome = dados.get('nome')
    descricao = dados.get('descricao')
    quantidade = dados.get('quantidade', 0)
    preco = dados.get('preco', 0.0)

    if not isinstance(nome, str) or not isinstance(descricao, str):
        return jsonify({"erro": "Nome e descrição devem ser strings"}), 400
    if not (isinstance(quantidade, int) and isinstance(preco, (int, float))):
        return jsonify({"erro": "Quantidade deve ser inteiro e preço numérico"}), 400

    try:
        add_produto(nome, descricao, quantidade, preco)
        return jsonify({"msg": "Produto adicionado com sucesso"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Rota para adicionar venda
@app.route('/venda/adicionar', methods=['POST'])
def adicionar_venda():
    dados = request.get_json()
    id_produto = dados.get('id_produto')
    quantidade = dados.get('quantidade')
    data_str = dados.get('data')

    if not (isinstance(id_produto, int) and isinstance(quantidade, int) and isinstance(data_str, str)):
        return jsonify({"erro": "Parâmetros inválidos"}), 400

    try:
        data_venda = datetime.strptime(data_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"erro": "Formato de data inválido, use YYYY-MM-DD"}), 400

    try:
        add_venda(id_produto, quantidade, data_venda)
        return jsonify({"msg": "Venda registrada com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Rota para atualizar produto
@app.route('/produto/atualizar', methods=['PUT'])
def atualizar_produto():
    dados = request.get_json()
    produto_id = dados.get('id')
    nova_quantidade = dados.get('nova_quantidade')

    if not isinstance(produto_id, int) or not isinstance(nova_quantidade, int):
        return jsonify({"erro": "ID e nova_quantidade devem ser inteiros"}), 400

    try:
        sucesso = atualizar(produto_id, nova_quantidade)  
        if sucesso:
            return jsonify({"msg": "Produto atualizado com sucesso"}), 200
        else:
            return jsonify({"erro": "Produto não encontrado ou erro na atualização"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# Rota para remover produto
@app.route('/produto/remover', methods=['DELETE'])
def remover_produto():
    dados = request.get_json()
    produto_id = dados.get('id')
    chave = dados.get('chave')

    if not isinstance(produto_id, int) or not isinstance(chave, str):
        return jsonify({"erro": "ID deve ser inteiro e chave deve ser string"}), 400

    try:
        sucesso = remover(produto_id, chave)
        if sucesso:
            return jsonify({"msg": "Produto removido com sucesso"}), 200
        else:
            return jsonify({"erro": "Produto não encontrado, chave inválida ou erro na remoção"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

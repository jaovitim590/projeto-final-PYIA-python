from sql.db import get_db
from .listar_id_quantidade import listar_quantidade
import mysql.connector

def atualizar(tabela: str):
    tabelas_validas = ("produtos", "vendas")

    if tabela not in tabelas_validas:
        print("Tabela inválida")
        return

    listar_quantidade(tabela)

    try:
        produto_id = int(input("Escreva o ID do produto que deseja atualizar: "))
        
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(f"SELECT id, nome, quantidade FROM {tabela} WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if not resultado:
            print("❌ Produto não encontrado.")
            return

        print(f"Produto encontrado: ID: {resultado[0]}, Nome: {resultado[1]}, Quantidade atual: {resultado[2]}")
        res = input("Esse é o produto correto? (S/N): ")

        if res.strip().upper() == "S":
            try:
                nova_quantidade = int(input("Insira a nova quantidade: "))

                sql = "UPDATE produtos SET quantidade = %s WHERE id = %s"
                cursor.execute(sql, (nova_quantidade, produto_id))
                conn.commit()

                print("✅ Produto atualizado com sucesso!")

            except mysql.connector.Error as err:
                print(f"❌ Erro ao atualizar o produto: {err}")
        
        else:
            print("❌ Operação cancelada pelo usuário.")

    except ValueError:
        print("❌ ID inválido. Digite um número inteiro.")

    except mysql.connector.Error as err:
        print(f"❌ Erro de conexão ou SQL: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


from sql.db import get_db
from .listar_id_nome import listar_id
import mysql.connector

def remover(key: str, tabela: str):
    tabelas_validas = ("produtos", "vendas")

    if tabela not in tabelas_validas:
        print("Tabela inválida")
        return

    if key != "bolinho de tilapia":
        print("Chave inválida!")
        return

    listar_id(tabela)

    try:
        produto_id = int(input("Escreva o ID do produto que deseja remover: "))

        conn = get_db()
        cursor = conn.cursor()

        try:
            cursor.execute(f"DELETE FROM {tabela} WHERE id = %s", (produto_id,))
            conn.commit()
            print("✅ Produto deletado com sucesso!")

        except mysql.connector.errors.IntegrityError as e:
            print("⚠️ Existe uma venda associada a esse produto.")
            res = input("Deseja remover as vendas associadas? (S/N): ")
            if res.strip().upper() == 'S':
                cursor.execute("DELETE FROM vendas WHERE id_produto = %s", (produto_id,))
                cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
                conn.commit()
                print("✅ Produto e vendas associadas removidos com sucesso.")
            else:
                print("❌ Remoção cancelada.")

    except ValueError:
        print("❌ ID inválido. Digite um número inteiro.")

    except mysql.connector.Error as err:
        print(f"❌ Erro inesperado: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

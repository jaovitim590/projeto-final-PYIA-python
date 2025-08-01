from sql.db import get_db
import mysql.connector

def add_produto(nome: str, descricao: str, quantidade: int = 0, preco: float = 0):
    try:
        conn = get_db()
        cursor = conn.cursor()

        sql = """
            INSERT INTO produtos (nome, descricao, quantidade, preco)
            VALUES (%s, %s, %s, %s);
        """
        valores = (nome, descricao, quantidade, preco)

        cursor.execute(sql, valores)
        conn.commit()

        print("✅ Produto adicionado com sucesso!")

    except mysql.connector.Error as err:
        print(f"❌ Erro ao adicionar produto: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()


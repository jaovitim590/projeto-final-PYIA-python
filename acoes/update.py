from sql.db import get_db
import mysql.connector

def atualizar(produto_id: int, nova_quantidade: int):
    try:
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM produtos WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()

        if not resultado:
            return False 

        cursor.execute(
            "UPDATE produtos SET quantidade = %s WHERE id = %s",
            (nova_quantidade, produto_id)
        )
        conn.commit()
        return True

    except mysql.connector.Error as err:
        print(f"❌ Erro ao atualizar o produto: {err}")
        return False

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

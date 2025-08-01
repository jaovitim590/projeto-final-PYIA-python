from sql.db import get_db
import mysql.connector

def remover(produto_id: int, chave: str):
    CHAVE_CORRETA = "bolinho de tilapia"
    if chave != CHAVE_CORRETA:
        return False  # Chave inválida

    try:
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM produtos WHERE id = %s", (produto_id,))
        resultado = cursor.fetchone()
        if not resultado:
            return False  # Produto não encontrado

        try:
            cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
            conn.commit()
            return True

        except mysql.connector.errors.IntegrityError:
            # Produto está em vendas, precisa remover vendas associadas
            # Aqui você pode decidir se remove as vendas também automaticamente
            cursor.execute("DELETE FROM vendas WHERE id_produto = %s", (produto_id,))
            cursor.execute("DELETE FROM produtos WHERE id = %s", (produto_id,))
            conn.commit()
            return True

    except mysql.connector.Error as err:
        print(f"❌ Erro inesperado: {err}")
        return False

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

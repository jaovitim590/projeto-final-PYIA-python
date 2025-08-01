from sql.db import get_db
import mysql.connector
from datetime import date

def add_venda(id_produto: int, quantidade: int, data_feita: date):
    try:
        conn = get_db()
        cursor = conn.cursor()

        sql = """
        INSERT INTO vendas (id_produto, quantidade, data_feita)
        VALUES (%s, %s, %s);
        """
        valores = (id_produto, quantidade, data_feita)

        cursor.execute(sql, valores)
        conn.commit()

        return {
            "mensagem": "Venda registrada com sucesso!",
            "id_venda": cursor.lastrowid,
            "venda": {
                "id_produto": id_produto,
                "quantidade": quantidade,
                "data_feita": data_feita.isoformat()
            }
        }

    except mysql.connector.Error as err:
        return {"erro": f"Erro ao adicionar venda: {err}"}

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

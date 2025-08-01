from decimal import Decimal
from sql.db import get_db
import mysql.connector

def listar(tabela: str):
    tabelas_validas = ("produtos", "vendas")

    if tabela not in tabelas_validas:
        return {"erro": "Tabela inválida"}

    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        sql = f"SELECT * FROM {tabela}"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        
        for item in resultados:
            if 'preco' in item and isinstance(item['preco'], Decimal):
                item['preco'] = float(item['preco'])

        return resultados

    except mysql.connector.Error as err:
        return {"erro": f"Erro ao listar os dados: {err}"}

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

from sql.db import get_db
import mysql.connector

def listar_id(tabela: str):

    tabelas_validas = ("produtos", "vendas")

    if tabela not in tabelas_validas:
        print("Tabela inválida")
        return

    try:
        conn = get_db()
        cursor = conn.cursor()

        sql = f"""
          SELECT id, nome FROM {tabela} ORDER BY id ASC
        """

        cursor.execute(sql)
        resultados = cursor.fetchall()
        for linha in resultados:
            print(linha)

    except mysql.connector.Error as err:
        print(f"❌ Erro ao listar os conteudos da tabela {tabela}: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

from sql.db import get_db
import mysql.connector
from datetime import date

def add_venda(id_produto: int, quantidade: int, data_feita: date ):
  try:
    conn= get_db()
    cursor = conn.cursor()

    sql = """
    INSERT INTO vendas (id_produto, quantidade, data_feita)
    VALUES (%s, %s, %s);
    """
    
    valores = (id_produto, quantidade, data_feita)

    cursor.execute(sql, valores)
    conn.commit()

    print("✅ Venda adicionado com sucesso!")


  except mysql.connector.Error as err:
        print(f"❌ Erro ao adicionar venda: {err}")

  finally:
      if 'cursor' in locals():
          cursor.close()
      if 'conn' in locals() and conn.is_connected():
          conn.close()


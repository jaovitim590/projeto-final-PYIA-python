import mysql.connector

def get_db():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="in12345678",
            database="estoque"
        )

if __name__ == "__main__":
    conn = get_db()
    print("CONECTADO!")

    cursor = conn.cursor()

    with open('./sql/dump.sql', 'r') as file:
        sql = file.read()

    comandos = sql.split(";")
    
    for comando in comandos:
        comando = comando.strip()
        if comando:
            cursor.execute(comando)

    conn.commit()
    cursor.close()
    conn.close()

    print("DUMB EXECUTADO COM SUCESSO!")
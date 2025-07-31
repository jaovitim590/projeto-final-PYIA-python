import mysql.connector

def get_db():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="in12345678",
            database="estoque"
        )

if __name == "__main__":
    conn = get_db()
    print("CONECTADO!")

    cursor = conn.cursor()

    with open('./dump.sql', 'r') as file:
        sql = file.read()

    
import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="yamanote.proxy.rlwy.net",
        port=15391,
        user="root",
        password="xXWPHqoWAWEdQMXbBfJQsfJxSHyGCSGY",
        database="railway"
    )

if __name__ == "__main__":
    conn = get_db()
    print("✅ CONECTADO COM SUCESSO!")

    cursor = conn.cursor()

    with open('./sql/dump.sql', 'r', encoding='utf-8') as file:
        sql = file.read()

    for result in cursor.execute(sql, multi=True):
        pass

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ DUMP EXECUTADO COM SUCESSO!")

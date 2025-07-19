import mysql.connector

def save_to_db(doc_type, text):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="megabus12345",
            database="documentos_db"
        )
        cursor = conn.cursor()
        query = """
            INSERT INTO documentos (tipo_documento, texto)
            VALUES (%s, %s)
        """
        cursor.execute(query, (doc_type, text))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al guardar en MySQL: {e}")
        raise
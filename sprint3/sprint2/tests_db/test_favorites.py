import mysql.connector
from db_config import config

def test_add_favorite():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    # Insertamos un usuario primero si no existe
    cursor.execute("INSERT IGNORE INTO users (id, name, email, password) VALUES (1, 'Carlos', 'fav@example.com', 'test')")
    cursor.execute("INSERT INTO favorites (user_id, category, data) VALUES (%s, %s, %s)",
                   (1, 'event', '{"title": "Concierto Imagine Dragons", "date": "2025-10-10"}'))
    cnx.commit()
    print("Favorito añadido.")
    cursor.close()
    cnx.close()

def test_delete_favorite():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM favorites WHERE user_id = %s", (1,))
    cnx.commit()
    print("Favoritos eliminados.")
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    test_add_favorite()
    test_delete_favorite()

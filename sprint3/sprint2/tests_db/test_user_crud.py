import mysql.connector
from db_config import config

def test_add_user():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                   ("Carlos", "carlos@example.com", "1234"))
    cnx.commit()
    print("Usuario añadido.")
    cursor.close()
    cnx.close()

def test_update_user():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("UPDATE users SET email = %s WHERE name = %s", 
                   ("nuevo@example.com", "Carlos"))
    cnx.commit()
    print("Email actualizado.")
    cursor.close()
    cnx.close()

def test_delete_user():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM users WHERE name = %s", ("Carlos",))
    cnx.commit()
    print("Usuario eliminado.")
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    test_add_user()
    test_update_user()
    test_delete_user()

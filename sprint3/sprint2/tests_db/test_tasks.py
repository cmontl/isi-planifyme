import mysql.connector
from db_config import config

def test_add_task():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("INSERT IGNORE INTO users (id, name, email, password) VALUES (2, 'Lucía', 'lucia@example.com', 'abcd')")
    cursor.execute("INSERT INTO tasks (user_id, title, description) VALUES (%s, %s, %s)", 
                   (2, 'Comprar entradas', 'Comprar entradas para el cine'))
    cnx.commit()
    print("Tarea añadida.")
    cursor.close()
    cnx.close()

def test_mark_task_done():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("UPDATE tasks SET done = TRUE WHERE user_id = %s", (2,))
    cnx.commit()
    print("Tarea marcada como hecha.")
    cursor.close()
    cnx.close()

def test_delete_tasks():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM tasks WHERE user_id = %s", (2,))
    cnx.commit()
    print("Tareas eliminadas.")
    cursor.close()
    cnx.close()

if __name__ == "__main__":
    test_add_task()
    test_mark_task_done()
    test_delete_tasks()

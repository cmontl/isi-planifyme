import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="PlanifyMe2025!",
        database="planifyme"
    )

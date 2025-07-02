from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import mysql.connector
from config import DB_CONFIG
import requests

routes = Blueprint('routes', __name__)

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

@routes.route('/')
def index():
    return redirect(url_for('routes.login'))

@routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password)
            )
            db.commit()
            flash("Registro exitoso. Inicia sesión.", "success")
            return redirect(url_for('routes.login'))
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "danger")
        finally:
            cursor.close()
            db.close()

    return render_template('register.html')

@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s",
            (email, password)
        )
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            return redirect(url_for('routes.dashboard'))
        else:
            flash("Credenciales incorrectas.", "danger")

    return render_template('login.html')

def get_weather_data(city):
    try:
        
        r = requests.get(f"http://weather_service:5000/weather?city={city}")
        return r.json()  # ← aquí devolvemos directamente el JSON completo
    except Exception as e:
        print(f"❌ Error al obtener el clima: {e}")
        return None


@routes.route('/dashboard')
def dashboard():
    name = session.get('user_name', 'Usuario')
    city = "Madrid"

    weather = get_weather_data(city)

    try:
        r_movies = requests.get("http://movies_service:5000/movies")
        movies_data = r_movies.json()
        movies = movies_data.get("peliculas", [])
    except Exception as e:
        print(f"❌ Error al obtener películas: {e}")
        movies = None

    try:
        r_events = requests.get(f"http://events_service:5000/events?city={city}")
        events_data = r_events.json()
        events = events_data.get("events", [])
    except Exception as e:
        print(f"❌ Error al obtener eventos: {e}")
        events = None

    # 🔁 Recuperamos las tareas del usuario desde la base de datos
    user_tasks = []
    if 'user_id' in session:
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks WHERE user_id = %s ORDER BY created_at DESC", (session['user_id'],))
        user_tasks = cursor.fetchall()
        cursor.close()
        db.close()

    return render_template("dashboard.html", name=name, weather=weather, movies=movies, events=events, tasks=user_tasks)

@routes.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('routes.login'))

@routes.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if 'user_id' not in session:
        return redirect(url_for('routes.login'))

    db = get_db()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        if title:
            cursor.execute(
                "INSERT INTO tasks (user_id, title, description) VALUES (%s, %s, %s)",
                (session['user_id'], title, description)
            )
            db.commit()

    cursor.execute(
        "SELECT * FROM tasks WHERE user_id = %s ORDER BY created_at DESC",
        (session['user_id'],)
    )
    tasks = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template('tasks.html', tasks=tasks)

@routes.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('routes.login'))

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE id = %s AND user_id = %s",
        (task_id, session['user_id'])
    )
    db.commit()
    cursor.close()
    db.close()

    return redirect(url_for('routes.tasks'))

@routes.route('/tasks/complete/<int:task_id>', methods=['POST'])
def mark_done(task_id):
    if 'user_id' not in session:
        return redirect(url_for('routes.login'))

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE tasks SET completed = 1 WHERE id = %s AND user_id = %s",
        (task_id, session['user_id'])
    )
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('routes.tasks'))

@routes.route('/plans/save', methods=['POST'])
def save_plan():
    if 'user_id' not in session:
        return redirect(url_for('routes.login'))

    plan_type = request.form['plan_type'].strip()
    details = request.form['details'].strip()

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO tasks (user_id, title, description) VALUES (%s, %s, %s)",
        (session['user_id'], plan_type, details)
    )
    db.commit()
    cursor.close()
    db.close()

    flash("✅ Plan guardado como tarea.", "success")
    return redirect(url_for('routes.dashboard'))

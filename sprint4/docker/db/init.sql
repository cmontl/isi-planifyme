CREATE DATABASE IF NOT EXISTS planifyme;
USE planifyme;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);

-- Tabla de tareas
CREATE TABLE IF NOT EXISTS tasks (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255),
    description TEXT,
    done TINYINT(1) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed TINYINT(1) DEFAULT 0
);

-- Tabla de favoritos
CREATE TABLE IF NOT EXISTS favorites (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category ENUM('event', 'movie', 'weather'),
    data JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

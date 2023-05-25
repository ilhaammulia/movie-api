import sqlite3

conn = sqlite3.connect('dataFilm.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users(id VARCHAR(255), username VARCHAR(255) UNIQUE, password VARCHAR(255), api_key VARCHAR(255))')


cursor.execute('SELECT * FROM data_film')
movies = cursor.fetchall()
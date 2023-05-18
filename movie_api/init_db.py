import sqlite3
from uuid import uuid4

connection = sqlite3.connect('dataFilm.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (id VARCHAR(255) PRIMARY KEY, username VARCHAR(50) UNIQUE, password VARCHAR(255))')
cursor.execute('CREATE TABLE IF NOT EXISTS genres (id VARCHAR(60) PRIMARY KEY, name VARCHAR(60))')
cursor.execute('CREATE TABLE IF NOT EXISTS companies (id VARCHAR(255) PRIMARY KEY, name VARCHAR(255))')
cursor.execute('CREATE TABLE iF NOT EXISTS movies (id VARCHAR(255), title VARCHAR(255), release_date DATE, language VARCHAR(20), vote_average FLOAT, vote_count INT(20), popularity FLOAT, synopsis TEXT, budget INT(30), revenue INT(30), runtime INT(11), tagline VARCHAR(60))')
cursor.execute('CREATE TABLE IF NOT EXISTS movie_genres (movie_id VARCHAR(255), genre_id VARCHAR(60), FOREIGN KEY(movie_id) REFERENCES movies(id), FOREIGN KEY(genre_id) REFERENCES genres(id))')
cursor.execute('CREATE TABLE IF NOT EXISTS movie_companies (movie_id VARCHAR(255), company_id VARCHAR(255), FOREIGN KEY(movie_id) REFERENCES movies(id), FOREIGN KEY(company_id) REFERENCES companies(id))')
cursor.execute('CREATE TABLE IF NOT EXISTS api_keys (user_id VARCHAR(255), key VARCHAR(255), FOREIGN KEY(user_id) REFERENCES users(id))')
connection.commit()

# cursor.execute('SELECT * FROM data_film')
# movies = cursor.fetchall()

# for i, movie in enumerate(movies):
#     genres = []
#     companies = []
#     movie_id = str(uuid4())

#     for genre in eval(movie[3]):
#         genres.append({
#             'id': genre.lower(),
#             'name': genre.capitalize()
#         })
#     for company in eval(movie[10]):
#         companies.append({
#             'id': str(uuid4()),
#             'name': company
#         })

#     for genre in genres:
#         try:
#           cursor.execute('INSERT INTO genres VALUES (?, ?)', (genre['id'], genre['name'],))
#         except:
#             pass
#     connection.commit()
#     for company in companies:
#         try:
#           cursor.execute('INSERT INTO companies VALUES (?, ?)', (company['id'], company['name'],))
#         except Exception as e:
#             print(e)
#             pass
#     connection.commit()

#     try:
#         cursor.execute('INSERT INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (movie_id, movie[1], movie[2], movie[4], movie[5], movie[6], movie[7], movie[8], movie[9], movie[11], movie[12], movie[13],))
#         for genre in genres:
#             cursor.execute('INSERT INTO movie_genres VALUES (?, ?)', (movie_id, genre['id'],))
#         for company in companies:
#             cursor.execute('INSERT INTO movie_companies VALUES (?, ?)', (movie_id, company['id'],))
#     except Exception as e:
#         print(e)
#         pass
#     connection.commit()
#     print('Success', i, movie_id)
    
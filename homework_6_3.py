import sqlite3
conn = sqlite3.connect("my_database1.db")
cursor = conn.cursor()

cursor.execute('''      
CREATE TABLE IF NOT EXISTS songs (

id INTEGER PRIMARY KEY AUTOINCREMENT,
song_title TEXT,               
artist TEXT,               
album TEXT,               
year INTEGER                           
)                
''')

cursor.execute("INSERT INTO songs (song_title, artist, album, year) VALUES ('Too Comfortable', 'Future', 'High Off Life', 2020)")
cursor.execute("INSERT INTO songs (song_title, artist, album, year) VALUES ('HOUSTONFORNICATION', 'Travis Scott', 'Astroworld', 2018)")
cursor.execute("INSERT INTO songs (song_title, artist, album, year) VALUES ('Open Hearts', 'The Weeknd', 'Hurry Up Tomorrow', 2025)")
cursor.execute("INSERT INTO songs (song_title, artist, album, year) VALUES ('Blinding Lights', 'The Weeknd', 'After Hours', 2020)")

cursor.execute("SELECT artist FROM songs WHERE artist LIKE 'T%'")
print(cursor.fetchall())

conn.close()
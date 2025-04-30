import sqlite3
import csv


conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
''')

# Create tables
cur.executescript('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


filename = 'tracks.csv'

with open(filename, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip the header row

    for row in reader:
        if len(row) < 7:
            continue

        name = row[0]
        artist = row[1]
        album = row[2]
        genre = row[3]
        count = row[4]
        rating = row[5]
        length = row[6]

        if name == '' or artist == '' or album == '' or genre == '':
            continue

        
        cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES ( ? )', (artist,))
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
        artist_id = cur.fetchone()[0]

        cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES ( ? )', (genre,))
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
        genre_id = cur.fetchone()[0]

      
        cur.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )',
                    (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (name, album_id, genre_id, length, rating, count))

        conn.commit()

# Test query
sql = '''
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
AND Album.artist_id = Artist.id 
ORDER BY Artist.name LIMIT 3
'''

print("\nTrack\t\t\tArtist\t\tAlbum\t\t\tGenre")
print("-" * 70)
for row in cur.execute(sql):
    print(f"{row[0]:30} {row[1]:15} {row[2]:25} {row[3]}")

cur.close()
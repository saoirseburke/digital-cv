import streamlit as st
import sqlite3

conn = sqlite3.connect('album_collection') 
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS artists (
    artist_id INTEGER(10)  PRIMARY KEY,
    artist_name varchar(128)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS albums (
    album_id INTEGER(10) PRIMARY KEY,
    album_name varchar(256),
    date_of_release DATE 
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS songs (
    song_id INTEGER(10) PRIMARY KEY,
    song_name varchar(128),
    genre varchar(32),
    song_length FLOAT, 
    date_of_release DATE
	)
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS album_artist (
    album_id INTEGER(10) REFERENCES albums(album_id),
    artist_id INTEGER(10) REFERENCES artists(artist_id), 
    PRIMARY KEY(artist_id, album_id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS song_artist (
    song_id INTEGER(10) REFERENCES songs(song_id),
    artist_id INTEGER(10) REFERENCES artists(artist_id),
    PRIMARY KEY(song_id, artist_id)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS song_album (
    song_id INTEGER(10) REFERENCES songs(song_id),
    album_id INTEGER(10) REFERENCES albums(album_id),
    track_no INTEGER NOT NULL, 
    PRIMARY KEY(song_id, album_id),
    UNIQUE(album_id, track_no)
    )
''')


# inserting data

def insert_artist_data(artist_name):
    c.execute('INSERT INTO artists (artist_name) VALUES (?)', (artist_name,))
    conn.commit()

def insert_album_data(album_name, date_of_release):
    c.execute('INSERT INTO albums (album_name, date_of_release) VALUES (?, ?)', (album_name, date_of_release))
    conn.commit()

def insert_song_data(song_name, genre, song_length, date_of_release):
    c.execute('INSERT INTO songs (song_name, genre, song_length, date_of_release) VALUES (?, ?, ?, ?)', (song_name, genre, song_length, date_of_release))
    conn.commit()

def insert_album_artist_data(album_id, artist_id):
    c.execute('INSERT INTO album_artist (album_id, artist_id) VALUES (?, ?)', (album_id, artist_id))
    conn.commit()

def insert_song_artist_data(song_id, artist_id):
    c.execute('INSERT INTO song_artist (song_id, artist_id) VALUES (?, ?)', (song_id, artist_id))
    conn.commit()

def insert_song_album_data(song_id, album_id, track_no):
    c.execute('INSERT INTO song_album (song_id, album_id, track_no) VALUES (?, ?, ?)', (song_id, album_id, track_no))
    conn.commit()

st.title('SQL Album Database in Streamlit')

# Insert data through a form for artists
st.header('Insert Artist Data')
artist_name = st.text_input('Enter artist name:')
if st.button('Add Artist'):
    insert_artist_data(artist_name)
    st.success('Artist data added successfully!')

# Insert data through a form for albums
st.header('Insert Album Data')
album_name = st.text_input('Enter album name:')
date_of_release_album = st.date_input('Enter date of release (album)', key='album_date_input')
if st.button('Add Album'):
    insert_album_data(album_name, date_of_release_album)
    st.success('Album data added successfully!')

# Insert data through a form for songs
st.header('Insert Song Data')
song_name = st.text_input('Enter song name:')
genre = st.text_input('Enter genre:')
song_length = st.number_input('Enter song length:')
date_of_release_song = st.date_input('Enter date of release (song)', key='song_date_input')
if st.button('Add Song'):
    insert_song_data(song_name, genre, song_length, date_of_release_song)
    st.success('Song data added successfully!')


# Function to insert data into the artists table
def insert_artist_data(artist_name):
    c.execute('INSERT INTO artists (artist_name) VALUES (?)', (artist_name,))
    conn.commit()

# Function to query data from the artists table
def query_artist_data():
    c.execute('SELECT * FROM artists')
    return c.fetchall()

# ... (your existing insert data functions)

# Streamlit app
st.title('SQL Album Database in Streamlit')

# ... (your existing code for inserting data)

# Query and display data for artists
st.header('Query Artist Data')
artist_result = query_artist_data()
st.table(artist_result)

# Close the database connection when the app is done
conn.close()




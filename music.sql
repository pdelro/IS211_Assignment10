DROP TABLE IF EXISTS artists;
CREATE TABLE artists(
    artist_id INTEGER PRIMARY KEY,
    artist_name varchar NOT NULL
);

DROP TABLE IF EXISTS albums;
CREATE TABLE albums(
    album_id INTEGER PRIMARY KEY,
    album_title varchar NOT NULL,
    artist_id INTEGER NOT NULL
    FOREIGN KEY(artist_id) REFERENCES(artist_id)
);

DROP TABLE IF EXISTS songs;
CREATE TABLE songs(
    song_id INTEGER PRIMARY KEY,
    song_title varchar NOT NULL,
    track_number INTEGER NOT NULL,
    track_length INTEGER NOT NULL,
    album_id INTEGER NOT NULL
    FOREIGN KEY(album_id) REFERENCES(album_id)
);

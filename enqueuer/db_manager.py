# -*- coding: utf-8 -*-

import os
from settings import logging
import settings
import sqlite3
import json


def is_new_db():
    return not os.path.exists(settings.DB_FILE_NAME)


def create_db(conn):
    logging.info("Creating database")
    create_schema = """
    CREATE TABLE song_requests (
        id    TEXT PRIMARY KEY,
        date  DATETIME DEFAULT current_timestamp,
        json  TEXT,
        done  BOOLEAN DEFAULT 0
    );
    """
    conn.executescript(create_schema)


def insert_or_replace_data(tweet):
    is_new = is_new_db()
    with sqlite3.connect(settings.DB_FILE_NAME) as conn:
        if is_new: create_db(conn)
        conn.execute("INSERT OR REPLACE INTO song_requests (id, date, json) VALUES ('{}', '{}', '{}')".format(
            tweet['id'],
            tweet['date_created'],
            json.dumps(tweet).replace("'", "''")))


def save(tweet):
    insert_or_replace_data(tweet)


def delete_song(song_id):
    is_new = is_new_db()
    with sqlite3.connect(settings.DB_FILE_NAME) as conn:
        if is_new: create_db(conn)
        conn.execute("UPDATE song_requests SET done = 1 WHERE id = '{}'".format(song_id))
        return conn.total_changes


def get_active_songs(limit=50):
    if is_new_db():
        with sqlite3.connect(settings.DB_FILE_NAME) as conn:
            create_db(conn)
        return json.dumps({"message": "Database created. Wait for a few minutes and refresh again."})
    else:
        with sqlite3.connect(settings.DB_FILE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT json FROM song_requests WHERE done = 0 ORDER BY date DESC LIMIT {}".format(limit))
            rows = cursor.fetchall()

            if not rows:
                return json.loads("[]")

            rows = map(lambda x: json.loads(x[0].encode('utf-8', 'ignore')), rows)
            return json.dumps(rows)


def get_active_songs_greater_than(date, limit=50):
    if is_new_db():
        with sqlite3.connect(settings.DB_FILE_NAME) as conn:
            create_db(conn)
        return json.dumps({"message": "Database created. Wait for a few minutes and refresh again."})
    else:
        with sqlite3.connect(settings.DB_FILE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT json FROM song_requests WHERE done = 0 AND date >= '{}' ORDER BY date DESC LIMIT {}".format(
                    date, limit))
            rows = cursor.fetchall()

            if not rows:
                return json.loads("[]")

            rows = map(lambda x: json.loads(x[0].encode('utf-8', 'ignore')), rows)
            return json.dumps(rows)

# -*- coding: utf-8 -*-
import os 
import psycopg2
from yoyo import read_migrations, get_backend

from src.templates import db


def create_db(name=None):
    db_name = "mr"
    if name:
        db_name = name

    conn = psycopg2.connect(database="postgres", user='postgres', host='127.0.0.1', port='5432')
    conn.autocommit = True
    cursor = conn.cursor()
    sql = '''CREATE database ''' + db_name + ''' OWNER it''';
    cursor.execute(sql)
    print(f"Database {name} created successfully")
    conn.close()


def applay_migration(path, db):
    print(f"run migrations from path {path} to database {db}")
    backend = get_backend('postgres://it:it@localhost/'+db)
    migrations = read_migrations(path)
    backend.apply_migrations(backend.to_apply(migrations))
    print("completed")


def connect_db():
    conn = psycopg2.connect(database=db.DATABASE.value, user=db.USER.value, host=db.HOST.value, port=db.PORT.value) 
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def run_query(sql):
    conn = connect_db()
    conn.execute(sql)
    return conn.fetchall()


def run_update(sql):
    conn = connect_db()
    conn.execute(sql)
    

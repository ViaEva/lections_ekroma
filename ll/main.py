from tkinter import EXCEPTION
import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='test_db',
            user='emir',
            password='1'
            )
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    connect()

import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='file size' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS file (filename TEXT, size TEXT)")
    conn.commit()
    conn.close()

def insert(file_name, file_size):
    conn = psycopg2.connect("dbname='file size' user='postgres' password='postgres123' host='localhost' port='5432'")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO file VALUES(%s, %s)", (file_name, file_size))
    conn.commit()
    conn.close()

create_table()
import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ROUTINE (Id INTEGER PRIMARY KEY, date text, assignment text, exercise text, study text, diet text, pending text)")
    conn.commit()
    conn.close()

def insert(date, assignment, exercise, study, diet, pending):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES (NULL, ?,?,?,?,?,?)", (date, assignment, exercise, study, diet, pending))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine where id = ?", (id,))
    conn.commit()
    conn.close()

def search(date='', assignment='', exercise='', study='', diet='', pending=''):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine WHERE date=? OR assignment=? OR exercise=? study=? OR diet=? OR pending=? ",(date, assignment, exercise, study, diet, pending) )
    conn.commit()
    conn.close()

connect()

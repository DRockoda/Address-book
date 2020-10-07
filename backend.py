import sqlite3

def connect():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS address(id INTEGER PRIMARY KEY,name TEXT,email text,address text,ph_number number)")
    conn.commit()
    conn.close()

def insert(name,email,address,ph_number):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("insert into address values(NULL,?,?,?,?)",(name,email,address,ph_number))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("select * from address")
    row=cur.fetchall()
    conn.close()
    return row

def search(name="",email="",address="",ph_number=""):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("select * from address where name=? or email=? or address=? or ph_number=?",(name,email,address,ph_number))
    row=cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("delete from address where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,name,email,address,ph_number):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("update address set name=?,email=?,address=?,ph_number=? where id=?",(name,email,address,ph_number,id))
    conn.commit()
    conn.close()


connect()

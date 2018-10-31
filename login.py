import sqlite3
import getpass
def logScreen(conn,cursor):
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    cursor.execute('''
    SELECT *
    FROM Members
    WHERE Members.email = ?
    AND Members.pwd = ?;''',
    (username,password))
    result = cursor.fetchone()
    if result == None:
        print('Username and Password not found')
        return
    if result[3] == password:
        print('Welcome ' + result[1])
        return result[0],result[1]

def register(conn,cursor):
    username = input('Username: ')
    name = input('Name: ')
    phone = input('Phone: ')
    pwd = input('Password: ')
    try:
        cursor.execute('''
        INSERT INTO Members VALUES
        (?,?,?,?);''',
        (username,name,phone,pwd))
        conn.commit()
        return username,name
    except sqlite3.IntegrityError:
        print('Email already registered')
    return

import sqlite3
import getpass
def logScreen(conn,cursor):
    username = input('Username: ')
    password = getpass.getpass('Password: ')
    cursor.execute('''
    SELECT *
    FROM members
    WHERE members.email = ?
    AND members.pwd = ?;''',
    (username,password))
    result = cursor.fetchone()
    if result == None:
        print('Username and Password not found')
        return
    else:
        print('Welcome ' + result[1])
        cursor.execute('''
        SELECT inbox.sender, inbox.msgTimestamp, inbox.rno, inbox.content
        FROM inbox
        WHERE inbox.email = ?
        AND inbox.seen = 'n';''',
        (username,))
        msgs = cursor.fetchall()
        print('You have ' + str(len(msgs)) + ' messages.')
        for m in msg:
            print('Sender: ' + m[0])
            print('Time: ' + m[1])
            print('Ride number: ' +m[2])
            print('Message: ' + m[3])
        cursor.execute('''
        UPDATE inbox SET
        seen = 'y'
        WHERE inbox.email = ?
        AND inbox.seen = 'n';''',
        (username,))
        return result[0],result[1]

def register(conn,cursor):
    username = input('Username: ')
    name = input('Name: ')
    phone = input('Phone: ')
    pwd = input('Password: ')
    try:
        cursor.execute('''
        INSERT INTO members VALUES
        (?,?,?,?);''',
        (username,name,phone,pwd))
        conn.commit()
        return username,name
    except sqlite3.IntegrityError:
        print('Email already registered')
    return

def logScreen(conn,cursor):
    username = input('Username: ')
    password = input('Password: ')
    cursor.execute('''
    SELECT *
    FROM Members
    WHERE Members.email = ?
    AND Members.pwd = ?;''',
    (username,password))
    result = cursor.fetchone()
    print(result)

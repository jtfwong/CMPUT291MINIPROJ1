import location
def postRequest(user, conn, cursor):
    rdate = input('Date of ride(YYYY-DD-MM): ')
    pickup = location.findLocation(input('Starting location: '), conn, cursor)
    dropoff = location.findLocation(input('Destination location: '), conn, cursor)
    amount = input('Price per seat: $')
    print(rdate,pickup,dropoff,price)

    cursor.execute('SELECT COUNT(*) FROM Requests;')
    rid = cursor.fetchone()[0] + 1
    cursor.execute('INSERT INTO Requests VALUES(?,?,?,?,?,?);', rid, user, rdate, pickup, dropoff, amount)
    conn.commit()

def deleteRequest(user, conn ,cursor):
    print('Type back to exit or delete to remove request')
    cursor.execute('SELECT * FROM Requests WHERE Requests.email = user')
    rows = cursor.fetchone()
    print row.keys()
    requests = cursor fetchall()
    for each in requests:
        print each["rid"], each["user"], each["rdate"], each["pickup"], each["dropoff"], each["amount"]
    back = False
    while not back:
        user_input = input('JavinDrive: ')
        if user_input == 'back':
            back = True
        if user_input == 'delete':
            cancel = False
            while not cancel:
                rno = input('Enter rno to delete: ')
                confirm = ('Confirm delete?(yes/no): ')
                if confirm = 'no':
                    cancel = True
                if confirm = 'yes':
                    cursor.execute('DELETE FROM Requests WHERE Requests.rno = ?', rno)
                    cancel =


def searchRequest():
    return 1
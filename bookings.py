import location

def bookMembers(user, conn, cursor):
    return 1

def cancelBook():
    print('Type back to exit or cancel to remove booking')
    cursor.execute('SELECT * FROM bookings WHERE bookings.email = ?' (user))
    bookings = cursor.fetchall()
    for each in bookings:
        print(each["bno"], each["email"], each["rno"], each["cost"], each["seats"], each["pickup"], each["dropoff"])
    back = False
    while not back:
        user_input = input('JavinDrive: ')
        if user_input == 'back':
            back = True
        if user_input == 'cancel':
            cancel = False
            while not cancel:
                rno = input('Enter bno to delete: ')
                confirm = ('Confirm delete?(yes/no): ')
                if confirm == 'no':
                    cancel = True
                if confirm == 'yes':
                    cursor.execute('DELETE FROM bookings WHERE bookings.bno = ?', (bno))
                    conn.commit()
                    cancel = True
            back = True
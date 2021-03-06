import location

def bookMembers(user, conn, cursor):
    cursor.execute('SELECT * FROM rides;')
    rides = cursor.fetchall()
    page = 0
    while page*5 < len(rides):
        print("Enter 'book' to book a ride")
        print('Rides: ')
        for i in range(0,min(5,len(rides)-page*5)):
            print(i+1,rides[i+page*5])
        print("Enter 'more options' to view more rides")
        choice = None
        try:
            choice = input('Choice: ')
            if choice == 'book':
                email = input("Enter member's email: ")
                seats = input('Enter number of seats to book: ')
                cost = input('Cost per seat: $')
                pickup = input('Starting location code: ')
                dropoff = input('Destination location code: ')
                cursor.execute('''SELECT rno FROM rides
                                  WHERE driver = ?
                                  AND price = ?
                                  AND src = ?
                                  AND dest = ?;''', (email, cost, pickup ,dropoff,))
                rno = cursor.fetchone()
                cursor.execute('SELECT COUNT(*) FROM bookings;')
                bno = cursor.fetchone()[0] + 1
                cursor.execute('INSERT INTO bookings VALUES(?,?,?,?,?,?,?);', (bno, email, rno[0], cost, seats, pickup, dropoff,))
                content = 'Booking for '+str(rno)+' has been confirmed'
                cursor.execute("INSERT INTO inbox VALUES(?,datetime('now'),?,?,?,'n');", (email, user, content, rno[0],))
                print('Booking confirmed')
                conn.commit()
                break
            elif choice == 'more options':
                page += 1
            else:
                print('Invalid choice, please choose from selection')
        except:
            print('Not a valid input, please enter a ride')
    if rides == None:
        print('No rides found')
        return

def cancelBook(user, conn, cursor):
    print('Type back to exit or cancel to remove booking')
    cursor.execute('SELECT * FROM bookings WHERE bookings.email = ?;', (user,))
    bookings = cursor.fetchall()
    print(bookings)
    back = False
    while not back:
        user_input = input('JavinDrive: ')
        if user_input == 'back':
            back = True
        if user_input == 'cancel':
            cancel = False
            while not cancel:
                bno = input('Enter bno to delete: ')
                confirm = input('Confirm delete?(yes/no): ')
                if confirm == 'no':
                    cancel = True
                if confirm == 'yes':
                    cursor.execute('SELECT * FROM bookings WHERE bookings.bno = ?;',(bno,))
                    toDelete = cursor.fetchone()
                    content = 'Booking has been cancelled'
                    cursor.execute("INSERT INTO inbox VALUES(?,datetime('now'),?,?,?,'n');",(toDelete[1], user, content, toDelete[2],))
                    cursor.execute('DELETE FROM bookings WHERE bookings.bno = ?;', (bno,))
                    conn.commit()
                    cancel = True
        back = True
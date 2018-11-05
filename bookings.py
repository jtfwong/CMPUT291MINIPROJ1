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
                print('test 1')
                cursor.execute('''SELECT rno FROM rides
                                  WHERE driver = ?
                                  AND price = ?
                                  AND src = ?
                                  AND dest = ?;''', (email, cost, pickup ,dropoff,))
                print('test 2')
                rno = cursor.fetchone()
                print('test 3')
                print(rno)
                cursor.execute('SELECT COUNT(*) FROM bookings;')
                print('test 4')
                bno = cursor.fetchone()[0] + 1
                print(rno)
                print(bno)
                print('test 5')
                cursor.execute('INSERT INTO bookings VALUES(?,?,?,?,?,?,?);', (bno, email, rno, cost, seats, pickup, dropoff,))
                print('test 6')
                content = print('Booking has been confirmed')
                print('test 7')
                cursor.execute("INSERT INTO inbox VALUES(?,datetime('now'),?,?,?,'n');", (email, user, content, rno,))
                print('test 8')
                conn.commit()
                print('test 9')
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
    cursor.execute('SELECT * FROM bookings WHERE bookings.email = ?;', (user))
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
                    cursor.execute('SELECT * FROM bookings WHERE bookings.bno = ?;'(bno))
                    toDelete = cursor.fetchone()
                    content = print('Booking has been cancelled')
                    cursor.execute("INSERT INTO inbox VALUES(?,datetime('now'),?,?,?,'n');"(toDelete[1], user, content, toDelete[2],))
                    cursor.execute('DELETE FROM bookings WHERE bookings.bno = ?;', (bno,))
                    conn.commit()
                    print('Booking cancelled')
                    cancel = True
        back = True
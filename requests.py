import location
def postRequest(user, conn, cursor):
    rdate = input('Date of ride(YYYY-DD-MM): ')
    pickup = location.findLocation(input('Starting location: '), conn, cursor)
    dropoff = location.findLocation(input('Destination location: '), conn, cursor)
    amount = input('Price per seat: $')
    print(rdate,pickup,dropoff,price)

    cursor.execute('SELECT COUNT(*) FROM requests;')
    rid = cursor.fetchone()[0] + 1
    cursor.execute('INSERT INTO requests VALUES(?,?,?,?,?,?);', (rid, user, rdate, pickup, dropoff, amount))
    conn.commit()

def deleteRequest(user, conn ,cursor):
    print('Type back to exit or delete to remove request')
    cursor.execute('SELECT * FROM requests WHERE requests.email = ?' (user))
    requests = cursor.fetchall()
    for each in requests:
        print(each["rid"], each["user"], each["rdate"], each["pickup"], each["dropoff"], each["amount"])
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
                if confirm == 'no':
                    cancel = True
                if confirm == 'yes':
                    cursor.execute('DELETE FROM requests WHERE requests.rno = ?', (rno))
                    cancel = True
            back = True


def searchRequest():
    search = location.findLocation(input('Search location keyword: '), conn, cursor)
    print('Type back to exit or select to take request')
    cursor.execute('SELECT * FROM requests WHERE requests.pickup = ?'(search))
    requests = cursor.fetchall()
    page = 0
    while page*5 < len(requests):
        print('Requests: ')
        for i in range(0,min(5,len(requests)-page*5)):
            print(i+1,requests[i+page*5])
        print(6, 'More options')
        choice = None
        try:
            choice = int(input('Choice: '))
            if choice >= 1 and choice <= 5:
                selected = requests[choice+page*5-1]
            elif choice == 6:
                page += 1
            else:
                print('Invalid choice, please choose from selection')
        except:
            print('Not a valid input, please enter a request')
    if requests == None:
        print('No requests found with keyword. Please try again')
        search = location.findLocation(input('Search location keyword: '), conn, cursor)
    content = input('Enter message to poster: ')
    cursor.execute("INSERT INTO inbox VALUES(?,datetime('now'),?,?,?,?);"(selected(email), user, content, selected[rid], 0))
    conn.commit()
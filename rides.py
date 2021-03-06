import location
def offerRide(user, conn, cursor):
    rdate = input('Date of ride(YYYY-DD-MM): ')
    seats = input('Number of seats: ')
    price = input('Price per seat: $')
    lugDesc = input('Luggage Description: ')
    src = location.findLocation(input('Starting location: '), conn, cursor)
    dest = location.findLocation(input('Destination location: '), conn, cursor)
    print(rdate,seats,price,src,dest)
    pick_car = False
    while pick_car == False:
        cno = input('Car number being used(optional): ')
        if cno == '':
            cno = None
            pick_car = True
        else:
            try:
                cno = int(cno)
                cursor.execute('SELECT * FROM cars WHERE cars.cno = ? AND cars.owner = ?;',
                (cno,user))
                car = cursor.fetchone()
                print(car)
                if car != None:
                    pick_car = True
                else:
                    print('Invalid. Car number does not exist or car is owned by another user. Please try again.')
            except:
                print('Invalid. Please enter a number or press enter if you want to leave it empty.')
    pick_enroute = False
    while pick_enroute == False:
        num_en = input('Number of enroute locations(optional): ')
        if num_en == '':
            num_en = 0
            pick_enroute = True
        else:
            try:
                num_en = int(num_en)
                pick_enroute = True
            except:
                print('Invalid. Please enter a number or press enter to select 0.')
    en_loc = list()
    for i in range(0,int(num_en)):
        en_loc.append(location.findLocation(input('Enroute location '+str(i)+': '), conn, cursor))
    cursor.execute('SELECT COUNT(*) FROM rides;')
    rno = cursor.fetchone()[0] + 1
    cursor.execute('INSERT INTO rides VALUES(?,?,?,?,?,?,?,?,?);',
    (rno, price, rdate, seats, lugDesc, src[0], dest[0], user, cno))
    conn.commit()

def searchRide(user, conn, cursor):
    numkey = None
    while numkey == None:
        try:
            user_input = int(input('Number of keyword(s) (1-3): '))
            if user_input >=1 and user_input<=3:
                numkey = user_input
            else:
                print('Invalid number, please enter a number from 1-3.')
        except:
            print('Invalid input, please enter a number from 1-3.')
    keywords = list()
    for i in range(0,numkey):
        keywords.append(input('Keyword ' + str(i) + ': '))
    locations = list()
    for k in keywords:
        cursor.execute('''
        SELECT locations.lcode
        FROM locations
        WHERE locations.lcode = ?
        OR locations.city LIKE ?
        OR locations.prov LIKE ?
        OR locations.address LIKE ?;''',
        (k,'%'+k+'%','%'+k+'%','%'+k+'%'))
        lcodes = cursor.fetchall()
        for l in lcodes:
            if l not in locations:
                locations.append(l)
    rides = list()
    for l in locations:
        cursor.execute('''
        SELECT *
        FROM rides
        LEFT JOIN enroute ON enroute.rno = rides.rno
        LEFT JOIN cars ON cars.cno = rides.cno
        WHERE rides.src = ?
        OR rides.dest = ?
        OR enroute.lcode = ?;''',
        (l[0],l[0],l[0]))
        test = cursor.fetchall()
        for t in test:
            if t not in rides:
                rides.append(t)

    page = 0
    while page*5 < len(rides):
        print('Rides: ')
        print('(Ride no., Price, Date, Seats, Luggage Description, Pickup lcode, Dropoff lcode, Driver, Car number, Car info)')
        for i in range(0,min(5,len(rides)-page*5)):
            print(i+1,rides[i+page*5])
        print(6, 'More options')
        choice = None
        try:
            choice = int(input('Choice: '))
            if choice >= 1 and choice <= 5:
                selected = rides[choice+page*5-1]
                content = input('Enter message to poster: ')
                cursor.execute("INSERT INTO inbox VALUES(?,datetime('now'),?,?,?,'n');", (selected[7], user, content, selected[0],))
                print('Message sent')
                conn.commit()
                break
            elif choice == 6:
                page += 1
            else:
                print('Invalid choice, please choose from selection')
        except:
            print('Not a valid input, please enter a ride')
    if rides == None:
        print('No rides found with keyword. Please try again')

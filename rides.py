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
    cursor.execute('INSERT INTO rides VALUES(?,?,?,?,?,?,?,?,?)',
    (rno, price, rdate, seats, lugDesc, src[0], dest[0], user, cno))
    conn.commit()

def searchRide():
    return 1

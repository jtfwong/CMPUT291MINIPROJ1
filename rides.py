import location
def offerRide(user, conn, cursor):
    rdate = input('Date of ride(YYYY-DD-MM): ')
    seats = input('Number of seats: ')
    price = input('Price per seat: $')
    lugDesc = input('Luggage Description: ')
    src = location.findLocation(input('Starting location: '), conn, cursor)
    dest = location.findLocation(input('Destination location: '), conn, cursor)
    print(rdate,seats,price,src,dest)
    cno = input('Car number being used(optional): ')
    if cno == '':
        cno = None
    num_en = input('Number of enroute locations(optional): ')
    if num_en == '':
        num_en = 0
    en_loc = list()
    for i in range(0,int(num_en)):
        en_loc.append(location.findLocation(input('Enroute location'+str(i)), conn, cursor))
    cursor.execute('SELECT COUNT(*) FROM Rides;')
    rno = cursor.fetchone()[0] + 1
    cursor.execute('INSERT INTO Rides VALUES(?,?,timefstr(?),?,?,?,?,?,?)',
    (rno, price, rdate, seats, lugDesc, src[0], dest[0], user, cno))
    conn.commit()

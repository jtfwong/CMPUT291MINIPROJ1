def findLocation(lcode,conn,cursor):
    cursor.execute('''
    SELECT *
    FROM locations
    WHERE locations.lcode = ?;''',
    (lcode,))
    location = cursor.fetchone()
    if location != None:
        return location
    else:
        cursor.execute('''
        SELECT *
        FROM locations
        WHERE locations.city LIKE ?
        UNION
        SELECT *
        FROM locations
        WHERE locations.prov LIKE ?
        UNION
        SELECT *
        FROM locations
        WHERE locations.lcode LIKE ?
        UNION
        SELECT *
        FROM locations
        WHERE locations.address LIKE ?;''',
        ('%'+lcode+'%','%'+lcode+'%','%'+lcode+'%','%'+lcode+'%'))
        locations = cursor.fetchall()
        page = 0
        while page*5 < len(locations):
            print('Valid locations: ')
            for i in range(0,min(5,len(locations)-page*5)):
                print(i+1,locations[i+page*5])
            print(6, 'More options')
            choice = None
            try:
                choice = int(input('Choice: '))
                if choice >= 1 and choice <= 5:
                    return locations[choice+page*5-1]
                elif choice == 6:
                    page += 1
                else:
                    print('Invalid choice, please choose from selection')
            except:
                print('Not a valid input, please enter a location')
        if location == None:
            print('No locations found with keyword. Please try again')
            return findLocation(input('Location: '),conn,cursor)
def rideLocationSearch(lcode,conn,cursor):
    return

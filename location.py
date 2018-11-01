def findLocation(lcode,conn,cursor):
    cursor.execute('''
    SELECT *
    FROM Locations
    WHERE Locations.lcode = ?;''',
    (lcode,))
    location = cursor.fetchone()
    if location != None:
        return location
    else:
        cursor.execute('''
        SELECT *
        FROM Locations
        WHERE Locations.city LIKE ?
        UNION
        SELECT *
        FROM Locations
        WHERE Locations.prov LIKE ?
        UNION
        SELECT *
        FROM Locations
        WHERE Locations.address LIKE ?;''',
        ('%'+lcode+'%','%'+lcode+'%','%'+lcode+'%'))
        locations = cursor.fetchall()
        page = 0
        while page*5 < len(locations):
            for i in range(0,min(5,len(locations)-page*5)):
                print(i+1,locations[i+page*5])
            print(6, 'More options')
            choice = None
            while choice == None:
                try:
                    choice = int(input('Choice: '))
                except:
                    print('Not a valid input, please enter a number')
            if choice >= 1 and choice <= 5:
                return locations[choice+page*5-1]
            elif choice == 6:
                page += 1
            else:
                print('Invalid choice, please choose from selection')

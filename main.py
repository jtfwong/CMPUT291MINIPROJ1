import sqlite3
import login
import menu
import location
import rides
import requests
import bookings

class JavinDrive():
    def __init__(self):
        #Stuff to initialize
        self.user = None
        self.menu = menu.Menu()

        self.conn = sqlite3.connect('./JavinDrive.db')
        self.cursor = self.conn.cursor()
        self.cursor.executescript('''
        PRAGMA foreign_keys = ON;

        create table if not exists members(
        email char(15),
        name char(20),
        phone char(12),
        pwd char(6),
        primary key (email));

        create table if not exists cars(
        cno int,
        make char(12),
        model char(12),
        year int,
        seats int,
        owner char(15),
        primary key(cno),
        foreign key (owner) references members
        );

        create table if not exists locations(
        lcode char(5),
        city char(16),
        prov char(16),
        address char(16),
        primary key (lcode)
        );

        create table if not exists rides(
        rno int,
        price int,
        rdate date,
        seats int,
        lugDesc char(10),
        src char(5),
        dest char(5),
        driver char(15),
        cno int,
        primary key (rno),
        foreign key (src) references locations,
        foreign key (dest) references locations,
        foreign key (driver) references members,
        foreign key (cno) references cars
        );

        create table if not exists bookings(
        bno int,
        email char(15),
        rno int,
        cost int,
        seats int,
        pickup char(5),
        dropoff char(5),
        primary key (bno),
        foreign key (rno) references rides,
        foreign key (pickup) references locations,
        foreign key (dropoff) references locations
        );

        create table if not exists enroute(
        rno int,
        lcode char(5),
        primary key (rno,lcode),
        foreign key (rno) references rides,
        foreign key (lcode) references locations
        );

        create table if not exists requests(
        rid int,
        email char(15),
        rdate date,
        pickup char(5),
        dropoff char(5),
        amount int,
        primary key (rid),
        foreign key (email) references members,
        foreign key (pickup) references locations,
        foreign key (dropoff) references locations
        );

        create table if not exists inbox(
        email char(15),
        msgTimestamp date,
        sender char(15),
        content text,
        rno int,
        seen char(1),
        primary key (email,msgTimestamp),
        foreign key (email) references members,
        foreign key (sender) references members,
        foreign key (rno) references rides
        );
        ''')
        self.conn.commit()

    def app_loop(self):
        Exit = False
        print(
        '''Hello, Welcome to JavinDrive.\nFor assistance please type help into the command''')
        while not Exit:
            user_input = input('JavinDrive: ')
            if user_input == 'help':
                print('help,quit,login,register,logout')
            if user_input == 'quit':
                Exit = True
            if user_input == 'login':
                if self.user != None:
                    print(self.user + ' is logged on already.')
                else:
                    try:
                        self.user,self.name = login.logScreen(self.conn,self.cursor)
                    except:
                        pass
            if user_input == 'register':
                if self.user == None:
                    try:
                        self.user,self.name = login.register(self.conn,self.cursor)
                    except:
                        pass
                else:
                    print(self.user + ' is logged on already.')
            if user_input == 'logout':
                self.user = None
                self.name = None
                print('Logged out')
            if user_input == 'menu':
                self.menu.showMenu()
            if user_input == 'search':
                lcode = input('Location: ').lower()
                print(location.findLocation(lcode,self.conn,self.cursor))
            if user_input == 'offer ride':
                rides.offerRide(self.user,self.conn,self.cursor)
            if user_input == 'search ride':
                rides.searchRide(self.user,self.conn,self.cursor)
            if user_input == 'post request':
                requests.postRequest(self.user,self.conn,self.cursor)
            if user_input == 'delete requests':
                requests.deleteRequest(self.user,self.conn,self.cursor)
            if user_input == 'search requests':
                requests.searchRequest(self.user,self.conn,self.cursor)
            if user_input == 'book members':
                bookings.bookMembers(self.user,self.conn,self.cursor)
            if user_input == 'cancel bookings':
                bookings.cancelBook(self.user,self.conn,self.cursor)

if __name__ == "__main__":
    app = JavinDrive()
    app.app_loop()

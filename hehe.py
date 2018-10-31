import sqlite3
import login

class JavinDrive():
    def __init__(self):
        #Stuff to initialize
        self.login = False
        self.user = None
        self.name = None

        self.conn = sqlite3.connect('./JavinDrive.db')
        self.cursor = self.conn.cursor()
        self.cursor.executescript('''
        PRAGMA foreign_keys = ON;

        create table if not exists Members(
        email char(28),
        name char(28),
        phone int,
        pwd char(28),
        primary key (email));

        create table if not exists Cars(
        cno int,
        make char(28),
        model char(28),
        year int,
        seats int,
        owner char(28),
        primary key(cno),
        foreign key (owner) references Members
        );

        create table if not exists Locations(
        lcode char(5),
        city char(20),
        prov char(20),
        address char(100),
        primary key (lcode)
        );

        create table if not exists Rides(
        rno int,
        price int,
        rdate date,
        seats int,
        lugDesc char(20),
        src char(5),
        dest char(5),
        driver char(28),
        cno int,
        primary key (rno),
        foreign key (src) references Locations,
        foreign key (dest) references Locations,
        foreign key (driver) references Members,
        foreign key (cno) references Cars
        );

        create table if not exists Bookings(
        bno int,
        email char(28),
        rno int,
        cost int,
        seats int,
        pickup char(5),
        dropoff char(5),
        primary key (bno),
        foreign key (rno) references Rides,
        foreign key (pickup) references Locations,
        foreign key (dropoff) references Locations
        );

        create table if not exists Enroute(
        rno int,
        lcode char(5),
        primary key (rno,lcode),
        foreign key (rno) references Rides,
        foreign key (lcode) references Locations
        );

        create table if not exists Requests(
        rid int,
        email char(28),
        rdate date,
        pickup char(5),
        dropoff char(5),
        amount int,
        primary key (rid),
        foreign key (email) references Members,
        foreign key (pickup) references Locations,
        foreign key (dropoff) references Locations
        );

        create table if not exists Inbox(
        email char(28),
        msgTimestamp date,
        sender char(28),
        content char(150),
        rno int,
        seen char(1),
        primary key (email,msgTimestamp),
        foreign key (email) references Members,
        foreign key (sender) references Members,
        foreign key (rno) references Rides
        );
        ''')
        self.conn.commit()

    def statement(self):
        print(self.hi)

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
if __name__ == "__main__":
    app = JavinDrive()
    app.app_loop()

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
        self.cursor.execute('''
        create table if not exists Members(
        email TEXT,
        name TEXT,
        phone TEXT,
        pwd TEXT,
        PRIMARY KEY (email))''')
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

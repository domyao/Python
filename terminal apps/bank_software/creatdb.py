
import sqlite3 as s


#put evrything in a function

def build_table():
    db = s.connect('bank.db')
    c = db.cursor()

    c.execute('DROP TABLE IF EXISTS users ')

    c.execute('''
                    CREATE TABLE users(
                    id INTEGER ,
                    username VARCHAR(30) UNIQUE,
                    password VARCHAR(30),
                    permission INTEGER,
                    date_created DATE,
                    date_updated DATE,
                    PRIMARY KEY(id)
                    )
              ''')

    print('table users created')

    c.execute('DROP TABLE IF EXISTS accounts')

    c.execute('''
                    CREATE TABLE accounts(
                    id INTEGER,
                    id_user INTEGER,
                    a_number INTEGER UNIQUE,
                    balance FLOAT(2),
                    date_created DATE,
                    date_updated DATE,
                    PRIMARY KEY(id),
                    FOREIGN KEY(id_user) REFERENCES users(id)
                    )
              ''')
    print('table accounts created')

    db.commit()
    db.close()


if __name__ == "__main__":
    build_table()

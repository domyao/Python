
import sqlite3 as s
import random as r
from uuid import uuid4 as u


def populate_bank():

    db = s.connect('bank.db')
    c = db.cursor()


    c.execute('DELETE FROM users')
    c.execute('DELETE FROM accounts')
    print('old records destroyed')

    users = [
    ('Adam', '1112', 2),
    ('Jeffson', 'rhtuyht', 1),
    ('Jovas', 'rhtuyht', 1),
    ('Matthew', 'thutyw', 1)

    ]


    c.executemany('''
                   INSERT INTO users (username, password, permission, date_created, date_updated)
                   VALUES(?,?,?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                  ''', users)

    print("users data imported into database")




    client_ids = c.execute('''
                             SELECT id FROM users
                             WHERE permission = 1
                        ''').fetchall()


    for client_id in client_ids:

        client_accounts = [(client_id[0], int(str(u().int)[:7]) ) for _ in range(r.randint(1, 4))]
        c.executemany('''INSERT INTO accounts (id_user, a_number, balance, date_created, date_updated)
                        VALUES (?,?, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                        ''', client_accounts)


    print("accounts data imported into database")

    db.commit()
    db.close()

if __name__ == '__main__':
    populate_bank()

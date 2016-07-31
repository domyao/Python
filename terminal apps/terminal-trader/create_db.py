import sqlite3
conn = sqlite3.connect('terminal_trader.db')
c = conn.cursor()

def build_table():


    c.execute(''' DROP TABLE IF EXISTS users ''')

    c.execute('''
                 CREATE TABLE users(
                 id INTEGER,
                 username VARCHAR(20) UNIQUE,
                 password VARCHAR(20),
                 access INTEGER,
                 fluid_cash FLOAT(2),
                 date_created DATE,
                 date_updated DATE,
                 PRIMARY KEY(id)

                )''' )

    print("table users created")







    c.execute('DROP TABLE IF EXISTS company')

    c.execute('''
                CREATE TABLE company(
                id INTEGER,
                symbol VARCHAR(6),
                PRIMARY KEY(id)
                )
    ''')

    print("table company created")








    c.execute('DROP TABLE IF EXISTS portfolio')

    c.execute('''
                CREATE TABLE portfolio(
                id INTEGER,
                id_user INTEGER,
                id_company INTEGER,
                stock_quantity INTEGER,
                last_trade_date DATE,
                PRIMARY KEY(id),
                FOREIGN KEY (id_user) REFERENCES users(id),
                FOREIGN KEY (id_company) REFERENCES company(id)
                )
    ''')

    print("table portfolio created")




    c.execute('DROP TABLE IF EXISTS trading_history')

    c.execute('''
                CREATE TABLE trading_history(
                id INTEGER,
                id_user INTEGER,
                id_company INTEGER,
                traded_quantity INTEGER,
                earn FLOAT(2),
                date_traded DATE,
                PRIMARY KEY(id),
                FOREIGN KEY (id_user) REFERENCES users(id),
                FOREIGN KEY (id_company) REFERENCES company(id)
                )
    ''')

    print("table trading_history created")

    conn.commit()




def seed(base_money):
    users = [
    ('Adam', '1110', 2),
    ('Jeffson', '1111', 1),
    ('Jack', '1112', 1),
    ('Mike', '1113', 1),
    ('Ellen', '1114', 1),
    ]

    for user in users:

        c.execute('''
                    INSERT INTO users
                    (username, password, access, fluid_cash, date_created, date_updated)
                    VALUES(?,?,?,?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                    ''', (*user, base_money) )

    print("users data created..")
    conn.commit()


if __name__ == "__main__":
    build_table()
    seed(100000)

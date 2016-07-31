
import sqlite3 as s

db = s.connect('bank.db')
c = db.cursor()


# To do:

# may be the sys does not need user arttibute... DONE
#
# A choice between these two:
# 1. To retrive a local copy of the data and modified it locally and then updated to database
# 2. directly operate on database (easier...!)
#
# NO right or wrong, just a perference
#
# the __str__ is here for test purpose only... should be implemented in view
#




class User:


    def __init__(self, id_, username, password, permission, date_created, date_updated):
        self.id = id_
        self.username = username
        self.password = password
        self.permission = permission
        self.date_created = date_created
        self.date_updated = date_updated





class Account:
    def __init__(self, id_, id_user, a_number, balance, date_created, date_updated ):
        self.id_ = id_
        self.id_user = id_user
        self.a_number = a_number
        self.balance = balance
        self.date_created = date_created
        self.date_updated = date_updated




    def __str__(self):
        return ("id:{}| id_user: {}| Account Number:{}| Balance: {}".format(self.id_, self.id_user, self.a_number, self.balance) )


    def __repr__(self):
       return '<' + self.__str__() + '>'















class Bank:
    def __init__(self):
        self.user = None
        self.sys = None



    def log_in(self, username, password_input):

        query = '''SELECT * from users
                   WHERE username = ? AND password = ?
                '''

        c.execute(query, (username, password_input))
        result = c.fetchall()

        if not result:
            return False
        else:
            self.user = User(*result[0])
            return True



    def init_user_system(self):
        if self.user.permission == 1:
            self.sys = ClientSys(self.user)
        else:
            self.sys = AdminSys(self.user)



    def check_account(self, account_num):
        '''
        Intelligently check the legility of the account required based on the user's permission level
        '''
        if self.user.permission == 1:
            account = self.sys.get_account_locally(account_num)
        else:
            account = self.sys.get_account_remotely(account_num)

        if not account:
            return False

        return account















class UserSys:

    def __init__(self, user):
        self.user = user



    def deposit(self, account, amount):

        account.balance += amount
        self.update_accounts_database(account)



    def withdraw(self, account, amount):
        if account.balance < amount:
            return False
        else:
            account.balance -= amount
            self.update_accounts_database(account)
            return True



    def transfer(self, account_from, account_to, amount):

        if self.withdraw(account_from, amount):   # if withdraw successfully
           self.deposit(account_to, amount)
           self.update_accounts_database(account_from)
           self.update_accounts_database(account_to)
           return True

        return False
        # the failure of transfer, given the right account info, would be due to the failure of withdraw


    def update_accounts_database(self, account):

        query = '''
                    UPDATE accounts
                    SET balance = ?, date_updated = CURRENT_TIMESTAMP
                    WHERE a_number = ?
                '''

        c.execute(query, (account.balance, account.a_number))

        db.commit()  # to save the change



    def get_account_remotely(self, account_num):
        '''
        Looking through the whole database. return the account object with the given account_number
        return False if not found
        '''
        account_info = c.execute(''' SELECT * FROM accounts WHERE a_number = ? ''', (account_num,)).fetchall()
        if not account_info:
            return False
        else:
            return Account(*account_info[0])











class ClientSys(UserSys):

    def __init__(self, user):
        super().__init__(user)
        self.accounts = self._fetch_accounts()



    def _fetch_accounts(self):
        query = '''
                    SELECT  a.id, a.id_user, a.a_number, a.balance, a.date_created, a.date_updated FROM accounts AS a
                    JOIN users AS u
                    ON a.id_user = u.id
                    WHERE u.username = ?
                '''
        accounts_info = c.execute(query, (self.user.username,) ).fetchall()

        return [ Account(*account_info) for account_info in accounts_info ]



    def view_accounts(self):
        '''
        all the operation will be done locally first.
        so view_accounts always see the lastest info of his account
        '''
        return self.accounts



    def get_account_locally(self, account_num):
       '''
       Looking through the accounts arttribute, return the account object with the given account_number
       return False if not found
       '''
       for account in self.accounts:
            if account.a_number == account_num:
                return account

       return False












class AdminSys(UserSys):


    def create_user(self, username, password):

        c.execute('''
                   INSERT INTO users (username, password, permission, date_created, date_updated)
                   VALUES(?,?,?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                  ''', (username, password, 1))
        db.commit()



    def create_account(self, username, account_num):

        id_user = c.execute('''SELECT id FROM users WHERE username = ?''', (username,)).fetchall()

        if not id_user:
            return False

        c.execute('''INSERT INTO accounts (id_user, a_number, balance, date_created, date_updated)
                        VALUES (?,?, 0, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                        ''', (id_user[0][0],account_num) )
        db.commit()
        return True



if __name__ == "__main__":
    db = s.connect('bank.db')
    c = db.cursor()
    bank = Bank()
    bank.log_in('Jeffson', 'rhtuyht')
    bank.init_user_system()






























#
# def __str__(self):
#     return ("id:{}| id_user: {}| Account Number:{}| Balance: {}".format(self.id_, self.id_user, self.a_number, self.balance) )
#
#
# def __repr__(self):
#    return '<' + self.__str__() + '>'
#
#
#
# def __str__(self):
#     return ("username: {}| permission: {}".format(self.username, self.permission, self.date_created, self.date_updated))
#
#
# def __repr__(self):
#     return '<' + self.__str__() + '>'
#
#
#
#
#
#
# get_account_locally can just replace check_if_account_permitted
#
# def check_if_account_permitted(self, account_num):
#     '''
#     check if the account given is the client's own account.
#     return True or Falses
#     '''
#
#     return account_num in (account.a_number for account in self.accounts)








# get_account_remotely can just replace with check_if_accounts_exists
#
# def check_if_accounts_exists(self, *account_nums):
#     '''
#     it is used when client transfer money to another users account
#     or the banker works with different accounts
#     @param: one or several account number
#
#     '''
#
#     all_accounts = c.execute(''' SELECT a_number FROM accounts ''').fetchall()
#     all_accounts = [x[0] for x in all_accounts]
#
#     for x in account_nums:
#         if x not in all_accounts:
#             return False
#
#     return True



#
# def deposit(self, account, amount):
#
#     c.execute('''
#                 UPDATE accounts
#                 SET balance = balance + ?
#                 WHERE a_number = ?
#                 ''',(amount, account_num)
#                 )
#
#
#
# def withdraw(self, account amount):
#     c.execute('''
#                 UPDATE accounts
#                 SET balance = balance - ?
#                 WHERE a_number = ?
#                 ''', (amount, account_num)
#                 )
#



#
# def withdraw(self, account_num, amount):
#
#     for accont in accounts:
#         if account.a_number == account_num:
#
#             if account.balance < amount:
#                 return False
#             else:
#                 account.balance -= amount
#                 return True

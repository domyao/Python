
from wrapper import Markit
m = Markit()
import sqlite3

conn = sqlite3.connect('terminal_trader.db')
c = conn.cursor()


TOP = 10
INIT_MONEY = 100000








class Stock:
    def __init__(self, symbol, quantity):
        self.symbol = symbol
        self.quantity = quantity
        self.in_database = False


    def __str__(self):
        return self.__repr__()


    def __repr__(self):
        return ("< {} |stock quantities: {} > ".format(self.symbol, self.quantity, self.in_database))






class User:
    def __init__(self, id_, username, password, access, fluid_cash, date_created, date_updated):
        self.id_ = id_
        self.username = username
        self.password = password
        self.access = access
        self.fluid_cash = fluid_cash
        self.date_created = date_created
        self.date_updated = date_updated


    def __repr__(self):
        return("<username: {} |access: {} |fluid_cash: {}>".format(self.username, self.access, self.fluid_cash) )


    def __str__(self):
        return self.__repr__()







class TerminalTrader:




    def __init__(self):
        self.user = None
        self.usersys = None




    def log_in(self, username, password):
        '''
        return True if log in successfully
        return False if no username, password combination found 
        '''
        
        query = '''SELECT * from users
                   WHERE username = ? AND password = ?
                '''

        c.execute(query, (username, password))
        result = c.fetchall()

        if not result:
            return False
        else:
            self.user = User(*result[0])
            return True






    def add_user(self, username, password):
        '''
        return True if add_user successfully
        return False if username already exists
        '''

        name_check = '''
                    SELECT username from users
                    WHERE username = ?
                    '''
        c.execute(name_check, (username,))

        if c.fetchone():   
            return False


        c.execute('''
                    INSERT INTO users
                    (username, password, access, fluid_cash, date_created, date_updated)
                    VALUES
                    (?, ?, 1, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                ''', (username, password, INIT_MONEY))

        conn.commit()

        return True









    def init_sys(self):
        if self.user.access == 1:
            self.usersys = NormalSys(self.user)
        else: 
            self.usersys = SuperSys(self.user)









class NormalSys:


    def __init__(self, user):
        self.user = user 
        self.portfolio = self._fetch_portfolio()
  

    def __repr__(self):
        return ("< username: {}| total_asset: {}".format(self.user.username, self.total_asset))




    @property
    def stock_worth(self):
        return self._stock_worth()



    @property
    def total_asset(self):

        #Try to catch the API failure?:
        return self.stock_worth + self.user.fluid_cash
    
   

    

    def _fetch_portfolio(self):
   
 
        all_info = c.execute('''
                                SELECT c.symbol, p.stock_quantity
                                FROM users AS u
                                JOIN portfolio AS p ON u.id = p.id_user
                                JOIN company AS c ON c.id = p.id_company
                                WHERE u.username = ?
                            ''', (self.user.username,) ).fetchall()

        if not all_info:
            return []
        else:
            return [Stock(*info) for info in all_info]






    def _stock_worth(self):

        stock_worth = 0

        for stock in self.portfolio:

            quote = self.get_quote(stock.symbol)
            if "ServerBusy" in quote: # if API fails
                return False

            stock_worth += stock.quantity * quote['LastPrice']  
           

        return stock_worth
        






    def dashboard(self):

        return {
                "username": self.user.username,
                "portfolio": self.portfolio, 
                "stock worth": self.stock_worth, 
                "fluid cash": self.user.fluid_cash,
                "total asset": self.total_asset
                }






    def company_search(self, company):
        return m.company_search(company)





    def get_quote(self, symbol):
        return m.get_quote(symbol)



    


    def buy(self, symbol, price, quantity):
        '''
        return False if user does not have enough money
        return True if trade successfully
        '''

        cost = price * quantity
        if cost > self.user.fluid_cash:
            return False


        stock = self.search_portfolio(symbol)

        if not stock:                                        # if the user haven't bought the stock from this company before
            stock = Stock(symbol, quantity)
            self.portfolio.append(stock)                     # add the new reord into user's portfolio          
        else:
             stock.quantity += quantity


        self.user.fluid_cash -= cost  
        self.update_portfolio(stock)
        self.update_users()
        return {'cost':cost}





        


    def sell(self, symbol, price, quantity):
        '''
        return different values based on the result condition

        '''

        cash = price * quantity
        stock = self.search_portfolio(symbol)

        if (not stock) or (stock.quantity < quantity):
            return False
        
        else:
            self.user.fluid_cash += cash
            stock.quantity -= quantity

            if stock.quantity == 0:
                self.portfolio.remove(stock)

            self.update_portfolio(stock)
            self.update_users()
            return {'earn':cash}







    def search_portfolio(self, symbol):

        for stock in self.portfolio:
            if stock.symbol.lower() == symbol.lower():   # lower()
                return stock

        return False






    def update_company(self, stock):

        id_company = c.execute('''
                                SELECT id FROM company
                                WHERE symbol = ?
                            ''', (stock.symbol,)).fetchall()

        if not id_company:

            c.execute('''
                INSERT INTO company (symbol) VALUES(?)
                ''', (stock.symbol,))

            id_company = c.lastrowid 

        else:
            id_company = id_company[0][0]


        return id_company







    def update_portfolio(self, stock):

        
        id_company = self.update_company(stock)   # update the company table. 


        if stock.quantity == 0:

            c.execute('''
                        DELETE FROM portfolio 
                        WHERE id_company = ?

                ''', (id_company,))




        elif not stock.in_database:

            c.execute('''
                        INSERT INTO portfolio 
                        (id_user, id_company, stock_quantity, last_trade_date)
                        VALUES
                        (?,?,?, CURRENT_TIMESTAMP)

                ''', (self.user.id_, id_company, stock.quantity))

            stock.in_database = True




        else:
            c.execute('''
                        UPDATE portfolio
                        SET stock_quantity = ?
                        WHERE id_company = ?
                ''', (stock.quantity, id_company))


        conn.commit()
        





    def update_users(self):

        c.execute('''
                    UPDATE users
                    SET fluid_cash = ?, 
                    date_updated = CURRENT_TIMESTAMP
                    WHERE id = ?
                ''', (self.user.fluid_cash, self.user.id_))


        conn.commit()



 
    



class SuperSys:

    
    
    def __init__(self, user):
        self.user = user


    @property
    def dashboards(self):
        return self._dashboards()
    



    def _dashboards(self):
    

        users_info = c.execute('''SELECT * from users
                                   WHERE access = 1
                                ''').fetchall()

        for user_info in users_info:            
            yield NormalSys( User(*user_info) ).dashboard()




    def leaderboard(self):

        users_sorted = sorted(self.dashboards, key = lambda dashboard: dashboard["total asset"], reverse = True)

        if len(users_sorted) < TOP:
            return users_sorted
        else:
            return users_sorted[:TOP]





    


if __name__ == "__main__":
    T = TerminalTrader()
    T.log_in('Mike', '1113')
    T.init_sys()
    sys = T.usersys
    T.log_in('Adam', '1110')
    T.init_sys()
    asys = T.usersys













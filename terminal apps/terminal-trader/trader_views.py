
# you will get a string from the input
# Do not forget to convert it

import pprint as p
class View:



    def welcome_message(self):
        print('''
---------- WELCOME to the terminal trader game ------------

In this game, you will have an initial asset of $100,000,
you can search for the real world stock info,and explore the stock market 
wisely invest your money, and grow your wealth!

PS: If in your dashboard, the stock asset is "FALSE"
    that means system is busy, try again. 
    (too lazy to catch the error, just so you know...)

------------------------------------------------------------
''')


    def login_or_new_user(self):
        print('''
1. log in 
2. sign up new account
''')

        return input()
    







    def prompt_info_log_in(self):
        print("\nEnter username and password:")



    def prompt_info_add_user(self):
        print("Register info:")


    
    def ask_username_password(self):

        username = input("Username: ")
        password = input("Password: ")
        return username, password








    def log_in_failed(self):
        print("\nno such a username and password combination found...Please try again\n")

    def add_user_failed(self):
        print("username already exist")

    def ask_if_log_in_as_new_user(self):
        return input("\nLog in as the new user?(y/n)    ")









    def prompt_for_options_normal(self):

        print('''
1. view dashboard
2. get company quote
3. buy stocks
4. sell stocks
                ''')

        return input()

   



    def prompt_for_options_super(self):

        print('''
view leaderbord? (y/n)             
                ''')

        return input()





    def print_dashboard_updating(self):
        print("\nupdating the dashboard...\ncalculating lasted stock worth...")



    def print_dashboard(self, dashboard):
        print('''
-------------------------------------------
          {username}'s DASHBOARD 
-------------------------------------------
Porfolio    : {portfolio}

Stock Worth : {stock worth}

Fluid Cash  : {fluid cash}

-------------------------------------
TOTAL ASSET : {total asset}

'''.format(**dashboard) )    # Oh, MY, GOD, IT WORKED!!









    def remind_server_busy(self):
        print("\nSorry, server is busy :( , Please try again later...\n")


    def ask_for_search_criteria(self):
        return input("\nwhich company are you interested to invest?  \n")

    def no_company_found(self):
        print("\nSorry, no company found Q.Q, please check your searching criteria\n")

    def print_companies(self, result):

        print('''\n-------------Searching Result------------------''')

        for m in result:
            print('''
|Symbol: {Symbol}   |Name: {Name}   |Exchange: {Exchange}
                '''.format(**m))



    def prompt_for_symbol(self):
        return input("\nEnter the unique symbol of the company \n")



    def print_error_message(self, result):

        print(result['Message'])





    def print_quote(self, quote):
        print('''\n-------------Company info ------------------\n''')
        p.pprint(quote)


    def show_lastest_price(self, symbol, price):
        print("\nThe lasted price of the stock of {} is {}\n".format(symbol, price))


    def prompt_for_quantity(self):
        return int(input("\nquantity you wanna trade: "))





    def print_not_enough_money(self):
        print("Fluid cash is not sufficient.\n")

    def print_not_enough_stock(self):
        print("Not enough stocks in your portfolio\n")

    def print_trading_succeed(self):
        print("trading successfully!\n")

    

    def print_money_deducted(self, cost):
        print("\n${:.3f} deducted from your account.".format(cost))

    def print_money_added(self, earn):
        print("\n${:.3f} added into your account.".format(earn))




    def print_leaderboard(self,leaderboard):

        print('''
------------------------------------------------
            LEADERBOARD (TOP 10)
------------------------------------------------
''')
        
        idx = 1
        for dashboard in leaderboard:

            print('''
{} {username} ----------------------- 

Porfolio    : {portfolio}
Stock Worth : {stock worth}    Fluid Cash  : {fluid cash}     TOTAL ASSET : {total asset}
                '''.format(idx, **dashboard))

            idx += 1






    def ask_if_continue(self):
        return input("\ncontinue?(y/n) ")

    def print_log_out_message(self):
        print("logging out....")

    

    



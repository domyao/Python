from trader_models import Stock, User, TerminalTrader, NormalSys, SuperSys
from trader_views import View
import re



class TraderController:




    def __init__(self):
        self.view = View()
        self.program = None







    def run(self):
        
        self.view.welcome_message()
        self.initialize_user()

        continue_ = 'y'
        while continue_ == 'y' :

            if self.program.user.access == 1:
                self.operate_normal()
            else:
                self.operate_super()

            continue_ = self.view.ask_if_continue()

        self.view.print_log_out_message()
    








    def initialize_user(self):

        choice = '3'
        while not(choice == '1'  or choice == '2'):
            choice = self.view.login_or_new_user()
        
        self.program = TerminalTrader()


        if choice == '1':
            self.log_in()
        else:
            self.sign_up()
 

        self.program.init_sys()









    def log_in(self):

        self.view.prompt_info_log_in()

        username, password = self.view.ask_username_password()

        while not self.program.log_in(username, password):  
            self.view.log_in_failed()
            username, password = self.view.ask_username_password()

         # two different log in one is in model, one is in controller
         # keep asking for log in if failed











    def sign_up(self):

        self.view.prompt_info_add_user()

        username, password = self.view.ask_username_password()

        while not self.program.sign_up(username, password):
            self.view.add_user_failed()
            username, password = self.view.ask_username_password()
    

        choice = self.view.ask_if_log_in_as_new_user()    # ask if uaer wanna sign in as the user just created

        if choice == 'y':
            self.program.log_in(username, password)
        else:
            self.log_in()







    def operate_normal(self):
   
        proce = None
        option = '5'

        while not re.match(r'[1234]', option):
            option = self.view.prompt_for_options_normal()

        if option == "1":
            self.view_dashboard()
            
        elif option == "2":
            self.get_company_quote()           

        elif option == "3" or "4":
            self.buy_sell_stock(option)


            





    def view_dashboard(self):
        self.view.print_dashboard_updating() 
        dashboard = self.program.usersys.dashboard()       
        self.view.print_dashboard(dashboard)








    def check_quote(self, symbol):

        quote = self.program.usersys.get_quote(symbol)

        if 'ServerBusy' in quote:
            self.view.remind_server_busy()
            return False 

        elif 'Message' in quote:        # if not company found for the given symbol, an error message will be there
            self.view.print_error_message(quote)
            return False
                
        return quote





    def check_out_companies(self, search_criteria):

        result = self.program.usersys.company_search(search_criteria)

        if 'ServerBusy' in result:
            self.view.remind_server_busy()   # Try to catch the API failure
            return False
        
        if 'Message' in result:              # if input is '', something like {'Message': 'Missing Required Parameter: "input"'} will be returned from API
            self.view.print_error_message(result)
            return False

        if not result:                       # if no company found, result is empty
            self.view.no_company_found() 
            return False

        return result






    def get_company_quote(self):

        search_criteria = self.view.ask_for_search_criteria() 
        result = self.check_out_companies(search_criteria)
        
        if not result:
            return

        self.view.print_companies(result)
        
        symbol = self.view.prompt_for_symbol() 
        quote = self.check_quote(symbol)      
 
        if not quote:
            return

        self.view.print_quote(quote) 



    





    def buy_sell_stock(self, option):

        symbol = self.view.prompt_for_symbol() 
        quote = self.check_quote(symbol)


        if not quote:
            return

        symbol = quote['Symbol']
        price = quote['LastPrice']     
        # update the symbol to the correct format, 
        # if user enter aapl, but the more accurate one is AAPl, everything is fine, no problem, 
        # but to look nicer in portfolio, it will be corrected here to the formal accurate one
 
        
        self.view.show_lastest_price(symbol, price) 
        quantity = self.view.prompt_for_quantity() 


        if option == '3':
            result = self.program.usersys.buy(symbol, price, quantity)
            if  result == False:
                self.view.print_not_enough_money() 
                return
            self.view.print_money_deducted(result['cost'])

 
        else:
            result = self.program.usersys.sell(symbol, price, quantity)
            print(result)
            if result == False:
                self.view.print_not_enough_stock() 
                return
            self.view.print_money_added(result['earn'])


        self.view.print_trading_succeed() 





    


    def operate_super(self):

        option = self.view.prompt_for_options_super()
        if option == 'y':
            leaderboard = self.program.usersys.leaderboard()
            self.view.print_leaderboard(leaderboard) 











if __name__ == "__main__":
    program = TraderController()
    program.run()
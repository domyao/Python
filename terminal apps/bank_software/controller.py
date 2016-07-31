
from models import User, Account, Bank, UserSys, ClientSys, AdminSys
from view import View
import re




class BankController:
    def __init__(self):
        self.bank = None
        self.view = View()



    def run(self):

        self.view.welcome_message()
        username, password = self.view.ask_username_password()
        self.bank = Bank()

        while not self.bank.log_in(username, password):
            self.view.print_log_in_error()
            username, password = self.view.ask_username_password()

        self.view.print_log_in_successfully()
        self.bank.init_user_system()

        continue_ = 'y'
        while continue_ == 'y' :
            self.operate()
            continue_ = self.view.ask_if_continue()

        self.view.print_log_out_message()





    def operate(self):

        option = '5'
        while not re.match(r'[1234]', option):
            option = self.view.prompt_for_options(self.bank.user)

        if option == '1':
            self.execute_option_1()
        elif option == '2'  or option == '3':  #deposit or withdraw
            self.execute_option_2_3(option)
        else:
            self.execute_option_4()



# execute option 1

    def execute_option_1(self):
        if self.bank.user.permission == 1:
            accounts = self.bank.sys.view_accounts()
            self.view.print_accounts_info(accounts)

        else:
            self.create_new_account()





    def create_new_account(self):

        username, account_num = self.view.ask_new_account_info()
        if username == self.bank.user.username:
            self.view.remind_banker_have_no_accounts()
            return

        if not self.bank.sys.create_account(username, account_num):
            self.view.print_no_user_found(username)
            add_user = self.view.ask_if_add_user()

            if add_user == 'y':
                self.create_new_user()

        else:
            self.view.account_created(account_num, username)







    def create_new_user(self):

        username, password = self.view.ask_username_password()
        self.bank.sys.create_user(username, password)
        self.view.user_created()






# execute option 2_3


    def execute_option_2_3(self, option):
        if option =='2': #deposit
            account_num = self.view.prompt_for_account_deposit()
        else:  #withdraw
            account_num = self.view.prompt_for_account_withdraw()


        account = self.bank.check_account(account_num)

        if not account:
            self.view.print_no_account_found(account_num)
            return


        amount = self.view.prompt_for_amount()




        if option == '2':
            self.bank.sys.deposit(account, amount)
            self.view.print_deposit_successfully(account_num, amount)
        else:
            if not self.bank.sys.withdraw(account, amount):  #not enough money
                self.view.remind_balance(account)
            self.view.print_withdraw_successfully(account_num, amount)



# execute option 4

    def execute_option_4(self):

        account_from_num, account_to_num = self.view.prompt_for_account_transfer()



        account_from = self.bank.check_account(account_from_num)

        if not account_from:
            self.view.print_no_account_found(account_from_num)
            return



        account_to = self.bank.sys.get_account_remotely(account_to_num)

        if not account_to:
            self.view.print_no_account_found(account_to_num)
            return



        amount = self.view.prompt_for_amount()

        if not self.bank.sys.transfer(account_from, account_to, amount):
            self.view.remind_balance(account_from)
        else:
            self.view.print_transfer_successfully(account_from_num, account_to_num, amount)



if __name__ == "__main__":
    bank = BankController()
    bank.run()

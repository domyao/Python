

# Be carefull about the datatype received and datatype passed.
# you get a string from input!!!


class View:

    def welcome_message(self):
        print("welcome to the CommandLine Bank Sysytem")
        print("Please log in")

            


    def ask_username_password(self):
        username = input("username: ")
        password = input("password: ")
        return username, password








    def print_log_in_error(self):
        print("\nno such a username and password combination found\nPlease Try again..\n")




    def print_log_in_successfully(self):
        print("\nlog in...")







    def prompt_for_options(self, user):
        if user.permission == 1:
            print('''
Select one of the following options:
1: view your account
2: deposit into your account
3: withdraw from your account
4: transfer money to another account
''')




        else:
            print('''
Select one of the following options:
1: create an account
2: deposit into an account
3: withdraw from an account
4: transfer money from one account to another account
''')

        return input()






    def print_accounts_info(self, accounts):
        print("\n -----------Accounts Info-----------\n")

        for account in accounts:
            print("\n account number: {}| balance: {}| date_updated: {}\n".format(account.a_number, account.balance, account.date_updated))






    def ask_new_account_info(self):
        username = input("\nEnter the username new account will be added into: ")
        account_num = input("Enter the new account number: ")
        return username, account_num

    def remind_banker_have_no_accounts(self):
        print("\nCannot create an account for banker...")
    def print_no_user_found(self, username):
        print("User {} not found ....\n".format(username))


    def ask_if_add_user(self):
        return input("Do you wanna add a new user(y/n)  ")


    def user_created(self):
        print("new user successfully added\n")






    def account_created(self, account_num, username):
        print("\nnew account {} successfully added into {}".format(account_num, username))


    def print_no_account_found(self, account_num):
        print("Account number {} not found \n".format(account_num))







    def prompt_for_account_deposit(self):
        account_num = input("deposit into (enter account number): ")
        return int(account_num)



    def print_deposit_successfully(self, account_num, amount):
        print("\nSuccessfully deposit ${} into account {}".format(amount, account_num))







    def prompt_for_account_withdraw(self):
        account_num = input("withdraw from (enter account number): ")
        return int(account_num)



    def print_withdraw_successfully(self, account_num, amount):
        print("\nSuccessfully withdraw ${} from account {}\n".format(amount, account_num))







    def prompt_for_account_transfer(self):
        account_from = input("transfer from: ")
        account_to = input("transfer into: ")
        return int(account_from), int(account_to)



    def print_transfer_successfully(self, account_from_num, account_to_num, amount):
       print("Successfully transfer ${} from account {} to account {}\n".format(amount, account_from_num, account_to_num))







    def prompt_for_amount(self):
        amount = input("The amount of money: ")
        return float(amount)







    def remind_balance(self, account):
       print("\nnot enough money in account {}\ncurrent balance: {}\n".format(account.a_number, account.balance))







    def ask_if_continue(self):
        return input("\nDo you wanna continue?(y/n)    ")






    def print_log_out_message(self):
        print("logging out....")

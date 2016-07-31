##  Bank software

A Python terminal app emulating bank software.

##### Database

* run the createdb.py and seed.py first in the terminal
* two tables Users and Accounts will be created and seeded with initial data
* A user can have many accounts
* Users have
	* A username to log in
	* A password to log in
	* When they were initially created
	* A permission level
* Accounts have
	* A number
	* A balance


##### Models

* two seperate classes ClientSys and AdminSys inherited from UserSys

* A client is able to:
	* view all their accounts
	* deposit and withdraw from their own account
	* transfer money from one account to another user account
* A banker is able to:
	* create accounts
	* deposit and withdraw from any user account
	* transfer money between two accounts
* Note
	* A client cannot see the options a banker has
	* A banker cannot have any account associated with them



* a Bank class to get start and initiate the ClientSys or AdminSys based on the user logged in.

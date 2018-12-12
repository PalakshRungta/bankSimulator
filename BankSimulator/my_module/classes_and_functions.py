import pickle
import time
import os.path
from random import randint

class SavingsAccount():
    '''A class with a set of functions that replicates a virtual banking application.
    With this, the user can make a Savings Account; Access an existing account (to withdraw, deposit, and display balance); and Delete an existing account

    Attributes
    ----------
    key: int, default = 0
        Used as a key to iterate through the dictionary of user data.
    '''

    # Defining a class attribute which will be later used to navigate through the dictionary containing user data.
    key = 0

    def __init__(self):

        #Initializing variables for the object.
        self.existing_accounts = {}
        self.userName = None
        self.depositAmount = None

        self.user_name = None
        self.account_number = None

        self.withdraw_amount = None
        self.deposit_amount = None


    def creating_file(self):
        '''Creating a file ('AccountInfo.txt') with a dictionary inside.
        If 'AccountInfo.txt' exists, the creation steps are skipped to avoid the creation of multiple files.
        '''

        #Finds the current working directory of the code.
        cwd = os.getcwd()

        #If file 'AccountInfo.txt' exists, pass.
        if os.path.isfile(cwd + "/AccountInfo.txt"):
            pass
        else:
            self.existing_accounts = {}

            #Creating a file 'AccountInfo.txt' by opening 'AccountInfo.txt' for writing
            output = open('AccountInfo.txt', 'wb')

            #Adds the dictionary to 'AccountInfo.txt'
            pickle.dump(self.existing_accounts, output)

            output.close()

    def savings_account_details(self):
        '''If the user wants to create a Savings Account, it asks for the name and deposit amount.
        It auto assigns a random 5 digit number as the account number to the user.
        '''

        print("\nPlease fill up the following details")

        self.userName = input("Name: ")
        self.depositAmount = int(input("Initial deposit amount: "))

        #Generates a random 5-digit number.
        self.accountNumber = randint(10000, 99999)
        self.accountNumber = str(self.accountNumber)

        print("\nThank you for creating a new Savings account! Your account number is:", self.accountNumber)

        #Waits for 1 second before executing the next segment of code.
        time.sleep(1)

    def adding_to_existing_account(self):
        '''Adds user data (name, deposit amount, and account number) to the dictionary present in 'AccountInfo.txt'.
        The dictionary is nested with integer keys representing one user's data.

        Notes
        -----
        Format of the dictionary: {
            1:{"Name": userName, "Account Number": accountNumber, "Amount": depositAmount},
            2:{"Name": userName, "Account Number": accountNumber, "Amount": depositAmount}
        }
        '''

        #Opens 'AccountInfo.txt' for reading
        output = open('AccountInfo.txt', 'rb')

        #Loads the dictionary data
        self.existing_accounts = pickle.load(output)

        output.close()

        len_of_array = len(self.existing_accounts)

        self.existing_accounts.update(
            {
                len_of_array + 1:{
                    "Name": self.userName,
                    "Account Number": self.accountNumber,
                    "Amount": self.depositAmount
                }
            }
        )

        output = open('AccountInfo.txt', 'wb')

        #Adds the updated dictionary to 'AccountInfo.txt'
        pickle.dump(self.existing_accounts, output)

        output.close()

    def existing_account_details(self):
        '''Checks if inputted name and account number matches the user data.
        If it does, it allows users to either withdraw, deposit, display balance, or do nothing.

        Raises
        ------
        ValueError:
            Raises ValueError if int is not inputted.

        SystemExit:
            Raises SystemExit when ValueError is raised and an invalid option is inputted.
        '''

        print("You have selected to access an existing account. Please give us your:")
        self.user_name = input("Name: ")
        self.account_number = input("Account Number: ")

        output = open('AccountInfo.txt', 'rb')
        self.existing_accounts = pickle.load(output)
        output.close()

        #Iterating through keys in the dictionary
        for element in self.existing_accounts:

            #Checks if name and account number matches the data present in the dictionary.
            if self.account_number == self.existing_accounts[element]["Account Number"] and \
            self.user_name.lower() == self.existing_accounts[element]["Name"].lower():

                #Assigns self.key to the dictionary key corresponding to the user.
                self.key = element
                print("\nHello, " + self.existing_accounts[element]["Name"].capitalize())

                break

        else:
            print("\nInvalid Input")

            #Calls main_body() which does not let the user withdraw, deposit or display balance as their account details did not match.
            main_body()

        loop_counter1 = True
        while loop_counter1:

            time.sleep(1)

            try:
                userChoice = int(input("\nWould you like to: \n 1: Withdraw Money \n " + \
                "2: Deposit Money \n 3: Display current Balance \n 4: None\n" + \
                "\n(Input the number corresponding to your choice)\n"))

                if userChoice == 1:
                    self.existing_account_withdrawal()
                elif userChoice == 2:
                    self.existing_account_deposit()
                elif userChoice == 3:
                    self.existing_account_balance()
                elif userChoice == 4:
                    loop_counter1 = False
                else:
                    print("Wrong Option")
                    raise SystemExit()

            except ValueError:
                print("\nInvalid Input")
                raise SystemExit()

    def existing_account_withdrawal(self):
        '''It withdraws the desired amount from the user's depositted amount and updates the amount in the dictionary.

        Raises
        ------
        ValueError:
            Raises a ValueError if int is not inputted
        '''

        try:
            self.withdraw_amount = int(input("Enter the amount you want to withdraw: \n"))

        except ValueError:
            print("\nInvalid Input")
            main_body()

        if self.withdraw_amount < 0: #If inputted amount is negative.
            print("\nInvalid Input. Please use the 'Deposit' option.")

        else:
            output = open('AccountInfo.txt', 'rb')
            self.existing_accounts = pickle.load(output)
            output.close()

            existing_withdrawal_amount = int(self.existing_accounts[self.key]["Amount"])
            amount_after_withdrawal = existing_withdrawal_amount - self.withdraw_amount

            #If excess money is trying to be withdrawed.
            if amount_after_withdrawal < 0:
                print("\nYou do not have enough balance.")

            else:
                self.existing_accounts[self.key]["Amount"] = str(existing_withdrawal_amount - self.withdraw_amount)
                print("\nYour current Balance is: ",self.existing_accounts[self.key]["Amount"])

                output = open('AccountInfo.txt', 'wb')
                pickle.dump(self.existing_accounts, output)
                output.close()

    def existing_account_deposit(self):
        '''It adds the desired amount to the user's existing amount and updates the amount in the dictionary.

        Raises
        ------
        ValueError:
            Raises a ValueError if int is not inputted
        '''

        try:
            self.deposit_amount = int(input("Enter the amount you want to Deposit: \n"))

        except ValueError:
            print("\nInvalid Input")
            main_body()

        #If inputted amount is negative.
        if self.deposit_amount < 0:
            print("\nInvalid Input. Please use the 'Withdraw' option.")

        else:

            output = open('AccountInfo.txt', 'rb')

            self.existing_accounts = pickle.load(output)

            output.close()

            existing_deposit_amount = int(self.existing_accounts[self.key]["Amount"])
            self.existing_accounts[self.key]["Amount"] = str(existing_deposit_amount + self.deposit_amount)
            print("Your current Balance is: ",self.existing_accounts[self.key]["Amount"])

            output = open('AccountInfo.txt', 'wb')

            pickle.dump(self.existing_accounts, output)

            output.close()

    def existing_account_balance(self):
        '''Displays the balance amount of the userself.'''

        output = open('AccountInfo.txt', 'rb')
        self.existing_accounts = pickle.load(output)
        output.close()

        print("Your current Balance is: ",self.existing_accounts[self.key]["Amount"])

    def deleting_an_existing_account(self):
        '''It asks the user for name and account number, with which it deletes the user's data in the dictionary'''

        print("\nPlease give the details of the account you want to delete")

        del_acc_name = input("Name: ")
        del_acc_number = input("Account Number: ")

        output = open('AccountInfo.txt', 'rb')
        self.existing_accounts = pickle.load(output)
        output.close()

        #Iterating through the dictionary.
        for item in self.existing_accounts:

            #Checks if name and account number matches the data in the dictionary.
            if self.existing_accounts[item]["Name"] == del_acc_name and \
            self.existing_accounts[item]["Account Number"] == del_acc_number:

                #Deletes the key and value corresponding to it.
                self.existing_accounts.pop(item)
                print("\nThank you for using our service, " + del_acc_name + ". Your account has been removed.")

                output = open('AccountInfo.txt', 'wb')
                pickle.dump(self.existing_accounts, output)
                output.close()

                time.sleep(1)

                break

        else:
            print("\nInvalid Input")

def main_body():
    '''This function runs the methods in SavingsAccount(). User input is used to [perform different tasks.

    Raises
    ------
    ValueError:
        Raises ValueError if an int is not inputted.

    SystemExit:
        Raises SystemExit to quit the code.
    '''

    #Calling the object saUser on SavingsAccount()
    saUser = SavingsAccount()

    #Calls method creating_file()
    saUser.creating_file()

    loop_counter0 = True
    while loop_counter0:

        print("\n Would you like to: \n 1: Create a new Savings account? \n " + \
         "2: Access an existing Savings Account? \n 3: Delete an existing Savings Account? \n 4: Exit")

        print("\n(Input the number corresponding to your choice)")

        try:
            userInput = int(input())

            if userInput == 1:

                #Asks for user name and deposit amount.
                saUser.savings_account_details()

                #Adds the user data to the dictionary.
                saUser.adding_to_existing_account()

            elif userInput == 2:

                #Accesses data which allows users to withdraw, deposit, and display balance.
                saUser.existing_account_details()

            elif userInput == 3:

                #Deletes user data from the dictionary.
                saUser.deleting_an_existing_account()

            elif userInput == 4:

                print("\nSee you later! Goodbye!\n")
                loop_counter0 = False

                raise SystemExit()

            else:

                print("\nInvalid Input")
                raise SystemExit()

        except ValueError:

            print("\nInvalid Input")
            raise SystemExit()

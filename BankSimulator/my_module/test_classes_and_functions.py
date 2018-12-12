from classes_and_functions import SavingsAccount, main_body
import os.path

"""Tests for my code."""

def test_function():

    assert SavingsAccount()
    user = SavingsAccount()
    
    assert user.creating_file() == None

    #Defining an object in the class SavingsAccount creates the file 'AccountInfo.txt'. As this is a test function, we can delete the file
    os.remove("AccountInfo.txt")

    assert user.existing_accounts == {}
    assert user.userName == None
    assert user.depositAmount == None
    assert user.user_name == None
    assert user.account_number == None
    assert user.withdraw_amount == None
    assert user.deposit_amount == None

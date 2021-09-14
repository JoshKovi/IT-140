import sys

#This is where the account_balance variable is initialized and set as a float of 500.25
account_balance = float(500.25)



#This is where the 3 functions used in this script are created. 
def printbalance(account_balance):
    #This is the printbalance function, it prints the account_balance variable, this function then returns the variable
    #account_balance with no changes and the return value is not assigned to anything.
    print("Your current balance:\n",account_balance,sep='')
    return account_balance


def deposit(deposited, account_balance):
    #The deposit function deposits a user input (deposited) by adding it to the account_balance variable, prints
    #a output notifying the user of the change in account_value, then finally returns the account_balance which is then 
    #assigned to the account_balance variable
    account_balance += deposited
    print("Deposit was $", format(deposited, '.2f'), ", current balance is $",account_balance, sep= '')
    return account_balance
    

def withdraw(withdrawn, account_balance):
    #The withdraw function subtracts checks if the user input withdrawal_amount is lessthan or equal to the account_balance
    #If True the function "withdrawals" the money from account_balance, prints an output statement to the user, then returns and
    #assigns the new account_balance, if the requested amount is larger, the function prints a message and then returns an unaltered
    #account_balance variable
    if withdrawn <= account_balance:
        account_balance -= withdrawn
        print("Withdrawal amount was $", format(withdrawal_amount, '.2f'), ", current balance is $%.2f" % account_balance, sep='')
        return account_balance
    else:
        print('$', format(withdrawal_amount, '.2f'), " is greater than your account balance of $%.2f" % account_balance, sep='')
        return account_balance




#This takes user input and then assigns it to the userchoice variable, The conditionals then execute based off the user input
#This entire section could be encased in a while loop to loop through multiple user actions
userchoice = input ("What would you like to do?\n")

if (userchoice == 'D'):
    #If the userchoice is "D" then prompt the user for the deposit_amount, call the deposit function and assign the return value
    #to the account_balance variable
    deposit_amount = float(input("How much would you like to deposit today?\n"))
    account_balance = deposit(deposit_amount, account_balance)
    

elif (userchoice == "B"):
    #This calls the printbalance function.
    printbalance(account_balance)


elif (userchoice == "W"):
    #This prompts the user for a withdrawal_amount, calls the withdraw function and then assigns the return value to the 
    #account_balance variable
    withdrawal_amount = float(input("How much would you like to withdraw today?"))
    account_balance = withdraw(withdrawal_amount, account_balance)
    
        

elif (userchoice == 'Q'):
    #This prints a thank you message for the user.
    print("Thank you for banking with us.")
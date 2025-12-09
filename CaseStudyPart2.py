#5 Design a software for bank system. There should be options like cash withdraw, cash credit and change password. According to user input, the software should provide required output
def AmountWithdrawl():
    PIN=int(input('Enter ATM CARD PIN to proceed:'))
    if PIN==12345:
        print ('Thank You For Banking With Us')
    else:
        print ('Enterd PIN Invalid . Try Again')
        
def CashCredit():
    PIN=int(input('Enter CARD PIN to proceed:'))
    if PIN==12345:
        AMT=input('Enter Amount You Wish to Credit To Bank:')
        print ('Thank You For Banking With Us***')
    else:
        print ('You Have Enterd Invalid PIN. Try Again')
def ChangePassword():
    PIN=int(input('Enter ATM or CARD PIN to proceed:'))
    if PIN==12345:
        OLD_PWD=int(input('Please Enter Your Old Password:'))
        print ('***Thank You For Banking With Us***')
    else:
        print ('You Have Enterd Invalid PIN. Try Again')
        



def Main():
    print ('Welcome to Edureka ABC Bank\nChoose from below options')
    print ('1. Cash withdrawal\n2. Cash credit\n3. Change password')
    
    bankoptions=int(input("Enter your option :"))
    
    if bankoptions ==1 :
        AmountWithdrawl()
    if bankoptions == 2:
        CashCredit()
    if bankoptions == 3:
        ChangePassword()
    else:
        print("Invalid Data entered ..")
        
Main()        
    


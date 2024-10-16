balance=0
def checkBalance():
    print(f"your balance is : {balance}")
def deposit(amount):
    global balance
   
    if amount>0:
        balance=balance+amount
        print(f"you have successfully deposited {amount} ")
        checkBalance()
    else:
        print("please enter valid amount")
def withdraw(withdraw):
    global balance
    
    if balance<withdraw:
        print("your balence is insufficient")
    else:
        balance=balance-withdraw
        print(f"you have successfully withdraw {withdraw}")
        checkBalance()
        
    
def bank():
    
    while True:
        print("welcome to banking")
        innput=int(input("enter 1 to check balance\n""enter 2 to deposit money\n""enter 3 to withdraw money\n"))
        if innput==1:
            checkBalance()

        elif innput==2:
            try:
                amount=float(input("enter amount to deposit :  "))
                deposit(amount)
            except Exception as e:
                print("Error : plz enter valid amt")
                

        elif innput==3:
            try:
                amount=float(input("enter amount to withdraw : "))
                withdraw(amount)
            except Exception as e:
                print("Error : plz enter valid amt")
        else:
            print("invalid input")
            break

bank()

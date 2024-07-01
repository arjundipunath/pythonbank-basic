'-------------------------------BANK--------------------------'
import mysql.connector as c

con = c.connect(host='localhost', user='root', passwd='8547', database='bank')
cr = con.cursor()
'-------------------------------------------------------------'
import time
import getpass  #for pin
import random



def menu():
    print("========== City BANK =============")
    print("1.DEPOSIT")
    print("2.WITHDRAW")
    print("3.CHECK BALENCE")
    print("4.NEW ACCOUNT")
    print("5.CLOSE ACCOUNT")
    print("6.EXIT")

def account():
    bal=1000
    print("------New Account-----")
    name=input("Enter the name: ")
    ph=int(input("Enter phone number: "))
    #passwd= getpass.getpass(prompt='Enter 4 DIGIT PIN: ')
    passwd=int(input("enter 4 digit pin: "))
    accno = random.randint(1000000000, 9999999999)
    t=(name,accno,passwd,ph,bal)
    q='insert into user values(%s,%s,%s,%s,%s)'
    cr.execute(q,t)
    con.commit()
    time.sleep(2)
    print("Account Creation Successful")
    passbook(name,ph,accno)

def passbook(name,ph,accno):
    print('=================== City BANK =====================')
    print("NAME: ",name,    "\tACCOUNT NO: ",accno)
    print("PHONENO:",ph,    "\tPASSWORD: ****")
    print('==================================================')
    



def deposit():
   
   

    accno=int(input("Enter the account no: "))
    passwd=int(input("enter 4 digit pin: "))
    cr.execute('select passwd from user where accno=%s',(accno,))
    c=cr.fetchone()
    pin=c[0]
    con.commit()
    if(passwd==pin):
        amount=int(input("Enter amount to deposit: "))
        cr.execute("UPDATE user SET bal = bal + %s WHERE accno = %s", (amount, accno))
        con.commit()
        print("Transaction Processing........")
        dot='.....................'
        for char in dot:
            print(char, end='', flush=True)  
            time.sleep(0.1)
        print()  
        time.sleep(1)
        print("Transction Completed")
    else:
        print("Invalid password")
    
def check():
    
    accno=int(input("Enter the account no: "))
    passwd=int(input("enter 4 digit pin: "))
    cr.execute('select passwd from user where accno=%s',(accno,))
    c=cr.fetchone()
    p=c[0]
    con.commit()
    if(passwd==p):
        cr.execute('select bal from user where accno=%s',(accno,))
        c=cr.fetchone()
        con.commit()
        if c:
            bal = c[0]
            print(f"Balance: ₹ {bal}")
        else:
            print("Account not found.")
        
    else:
        print("Invalid password")


def withd():
   
    accno=int(input("Enter the account no: "))
    passwd=int(input("enter 4 digit pin: "))
    cr.execute('select passwd from user where accno=%s',(accno,))
    c=cr.fetchone()
    pin=c[0]
    con.commit()
    if(passwd==pin):
        wth=int(input("Enter amount to withdraw: "))
        cr.execute('select bal from user where accno=%s',(accno,))
        c=cr.fetchone()
        con.commit()
        ch=c[0]
        if(wth <= ch):
            cr.execute("UPDATE user SET bal = bal - %s WHERE accno = %s", (wth, accno))
            con.commit()

            print("Transaction Processing.....")
            dot='................'
            for char in dot:
                print(char, end='', flush=True)  
                time.sleep(0.1) 
            print()  

            time.sleep(1)
            print("Transcation Completed")
            
        else:
            print("Insufficnt fund")
    else:
        print("Incorrect password")


def main():
    menu()
    ch=int(input("Enter the choice: "))

    match ch:
        case 1:
             deposit()
             
        case 2:
            withd()

        case 3:
            check()
    
        case 4:
            account()
            
        case 5:
            close()

        case 6:
            print("Exiting....")
            exit()
            
        case default:
           print("Invalid choice")
            
while True:
   
    main()



pin  =  "1234"
balance = 1000

enter_pin  =  input("Enter pin:  ")
if enter_pin  ==  pin:
 
 while True:
    print("\n==== ATM SYSTEM ====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choices = input("Choose an option:  ")
    
    if choices  ==  "1":
     print("Your balance is:",  balance)
     
    elif choices  ==  "2":
        amount = int(input("Enter amount to deposit:  "))
        balance += amount
        print("Deposit went successful!")
        
    elif choices  ==  "3":
        amount = int(input("Enter amount to withdraw:  "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal went successfull!")
        else:
            print("Not enough money")
            
    elif choices  ==  "4":
        print("Thank you for using ATM SYSTEM!")
        break
    
else:
   print("Incorrect PIN.")

       
    

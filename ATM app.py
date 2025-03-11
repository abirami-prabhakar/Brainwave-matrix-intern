
class ATM:
    def __init__(self,balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self,amount):
        self.balance += amount
        return f"${amount} deposited successfully. New Balance: ${self.balance}"

    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient funds. "
        else:
            self.balance -= amount
            return f"${amount} withraw successfully. New balance: ${self.balance}"

def main():
    starting_balance = float(input(" Enter starting balance :"))
    atm = ATM(starting_balance)

    while True:
        print("\nChoose an action:")
        print("1. Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4. Exit")

        choice = input("Enter your choice(1/2/3/4): ")

        if choice == "1":
            print("Your current balance is : $",atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter amount to deposit :"))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the ATM.")
        else:
            print("Invalid choice . Please choose a valid option .")

print("PLease insert your card")
password = 1234
pin=int(input("Enter your atm pin"))
if pin == password:
    pass
else:
    print("wrong pin please try again")

if __name__ == "__main__":
    main()
                
    

            

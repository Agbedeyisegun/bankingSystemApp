class bankingSystemApp():
    def __init__(self, balance: float):
        self.balance = balance
    def deposit(self):
        username = "Agbedeyi S"
        input_username = input("You're Welcome to Pheemyhan Concept Online Banking, What is your Name.. \n")
        if input_username != username:
            print("So sorry we cant authenticate this transactions")
        else:
            confirm_deposit = input(f"Please, do you want to deposit, {input_username}? yes/no:  \n ")
            if confirm_deposit == "yes":
                while True:
                    try:
                        deposit_amount = float(input("Please Enter the amount you want to deposit, \n"))
                        break
                    except ValueError:
                        print("wrong value inputted, try again")

                self.balance += deposit_amount
                initial_name = username.split(" ")
                initial_name2 = initial_name[0]
                print(f"Thanks for banking with Us {initial_name2},"
                f"your new balance is {self.balance} Naira.")
            else:
                print("Thank you for banking with us..")

    def withdraw(self):
        username = "Agbedeyi S"
        input_username = input("You're Welcome to Pheemyhan Concept Online Banking, Please, what is your Name.. \n")
        if input_username != username:
            print("So sorry we cant authenticate this transactions. Bye!!")
        else:
            print(f"You are welcome to out banking Platform {input_username}")
            initial_name = username.split(" ")
            initial_name2 = initial_name[0]
            confirm_withdraw = input(f"Kindly confirm you want to withdraw {initial_name2}, yes/no \n")
            if (confirm_withdraw == "yes"):
                while True:
                    try:
                        withdraw_amount = float(input(f"kindly input your withdrawal amount {initial_name2}.. \n "))
                        break
                    except ValueError:
                        print("Enter a valid input, Please")
                self.balance -= withdraw_amount 
                if withdraw_amount > self.balance:
                    print(f"You dont have enough balance to cover withdrawal amount {initial_name2} \n")
                    overdraft = input("do you want to apply for overdraft to cover the amount you want to withdraw, yes/no \n")
                    if overdraft == "yes":
                        print("A form has been forwarded to your mail box, fill and submit for your overdaft to be processed in 24 Hours, Thanks. \n")
                else:
                    print(f"{initial_name2}, your new balance is {self.balance}, Thanks for banking with us.")
            else:
                print("Thanks for coming, bye!!")       
banking = bankingSystemApp(1000)
banking.deposit()
banking.withdraw()
        
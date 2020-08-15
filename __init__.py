

class BankAccount:
   

    def __init__(self, first_name, last_name, phone_no, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_no = phone_no
        self.bank = bank
        self.balance = 0
        self.withdraw_summary = []
        self.deposit_summary = []
        self.loan_balance = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name, self.phone_no, self.bank)
        return name

    def deposit(self, amount): 
        if amount <= 0:
            print("You cannot deposit zero or negative")
        else:
            self.balance += amount
        print("You deposited {} to {}".format(amount, self.account_name()))
        return 
            
            
    def withdraw(self, amount):
         
        if amount <= 0:
            print("You cannot withdraw zero or negative")
          
        elif amount > self.balance:
            print("You have insufficient balance")
        else:
            self.balance -= amount
        print("You have withdrawn {} from {}".format(amount, self.account_name()))

    def get_balance(self):
   
        return "The balance for {} is {}".format(self.account_name(), self.balance)
    
  
  
    
    def lend_loan(self, loan):
        if loan <= 0:
            print("Invalid request")
        
        else: 
            self.loan_balance += loan
        print("{} borrowed {}".format(self.account_name(), loan))
      
    def pay_loan(self, loan):
        if loan <= 0:
            print("Invalid amount to reduce your loan")
        else:
            self.loan_balance -= loan
        print(" You repaid {}".format(loan))
      
    def deposit_statement(self, amount):
            self.deposit(self, amount)
            return self.deposit_summary.append(amount)
      
      
            def deposit_statement(self, amount):
                    self.deposit(self, amount)
      
            return self.deposit_summary.append(amount)
       
      
    
    
acc1 = BankAccount("Esther", +25491837080, "Herman", "KCB")
print(acc1.phone_no)
acc1.deposit(1000)
acc1.withdraw(2500)
acc1.withdraw(4600)
acc1.deposit(2100)
acc1.deposit(9450)
acc1.lend_loan(8400)
acc1.lend_loan(5300)
acc1.pay_loan(18900)
print(acc1.loan_balance)

print(acc1.deposit_summary)



        
        
        
        
        
from datetime import datetime
class Account:
    def __init__(self, first_name, last_name,phone_no,bank):
        self.self.first_name = first_name
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
        try:
            amount + 1
        except:TypeError
        print("Please enter amount in figures")
        return
        if amount <=0:
            print("You can\'t deposit zero or negative")
        else:
            self.balance += amount
            self.deposits.append(amount)
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
        print("You have deposited {} to {}".format(amount, self.account_name(),formated_time))
        return
    def withdraw(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return
        if amount <= 0:
            print("You can\'t withdraw zero or negative")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount, self.account_name()))
    def get_balance(self):
        return "The balance for {} is {}".format(self.account_name(), self.balance)
    def show_deposit_statements(self):
        for deposit in self.deposits:
            formated_time = time.strftime("%A, %drd %B %Y, %H:%M %p")
            print("{} deposited on {}".format(deposit, formated_time))
    def show_withdrawals_statement(self):
        for withdraw in  self.withdrawals:
            print(withdraw)
    def request_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount <= 0:
            print("You can\'t request for an amount low than zero")
        else:
            self.loan = amount
            print("You have been given a loan of {}".format(amount))
    def repay_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount <= 0:
            print("Too low to repay your amount")
        elif self.loan == 0:
            print("You don't have a loan at the moment")
        elif amount > self.loan:
            print("Your loan is {} please enter an amount that is less or equal".format(self.loan))
        else:
            self.loan == amount
            time ==datetime.now()
            repayment={
                  "time":time
                  "amount":amount
            }
            self.loan -= amount
            print("You have repaid you loan with {} your balance is {}".format(amount, self.loan))
    def repay_loan_statement(self)
        for repayment in self.loan_repayments:
            time= repayment["time"]
            amount=repayment["amount"]
            formated_time=self.get_formatted_time(time)
            statement="You repaid {} on {}".format(amount,formated_time)
            print (statement0
class BankAccount(Account):
    def __init__(self,first_name,last_name,phone_no,bank)
    self.bank = bank
    super().__init__(first_name,last_name,phone_no)
class MobileMoneyAccount(Account):
    def __init__(self,first_name,last_name,phone_no,service_provider)
    self.service_provider=service_provider
    self.airtime =[]
        super().__init__(first_name,last_name,phone_no)
    def buy_airtime(self,amount):
        try:
            amount +1
        except TypeError:
            print("Please enter amount in figures")
            return
        if amount >self.balance:
            print ("You should have enough balance")
        else:
            self.balance-= amount
            time =datetime.now()
            "time":time
            "airtime":amount
        }
        self.airtime.append(airtime)
        print("You\'ve bought airtime worth {} on {}".format(amount,self.get_formatted_time(time)))
        def pay_bill(self,amount):
        try:
            amount +1
            except TypeError:
                print("Please enter amount figures")
                return
        if amount>self.balance:
            print("Should have enough balance")
        else:
            self.balnce -= amount
            time=datetime.now()
            "time":time
            "bill":amount
        }
        self.bill.append(bill)
        print("You\'ve paid bill worth {} on {} to {}".format(amount,self,get_formatted_time(time)))
    def send_money(self.amount):
    try:
            amount +1
            except TypeError:
                print("Please enter amount in figures")
        if amount >self.balance:
            print("You have enough balance")
        else:
            self.balance -=amount
            time = datetime .now()
            sendmoney{
            "time":time
            "send_money":amount
    }
    self.send_money.append(send_money)
    print ("You\'ve sent {} money to {} on {}".format(amount,self.get_formatted_time(time)))
    def recieve_money(self,amount):
        time=datetime.now()
        recieve_money{
            "time":time,
            "recieve_money":amount
            }
        self.recieve_money.append(recieve_money)
        print("You\'ve recieved {} on {} and your new balance is {}".format(amount,get_formated_time(time),self.balance))
acc1 = BankAccount("Ringo" ,"Martinez",+2547093886720,"Equity")
acc1.first_name
acc1.deposit(100500)
print(acc1.first_name)
acc1.deposit(200500)
print(acc1.balance)
acc1.request_loan(8000)
acc1.repay_loan(3000)
acc1.repay_loan(45000)
acc1.repay_loan(40000)
print(acc1.loan)
print(acc1.balance)
acc1.request_loan(7040)
acc1.deposit(700)
acc1.deposit("eighty")
acc1.deposit(3556)
acc1.deposit(1504)
acc1.show_deposit_statements()
acc1.request_loan("eighty")
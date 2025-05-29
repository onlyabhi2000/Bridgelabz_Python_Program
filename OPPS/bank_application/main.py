class Account:
    def __init__(self ,name , balance , phone):
        self.name = name
        self.balance = balance
        self.phone =phone

    def __str__(self):
        pass



    def add_money(self,money):
        new_balance = self.balance+money
        return new_balance
    
    def withdrawl(self, money):
        if self.balance>money:
            new_balance = self.balance-money
            return new_balance
        
acc1= Account("abhi" , 1000 , 98769878)
acc2= Account("shaek" , 5000 , 87689098)


added1=acc1.add_money(2000)
print(added1)

withdrawl2 = acc2.withdrawl(350)
print(withdrawl2)


    
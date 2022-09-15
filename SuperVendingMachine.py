class VendingMachine:
    pass
    # init method
    def __init__(self, name):
        self.name = name
        print(f"Welcome to {self.name}!")

        self.balance = 0 # assume start with $0
        self.inventory = {"Coke": 10, "Sprite": 10, "Water": 10}
        self.prices = {"Coke": 1.50, "Sprite": 1.50, "Water": 1.00}
        self.transactions = {}

    def show_inventory(self):
        for item in self.inventory:
            print(f"{item}: {self.inventory[item]} units")
    
    def show_prices(self):
        for item in self.prices:
            print(f"{item}: ${self.prices[item]}")
        
    def show_inventory_with_prices(self):
        for item in self.inventory:
            print(f"{item}: {self.inventory[item]} units, ${self.prices[item]}")

    def change_price(self, item, new_price):
        self.prices[item] = new_price

    def add_money(self, amount):
        self.balance += amount

    def show_balance(self):
        print(f"you have ${self.balance} in your account")

    def add_item(self, item, quantity):
        self.inventory[item] += quantity
    
    def buy_item(self, item):
        # try catch block
        try:
            if self.inventory[item] > 0:
                if self.balance >= self.prices[item]:
                    self.balance -= self.prices[item]
                    self.inventory[item] -= 1
                    print(f"Enjoy your {item}")
                    self.transactions[item] = self.transactions.get(item, 0) + 1
                else:
                    print("Insufficient funds")
            else:
                print("Item not available")
        except:
            print("We do not have that item")

    def exit(self):
        print(f"Thanks for using {self.name}!")
        print(f"Here is your ${self.balance} change")
        self.balance = 0

    # store list of transations
    def show_transactions(self):
        for item in self.transactions:
            print(f"number of {item}s bought: {self.transactions[item]}")

    # help method
    def help(self):
        print("Commands:")
        print("show inventory")
        print("show prices")
        print("show inventory with prices")
        print("change price")
        print("add money")
        print("show balance")
        print("add item")
        print("buy item")
        print("leave")
        print("show transactions")

    #TODO
    # implement help
    # implement precise change





# if name is main
if __name__ == "__main__":
    # create vending machine
    alley_machine = VendingMachine("王中国的小贩")
    alley_machine.show_inventory_with_prices()
    alley_machine.add_money(10)
    alley_machine.show_balance()
    alley_machine.buy_item("Coke")
    alley_machine.show_balance()

    alley_machine.buy_item("Water")
    alley_machine.show_transactions()

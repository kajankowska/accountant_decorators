# import sys

class Manager:
    def __init__(self):
        self.callbacks = {}
        self.actions = {}
        self.balance = 0

    def assign(self, action, count):
        def decorate(callback):
            self.callbacks[action] = callback
            self.actions[action] = count
        return decorate


manager = Manager()


@manager.assign("balance", 2)
def balance(data):
    amount = data[0]
    comment = data[1]
    if manager.balance + amount < 0:
        print("No funds in the account.")
    else:
        manager.balance += amount


@manager.assign("purchase", 3)
def purchase(data):
    quantity = data[0]
    product = data[1]
    price = data[2]
    if manager.balance < int(price * quantity):
        print("Insufficient funds to purchase.")
    if product in manager.callbacks:
        manager.callbacks[product] += quantity
    else:
        manager.callbacks[product] = quantity
    manager.balance -= price * quantity
    if price < 0 or quantity < 0:
        print("Error! Negative value.")


@manager.assign("sales", 3)
def sales(data):
    value = data[0]
    comment = data[1]
    price = data[2]

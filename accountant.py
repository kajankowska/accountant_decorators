import sys
from accountant_manager import Manager, File

manager = Manager()
file = File(filepath=sys.argv[1])
file.readfile()


@manager.assign("balance", 2)
def balance(data):
    amount = int(data[0])
    comment = data[1]
    if manager.balance + amount < 0:
        print("No funds in the account.")
    else:
        manager.balance += amount


@manager.assign("purchase", 3)
def purchase(data):
    product = data[0]
    price = int(data[1])
    quantity = int(data[2])
    if manager.balance < price * quantity:
        print("Insufficient funds to purchase.")
    if product in manager.warehouse:
        manager.warehouse[product] += quantity
    else:
        manager.warehouse[product] = quantity
    manager.balance -= price * quantity
    if price < 0 or quantity < 0:
        print("Error! Negative value.")


@manager.assign("sales", 3)
def sales(data):
    product = data[0]
    price = int(data[1])
    quantity = int(data[2])
    if product not in manager.warehouse:
        print("Item out of stock.")
    if quantity > manager.warehouse[product]:
        print("Insufficient stock.")
    else:
        manager.warehouse[product] -= quantity
    if price < 0 or quantity < 0:
        print("Error! Negative value.")
        manager.balance += price * quantity


manager.write_history(file.tasks)

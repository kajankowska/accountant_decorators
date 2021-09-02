from accountant_manager import Manager, File

manager = Manager()
file = File()


@manager.assign("balance", 2)
def balance(data):
    amount = data[0]
    comment = data[1]  # comment?
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
    quantity = data[0]
    product = data[1]
    price = data[2]
    if product not in manager.callbacks:
        print("Item out of stock.")
    if manager.callbacks[product] < quantity:
        print("Insufficient stock.")
    else:
        manager.callbacks[product] -= quantity
    if price < 0 or quantity < 0:
        print("Error! Negative value.")
        manager.balance += price * quantity

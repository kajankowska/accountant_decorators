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
    value = data[0]
    comment = data[1]

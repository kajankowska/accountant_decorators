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


class File:
    def __init__(self, filepath):
        self.filepath = filepath
        self.actions = []

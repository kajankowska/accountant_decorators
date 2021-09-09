class Manager:
    def __init__(self):
        self.callbacks = {}
        self.actions = {}
        self.history = []
        self.warehouse = {}
        self.balance = 0

    def assign(self, action, count):
        def decorate(callback):
            self.callbacks[action] = callback
            self.actions[action] = count
        return decorate

    def write_history(self, activities):
        while activities:
            act = activities.pop(0)
            data = []
            if act in self.actions:
                for i in range(self.actions[act]):
                    data.append(activities.pop(0))
                self.history.append((act, data))

    def run(self):
        for act, data in self.history:
            if act in self.callbacks:
                self.callbacks[act](data)


class File:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = []

    def readfile(self):
        with open(self.filepath, "r", encoding="utf-8") as file:
            for line in file:
                self.tasks.append(line.strip())

    def savefile(self):
        with open(self.filepath, "w", encoding="utf-8") as file:
            for line in self.tasks:
                file.write(line + "\n")

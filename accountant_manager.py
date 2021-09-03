class Manager:
    def __init__(self):
        self.callbacks = {}
        self.actions = {}
        self.history = []
        self.balance = 0

    def assign(self, action, count):
        def decorate(callback):
            self.callbacks[action] = callback
            self.actions[action] = count
        return decorate

    def history(self, activities):
        while activities:
            act = activities.pop()
            data = []
            if act in self.actions_args:
                for i in range(self.action_args[act]):
                    data.append(activities.pop())

    def execute(self, action, *args, **kwargs):
        if action not in self.actions:
            pass
        else:
            self.actions[action][0](self, *args, **kwargs)


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

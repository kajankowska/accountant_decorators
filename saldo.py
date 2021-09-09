from accountant_decorators import manager
import sys

action = "balance"
amount = int(sys.argv[2])
comment = sys.argv[3]
task = (action, [amount, comment])
manager.history.append(task)

manager.run()
print(manager.balance)

with open(sys.argv[1], "a", encoding="utf-8") as file:
    file.write("\n" + action + "\n")
    file.write(str(amount) + "\n")
    file.write(comment + "\n")

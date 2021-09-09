from accountant_decorators import manager
import sys

action = "sales"
product = sys.argv[2]
price = int(sys.argv[3])
quantity = int(sys.argv[4])

task = (action, [product, price, quantity])
manager.history.append(task)

manager.run()

with open(sys.argv[1], "a", encoding="utf-8") as file:
    file.write("\n" + action + "\n")
    file.write(product + "\n")
    file.write(str(price) + "\n")
    file.write(str(quantity) + "\n")

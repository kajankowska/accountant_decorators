from accountant_decorators import manager
import sys

manager.run()
products = sys.argv[2:]

for product in products:
    if product in manager.warehouse:
        print("{}: {} ".format(product, manager.warehouse[product]))
    else:
        print("{}: 0 ".format(product))

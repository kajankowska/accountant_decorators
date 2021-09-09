from accountant_decorators import manager
import sys

manager.run()
print("Account balance: ", manager.balance, "\nThe program has finished.")

with open(sys.argv[1], "a", encoding="utf-8") as file:
    file.write("\n" + "koniec")

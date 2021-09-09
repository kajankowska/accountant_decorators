from accountant_decorators import manager

manager.run()

print("\nEnter the scope of operations (from, to):")
start = int(input())
end = int(input())
print(manager.history[start:end])

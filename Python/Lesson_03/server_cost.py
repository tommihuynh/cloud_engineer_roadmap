servers = int(input(f"Number of servers: "))
monthly_cost = float(input(f"Monthly cost per server: "))

print()
print("===== Cloud Cost =====")
print()
print(f"Servers: {servers}")
print(f"Cost per server: ${monthly_cost: .2f}")
print()
print(f"Total monthly cost: ${servers*monthly_cost: .2f}")


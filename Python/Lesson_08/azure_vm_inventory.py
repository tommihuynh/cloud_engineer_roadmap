vms = []

for i in range(3):
    vm = input(f"Virtual Machine {i + 1}: ")
    vms.append(vm)

print()

print("===== Azure VM Inventory =====")
for vm  in vms:
    print(vm)

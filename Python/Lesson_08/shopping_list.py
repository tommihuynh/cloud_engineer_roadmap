

shopping = []
while True:
    item = input("Add an item (or type 'done'): ")
    if item.lower() == "done":
        break
    shopping.append(item)

shopping.sort()
print("\nShopping List")

for item in shopping:
    print(f"- {item}")
print("\nTotal items: {len(shopping)}")

#Initializing function blocks for repeatablity
def display_items(items):
    print("\nAvailable Items:")
    for idx in range(len(items)):
        print(f"{idx + 1}. {items[idx][0]} - PHP {items[idx][1]:.2f} - Stock: {items[idx][2]}")

def generate_receipt(cart, items, payment):
    print("\nRECEIPT")
    total = 0
    print(f"{'Item':<20}{'Price':<10}")
    for i in range(len(cart)):
        item_idx, qty = cart[i]
        item_name = items[item_idx][0]
        price = items[item_idx][1]
        subtotal = price * qty
        total += subtotal
        print(f"{item_name:<20}PHP {subtotal:.2f}")
    change = payment - total
    print(f"\n{'Total':<20}PHP {total:.2f}")
    print(f"{'Payment':<20}PHP {payment:.2f}")
    print(f"{'Change':<20}PHP {change:.2f}")
    print("Thank you for shopping with us!")

# Define available items as a list of lists
items = [
    ["Rice (1kg)", 40, 50],
    ["Canned Tuna", 30, 20],
    ["Milk (1L)", 50, 30],
    ["Eggs (dozen)", 100, 10],
    ["Medicine", 500, 10],
    ["Shampoo", 150, 15],
    ["Toothpaste", 80, 25],
    ["Soap", 40, 40],
    ["Cooking Oil", 70, 20],
    ["Detergent", 90, 20]
]

#Basket
cart = []

#Introduction, display of available items
print("Good day! Welcome to our store.")
while True:
    display_items(items)

    choice = input("\nWhat would you like to add to your cart? (Type the number or 'done' to checkout): ")

    if choice.lower() == "done":
        if not cart:
            print("Your cart is empty. Thank you for visiting!")
            exit()
        break

    if not choice.isdigit() or int(choice) not in range(1, len(items) + 1):
        print("Sorry, this item is not available.")
        continue

    item_idx = int(choice) - 1
    item_name, price, stock = items[item_idx]

    if stock <= 0:
        print("Sorry, this item is already out of stock.")
        continue

    quantity = input(f"Enter quantity for {item_name} (Available: {stock}): ")

    if not quantity.isdigit() or int(quantity) <= 0 or int(quantity) > stock:
        print("Invalid quantity. Please enter a number within the available stock.")
        continue

    quantity = int(quantity)
    items[item_idx][2] -= quantity
    cart.append([item_idx, quantity])

    print(f"Added {quantity} x {item_name} to your cart.")

while True:
    print("\nThis is the summary of your cart:")
    total = 0
    for i in range(len(cart)):
        item_idx, qty = cart[i]
        item_name = items[item_idx][0]
        price = items[item_idx][1]
        subtotal = price * qty
        total += subtotal
        print(f"{item_name}: {qty} x PHP {price:.2f}")
    print(f"\nTotal Amount: PHP {total:.2f}")

    action = input("Proceed to payment?\n1. Yes\n2. Back\nChoose: ")

    if action == "2":
        while True:
            display_items(items)

            choice = input("\nWhat would you like to add to your cart? (Type the number or 'done' to checkout): ")

            if choice.lower() == "done":
                break

            if not choice.isdigit() or int(choice) not in range(1, len(items) + 1):
                print("Sorry, this item is not available.")
                continue

            item_idx = int(choice) - 1
            item_name, price, stock = items[item_idx]

            if stock <= 0:
                print("Sorry, this item is already out of stock.")
                continue

            quantity = input(f"Enter quantity for {item_name} (Available: {stock}): ")

            if not quantity.isdigit() or int(quantity) <= 0 or int(quantity) > stock:
                print("Invalid quantity. Please enter a number within the available stock.")
                continue

            quantity = int(quantity)
            items[item_idx][2] -= quantity
            cart.append([item_idx, quantity])

            print(f"Added {quantity} x {item_name} to your cart.")
        continue
    elif action == "1":
        break
    else:
        print("Invalid choice. Please choose again.")

payment = 0
while True:
    total = 0
    for i in range(len(cart)):
        item_idx, qty = cart[i]
        price = items[item_idx][1]
        total += price * qty

    payment_input = input("How much is your payment?: PHP ")
    if not payment_input.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a numeric value.")
        continue

    payment = float(payment_input)
    if payment < total:
        print(f"Insufficient payment. Your total is PHP {total:.2f}.")
        continue
    break

generate_receipt(cart, items, payment)

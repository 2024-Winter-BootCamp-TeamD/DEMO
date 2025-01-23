# def shopping_cart():
#     cart = {}
#     while True:
#         action = input("Enter 'add' to add an item, 'remove' to remove an item, 'view' to view cart, or 'exit' to quit: ")
#         if action == 'add':
#             item = input("Enter the item name: ")
#             quantity = input("Enter the quantity: ")
#             try:
#                 quantity = int(quantity)
#             except ValueError:
#                 print("Quantity must be a number.")
#                 continue
#             if item in cart:
#                 cart[item] += quantity
#             else:
#                 cart[item] = quantity
#         elif action == 'remove':
#             item = input("Enter the item name to remove: ")
#             if item in cart:
#                 del cart[item]
#             else:
#                 print(f"Item '{item}' not found in cart.")
#         elif action == 'view':
#             print("Your shopping cart:")
#             for item, quantity in cart.items():
#                 print(f"- {item}: {quantity}")
#         elif action == 'exit':
#             print("Exiting shopping cart.")
#             break
#         else:
#             print("Invalid action. Please try again.")
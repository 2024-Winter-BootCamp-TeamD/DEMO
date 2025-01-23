# def calculator():
#     print("Simple Calculator")
#     print("Operations: add, subtract, multiply, divide")
#     while True:
#         operation = input("Enter operation (or 'exit' to quit): ")
#         if operation == 'exit':
#             print("Exiting calculator.")
#             break
#         if operation not in ('add', 'subtract', 'multiply', 'divide'):
#             print("Invalid operation. Try again.")
#             continue
#
#         try:
#             num1 = float(input("Enter the first number: "))
#             num2 = float(input("Enter the second number: "))
#         except ValueError:
#             print("Invalid input. Please enter numbers only.")
#             continue
#
#         if operation == 'add':
#             result = num1 + num2
#         elif operation == 'subtract':
#             result = num1 - num2
#         elif operation == 'multiply':
#             result = num1 * num2
#         elif operation == 'divide':
#             if num2 == 0:
#                 print("Error: Cannot divide by zero.")
#                 continue
#             result = num1 / num2
#
#         print(f"The result of {operation} is: {result}")
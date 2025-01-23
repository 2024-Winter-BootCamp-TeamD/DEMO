# def process_file_data(file_name):
#     try:
#         with open(file_name, 'r') as file:
#             data = file.readlines()
#     except FileNotFoundError:
#         print(f"Error: File '{file_name}' not found.")
#         return
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return
#
#     word_count = 0
#     line_count = 0
#     for line in data:
#         line_count += 1
#         word_count += len(line.split())
#
#     print(f"File '{file_name}' has {line_count} lines and {word_count} words.")
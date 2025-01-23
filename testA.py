# def manage_student_scores():
#     students = {}
#     while True:
#         action = input("Enter 'add' to add a student, 'view' to view all, or 'exit' to quit: ")
#         if action == 'add':
#             name = input("Enter the student's name: ")
#             scores = input("Enter the student's scores separated by commas: ").split(',')
#             scores = [int(score.strip()) for score in scores]
#             students[name] = scores
#         elif action == 'view':
#             for student, scores in students.items():
#                 print(f"Student: {student}, Scores: {scores}, Average: {sum(scores) / len(scores):.2f}")
#         elif action == 'exit':
#             break
#         else:
#             print("Invalid action. Please try again.")
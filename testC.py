# import re
#
# def validate_and_extract_email(email):
#     email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if not re.match(email_pattern, email):
#         return {"valid": False, "message": "Invalid email format."}
#
#     local_part, domain = email.split('@')
#     return {"valid": True, "local_part": local_part, "domain": domain}
#
# def process_emails(email_list):
#     for email in email_list:
#         result = validate_and_extract_email(email)
#         if result['valid']:
#             print(f"Email: {email}, Local Part: {result['local_part']}, Domain: {result['domain']}")
#         else:
#             print(f"Error: {result['message']} - {email}")
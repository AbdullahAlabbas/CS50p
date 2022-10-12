from  validator_collection import validators


email = input("What's your email address?")
try:
    valid_email = validators.email(email)
    print("Valid")
except:
    print("Invalid")
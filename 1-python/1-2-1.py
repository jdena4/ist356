Password = "secret"
MAX_ATTEMPTS = 5
success = False

for attempt in range(MAX_ATTEMPTS):

    your_password = input("Enter password: ")
    if your_password == Password:
        print("Access granted.")
        success = True
        break
    else:
        print("Invalid password.") 
        print(f"Attempt {attempt + 1} of {MAX_ATTEMPTS}")

if not success:
    print("You are locked out.")

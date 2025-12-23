import string

password = input("Enter your password: ")
    # Initialize criteria flags
has_upper = 0
has_lower = 0
has_digit = 0
has_special = 0

    # Check each character in the password
for char in password:
        if char.isupper():
            has_upper = 1
        elif char.islower():
            has_lower = 1
        elif char.isdigit():
            has_digit = 1
        elif char in "!@#$%^&*()-_+=<>?/\\|{}[]~`":
            has_special = 1

    # Check password length
if len(password) >= 8:
        length_ok = 1
else:
        length_ok = 0

    # Count how many conditions are true
count = 0
if length_ok==1:
        count += 1
if has_upper==1:
        count += 1
if has_lower==1:
        count += 1
if has_digit==1:
        count += 1
if has_special==1:
        count += 1

    # Evaluate strength
if count == 5:
        print("Strong password 💪")
elif count >= 3:
        print("Moderate password ⚠️")
else:
        print("Weak password ❌")


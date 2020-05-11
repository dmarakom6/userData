##Account generator v1.0
##Ctrl+C is not allowed!
##info: www.github.com/dmarakom

print("Welcome!")

def start():
    create_new_pass = input("Would you like to create a new account?\n[Y/N]: ").lower()
    if create_new_pass in ["yes", "y"]:
        generate()
    else:
        print("Canceled.")


def generate():
    import same
    from same import users
    print()
    email = input("Please enter your email: ")
    if email in users:
        print("Email already exists.")
        print("canceled.")
        exit()
    elif "@" not in email:
        print("That email was not accurate.")
        exit()
    elif "." not in email:
        print("Username and email cannot be the same.")
        exit()
    username = input("Please enter a username: ")
    if username in users:
        print("Username already exists.")
        print("canceled.")
        exit()
    if username == email:
        print("That input was invalid.")
        print("canceled.")
        exit()
    import random
    chars = "1234567890qwertyuiopasdfghjklzxcvbnm@!#*_"
    letters = "qwertyuipasdfghjklzxcvbnm"
    caps = letters.upper()
    nums = "1234567890"
    num = 1
    length = int(input("Password lengh?(Recommended: 6)- "))
    if length == 0:
        print("Canceled.")
        exit()
    numbers = input("Would you like your password to contain numbers\nand special characters?- ").lower()

    if numbers in ["yes", "y"]:
        for p in range(num):
            password = ""
            for c in range(length):
                password += random.choice(chars)

    elif numbers in ["no", "n"]:
        for p in range(num):
            password = ""
            for c in range(length):
                password += random.choice(letters)

    capitals = input("Would you like your password to include only capital letters?(Recommended)- ").lower()
    if capitals in ["yes", "y"]:
        for p in range(num):
            password = ""
            for c in range(length):
                password += random.choice(caps)
    elif capitals in ["no", "n"]:
        pass


    else:
        print("Input was invalid. Password was not successfully generated.")

    print()
    print(f"Your password is: {password}")


    verify = input("Verify password: ")
    if verify == password:
        import same
        from same import users
        generated = print(f"Password successfully generated for new account {email}!")
        acc_id = random.choice(nums) + random.choice(nums) + random.choice(nums)
        while acc_id in users:
            acc_id += 1
        save = open('userdata.txt', 'a')

        line = f"{acc_id};{username};{email};{password}\n"
        save.write(line)
        save.close()
    else:
        print("Verification was not correct. Password was not successfully generated.")
        del password
        exit()


##run
start()

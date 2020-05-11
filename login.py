##login
def ask():
    import same
    from same import users
    global enter_name, enter_pass
    enter_name = input("Enter your username: ")
    enter_pass = input("Enter your password: ")
    ##for each user in userdata.txt
    for i in range(len(users)):
        if users[i][1] == enter_name and users[i][3] == enter_pass:
            loginacc()
            break
    else:
        # User login has failed
        import datetime
        date = datetime.datetime.now()
        save = open('loginattempt.txt', 'a')
        save.write("DATE: ")
        save.write(str(date))
        save.write(" ")
        save.write("FAILED ATTEMPT: ")
        save.write("\n")
        save.write("USR: ")
        save.write(enter_name)
        save.write(" ")
        save.write("PASS: ")
        save.write(enter_pass)
        save.write("\n")
        print("That account doesn't exist.")
        new = input("Would you like to create a new one? ").lower()
        if new in ["yes", "y"]:
            import signup
        elif new in ["no", "n"]:
            exit()
        else:
            print("That didn't work.")
    

##login
def loginacc():
    import datetime
    save = open('loggedin.txt', 'a')
    date = str(datetime.datetime.now())
    save.write("DATE:")
    save.write(str(date))
    save.write(" ")
    save.write("USR: ")
    save.write(enter_name)
    save.write(" ")
    save.write("PASS: ") 
    save.write(enter_pass)
    print("Welcome!")

        #import app content here


##run:
ask()
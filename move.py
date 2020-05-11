print("Welcome!")
move = input("Do you have an account? ").lower()
if move in ["yes", "y"]:
    import login
else:
    import signup
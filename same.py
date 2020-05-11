##if email or username are the same::::::
read_user_data = open('userdata.txt', 'r')
users = (read_user_data.read().splitlines())

for i in range(len(users)):
    users[i] = users[i].split(";")

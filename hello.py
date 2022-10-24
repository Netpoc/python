username = input("Username: ")
password = input("Password: ")
if ((username == "Admin" or username == "admin") and (password == "1234@admin")):
    print(f"Hello, you are logged in as Admin")
else:
    print(f"Invalid username or password")   
import os

file_name = "passwords.txt"

def add_password():
    site = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    with open(file_name, "a") as file:
        file.write(site + "," + username + "," + password + "\n")
    print("Password saved successfully")

def view_passwords():
    if not os.path.exists(file_name):
        print("No passwords stored yet")
        return
    with open(file_name, "r") as file:
        for line in file:
            site, username, password = line.strip().split(",")
            print("Website:", site)
            print("Username:", username)
            print("Password:", password)
            print("-----------")

while True:
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        print("Exiting Password Manager")
        break
    else:
        print("Invalid choice")

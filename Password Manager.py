passwords = {}

while True:
    print("\n1. Add Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        site = input("Enter website: ")
        password = input("Enter password: ")
        passwords[site] = password
        print("Password saved!")

    elif choice == "2":
        for site, password in passwords.items():
            print(site, ":", password)

    elif choice == "3":
        break

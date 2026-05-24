from vault import vault_init, vault_load
from accounts import add_account, list_accounts, get_password


def main():
    file_path = input("What path do you wanna save the vault at")
    master_password = input("Enter master password: ")
    while True:

        menu = int(input("What do you wanna do: Create a Vault? press 1," \
        "Add account? press 2, List Account? press 3, Get Password press 4, for exit press 5"))
        if menu == 1:
            master_password = input("Enter master password: ")
            vault_init(master_password, file_path)
        elif menu == 2:
            master_password = input("Enter master password: ")
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            add_account(master_password, file_path, service, username, password)

        elif menu == 3:
            master_password = input("Enter master password: ")
            list_accounts(master_password, file_path)

        elif menu == 4:
            master_password = input("Enter master password: ")
            service = input("Enter service name: ")
            password = get_password(master_password, file_path, service)
            print("Password:", password)

        elif menu == 5:
            break


main()
        




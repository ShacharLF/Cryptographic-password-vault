from vault import vault_load, vault_save

def add_account(master_password, file_path, service, username, password):
    vault_data, key, salt = vault_load(master_password, file_path)
    if vault_data is None:
        return
    else:

        new_account = {
            "service": service,
            "username": username,
            "password": password
        }

        vault_data["accounts"].append(new_account)
        vault_save(vault_data, key, salt, file_path)
    

def list_accounts(master_password, file_path):
    vault_data, _ , _ = vault_load(master_password, file_path)
    if vault_data is None:
        return
    else:
        for account in vault_data["accounts"]:
            service = account["service"]
            username = account["username"]

            print(service, username)


def get_password(master_password, file_path, service):
    vault_data, _ , _ = vault_load(master_password, file_path)
    if vault_data is None:
        return None
    else:
        for account in vault_data["accounts"]:
            if service == account["service"]:
             return account["password"]


    return None







        
from crypto_utils import generate_salt, Key_Derive, encrypt, decrypt
import json


def vault_init(master_password, file_path):
    salt = generate_salt()
    key = Key_Derive(master_password, salt)

    vault_data = {

        "accounts": []
    }

    plaintext_bytes = json.dumps(vault_data).encode()
    nonce, ciphertext = encrypt(plaintext_bytes, key)
    with open(file_path, "wb") as f:
        f.write(salt+nonce+ciphertext)


def vault_load(master_password, file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        salt = data[:16]
        nonce = data[16:28]
        ciphertext = data[28:]
        key = Key_Derive(master_password,salt)


        try:
            plaintext = decrypt(nonce, ciphertext, key)
        except Exception:
            print("Wrong master password!")
            return None, None, None

        vault_data = json.loads(plaintext)
    return vault_data, key, salt

def vault_save(data_dict, key, salt, file_path):
    dict_bytes = json.dumps(data_dict).encode()
    nonce, ciphertext = encrypt(dict_bytes, key)

    with open(file_path, "wb") as f:
        f.write(salt+nonce+ciphertext)









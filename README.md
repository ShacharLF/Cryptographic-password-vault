Secure Password Manager (Python)

A secure, local password manager built in Python using modern cryptographic practices such as AES-GCM encryption and Argon2 key derivation.

This project demonstrates how sensitive data can be securely stored, encrypted, and managed locally without relying on external services.

---

Features

- Create an encrypted password vault
- Secure master password authentication
- Add new accounts (service, username, password)
- List stored accounts
- Retrieve stored passwords
- Full encryption using AES-GCM
- Key derivation using Argon2
- Random salt and nonce for each vault

---

Security Design

This project follows secure design principles:

- **AES-GCM encryption** for confidentiality + integrity
- **Argon2 key derivation** from master password
- **Random salt (16 bytes)** stored in vault file
- **Random nonce (12 bytes)** per encryption
- No plaintext passwords stored on disk
- No encryption keys stored anywhere
- Vault is decrypted only in memory at runtime

Vault file structure:

[salt (16 bytes)] + [nonce (12 bytes)] + [ciphertext]

---

Project Structure

main.py # CLI interface
vault.py # Vault creation, load, save logic
accounts.py # Add/list/get password functions
crypto_utils.py # Encryption + key derivation utilities



How to Run

1. Install dependencies

pip install cryptography argon2-cffi


2. Run the program


python main.py


---

How It Works

1. User creates a vault with a master password
2. A cryptographic key is derived using Argon2 + salt
3. All data is stored as encrypted JSON
4. Each operation:
   - decrypts vault
   - modifies data in memory
   - re-encrypts and saves

---

Security Notes

- The master password is never stored
- The encryption key is derived at runtime only
- Vault file contains only encrypted data
- This project is for educational purposes

---

Technologies Used

- Python 3
- AES-GCM (cryptography library)
- Argon2 (secure KDF)
- JSON serialization

---

Future Improvements

- Password strength checker
- Clipboard auto-clear for copied passwords
- GUI interface (Tkinter / PyQt)
- Password generator
- Biometric unlock support

---

##  Author

Built as a cybersecurity learning project focusing on encryption, secure storage, and secure software design principles.


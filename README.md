# Caesar Cipher Encryption and Decryption with Python

This repository demonstrates the implementation of the Caesar Cipher encryption and decryption in Python. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

## Prerequisites

There are no additional dependencies required to run this project, as it only relies on basic Python functionality. You only need Python installed on your machine.

## Caesar Cipher Overview

The **Caesar Cipher** is one of the oldest and simplest encryption techniques. It works by shifting each letter of the plaintext by a certain number of positions in the alphabet.

- **Encryption**: Each letter in the plaintext is replaced by the letter that appears after it by a fixed number of positions in the alphabet (the "shift").
- **Decryption**: To decrypt the message, you simply shift the letters in the opposite direction by the same amount.

## Code Walkthrough

### Caesar Encryption

The encryption function shifts each letter of the plaintext by a specified number of positions (shift value) in the alphabet:

```python
def caesar_encrypt(plaintext, shift):
    encrypted = ''
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted
```

- It checks if each character is a letter.
- It calculates the shifted position by converting the character to its ASCII value (`ord()`), applies the shift, and converts it back to a character (`chr()`).
- Non-alphabetical characters (spaces, punctuation, etc.) remain unchanged.

### Caesar Decryption

Decryption is simply the reverse of encryption. The same function `caesar_encrypt` is used with the negative shift value:

```python
def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)
```

### Example Usage

Here’s an example of how to use the Caesar Cipher functions to encrypt and decrypt a message:

```python
plaintext = "HELLO"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
decrypted = caesar_decrypt(ciphertext, shift)

print("Caesar Cipher - Encrypted:", ciphertext)
print("Caesar Cipher - Decrypted:", decrypted)
```

In this example, the plaintext message `"HELLO"` is encrypted with a shift of 3, resulting in the ciphertext. The ciphertext is then decrypted back to the original message using the same shift value.

## Example Output

```text
Caesar Cipher - Encrypted: KHOOR
Caesar Cipher - Decrypted: HELLO
```

- The plaintext `"HELLO"` is shifted by 3 positions to become `"KHOOR"`.
- Decrypting `"KHOOR"` with the same shift (3) gives us the original message `"HELLO"`.

## How to Run the Code

1. Clone the repository:

```bash
git clone https://github.com/Jsujanchowdary/Caesar-Cipher-Encryption-and-Decryption-with-Python.git
```

2. Navigate to the project directory:

```bash
cd caesar-cipher-python
```

3. Run the script:

```bash
python caesar_cipher.py
```

## Conclusion

This project demonstrates a simple implementation of the Caesar Cipher in Python. Although it is not secure by modern cryptographic standards, it is an excellent introductory example for understanding encryption and decryption.

---

### Example Directory Structure

```plaintext
caesar-cipher-python/
│
├── caesar_cipher.py   # Python script for Caesar Cipher encryption and decryption
├── README.md          # Project documentation
└── requirements.txt   # Python dependencies (if needed, but for this project, not required)
```

---

### Notes

- You can experiment with different shift values to see how the encryption and decryption process changes.
- The Caesar Cipher is highly vulnerable to brute-force attacks, as there are only 26 possible shifts. However, it's a good educational tool for understanding basic encryption principles.

---

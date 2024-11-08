def caesar_encrypt(plaintext, shift):
    encrypted = ''
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# Example usage:
plaintext = "HELLO"
shift = 3
ciphertext = caesar_encrypt(plaintext, shift)
decrypted = caesar_decrypt(ciphertext, shift)
print("Caesar Cipher - Encrypted:", ciphertext)
print("Caesar Cipher - Decrypted:", decrypted)

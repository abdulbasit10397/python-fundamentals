import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def aes_encrypt(string_to_encrypt, key, iv):
    try:
        key = base64.b64decode(key)
        iv = base64.b64decode(iv)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_string = pad(string_to_encrypt.encode('utf-8'), AES.block_size)
        ciphertext = cipher.encrypt(padded_string)
        return base64.b64encode(ciphertext).decode('utf-8')

    except:
        print("#### Error encrypting msg")

    return None


def aes_decrypt(encrypted_string, key, iv):
    try:
        key = base64.b64decode(key)
        iv = base64.b64decode(iv)

        ciphertext = base64.b64decode(encrypted_string)
        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypted = cipher.decrypt(ciphertext)
        return unpad(decrypted, AES.block_size).decode('utf-8')

    except:
        print("#### Error decrypting msg")

    return None


# Example usage
secret = "irQYAOIrZsKSs9pqXi1Uwg=="
i_vector = "XG9/IJ1+JrFqbQacAvwxBQ=="
original_string = "{\"otp\":\"629073\",\"convID\":\"de60a7ee0867435bb7fee91c31e5f536\",\"txnCode\":\"Login\"}"

encrypted_str = aes_encrypt(original_string, secret, i_vector)
decrypted_string = aes_decrypt(encrypted_str, secret, i_vector)

print("Original string:", original_string)
print("Encrypted string:", encrypted_str)
print("Decrypted string:", decrypted_string)

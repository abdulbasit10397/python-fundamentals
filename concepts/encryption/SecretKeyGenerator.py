import hashlib
import base64


class AppException(Exception):
    pass


def get_card_secret_key():
    try:
        key = "12345566".encode('utf-8')

        sha = hashlib.sha1()
        sha.update(key)
        key = sha.digest()[:16]

        encoded_key = base64.b64encode(key).decode('utf-8')
        return encoded_key

    except Exception as e:
        print(f"Exception in generateKeys: {e}")
        raise AppException("KEY_GEN_FLD") from e


# Example usage:
try:
    secret_key = get_card_secret_key()
    print(f"Generated Secret Key: {secret_key}")
except AppException as e:
    print(f"Failed to generate secret key: {e}")

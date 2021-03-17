import hashlib
import secrets
from database import add_hash

def generate_key():
    return secrets.token_urlsafe(30)

def hash_key(key_str):
    m = hashlib.sha256()
    m.update( bytes(key_str, 'utf-8') )
    return m.hexdigest()

if __name__ == '__main__':
    key = generate_key()
    print("New Key: " + key)
    hidden_key = str(hash_key(key))
    add_hash(hidden_key)
    print("Remember to save your new key!  This is the only time it will be displayed!")

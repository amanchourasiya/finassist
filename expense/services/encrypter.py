import hashlib

def get_hash(word):
    return hashlib.md5(word.encode()).hexdigest()
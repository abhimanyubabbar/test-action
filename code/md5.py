import hashlib


def get_md5(key):
    return hashlib.md5(key.encode("utf-8")).hexdigest()

import hashlib
import pickle


def cache_key_generator(a, k):
    return hashlib.md5(pickle.dumps((a, k))).hexdigest()



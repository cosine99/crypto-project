import uuid
import hashlib
import random
from itertools import cycle
import base64

def hash(password):
    # return hashlib.sha256(password.encode()).hexdigest()
    return (abs(password))

def xor(data, key, encode=False, decode=False):
    
    # if decode:
    #      data = base64.decodestring(data)

    # xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
    # return xored

    return (data ^ key)

def orutil(data, key):
    # ored = ''.join(chr(ord(x) | ord(y)) for (x,y) in zip(data, cycle(key)))
    # return ored

    return (data | key)
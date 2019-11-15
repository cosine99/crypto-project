import uuid
import hashlib
import random
from itertools import cycle
import base64


def xor(data, key):

    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(str(data), cycle(str(key))))
    return xored
  
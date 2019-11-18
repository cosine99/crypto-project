import uuid
import hashlib
import random
from itertools import cycle
import base64


def xor(data, key):
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(str(data), cycle(str(key))))
    return xored


class HomeAgent:
    
    def __init__(self):
        self.SKha = 'SKha'


    def user_registration_2(self, EID):
        S = hash(EID + str(hash(self.SKha)))

        return 0, S


    def a_step3(self, EID1, Vm, Vf, Qf, Nm, IDfa, foreign_agent):
        self.S1 = hash(EID1 + str(hash(self.SKha)))
        self.EID1new = xor(Vm, hash(str(self.S1) + str(Nm)))
        self.SKfa = hash(xor(IDfa, self.SKha))
        self.Nf = xor(Vf, hash(self.SKfa))
        self.Qf = str(hash(str(hash(self.EID1new + str(self.S1) + Nm)) + self.Nf + str(self.SKfa)))

        # FIX THIS
        if self.Qf != Qf:
            print('\nQFs are Not Equal\n\n')
            self.Qf = Qf

        self.Snew = hash(str(self.EID1new) + str(hash(self.SKha)))
        self.Vh = xor((self.EID1new + str(self.S1) + str(self.Snew)), hash(str(self.SKfa) + self.Nf))

        return foreign_agent.aesk_step_4(self.Vh, self.Snew, self.Snew, self)
        
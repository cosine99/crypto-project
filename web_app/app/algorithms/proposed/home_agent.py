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


    def agent_registration_2(self, IDfa, Kfa, foreign_agent):
        self.SKfa = hash(xor(IDfa, self.SKha))
        self.Kfa = Kfa

        return foreign_agent.agent_registration_3(self.SKfa)


    def user_registration_2(self, EID):
        S = hash(EID + str(hash(self.SKha)))
        
        return 0, S


    def aesk_step_3(self, EID1, Vm, Vf, Qf, Nm, IDfa, Nf2, foreign_agent):
        self.S1 = hash(EID1 + str(hash(self.SKha)))
        self.EID1new = xor(Vm, hash(str(self.S1) + str(Nm)))
        SKfa = hash(xor(IDfa, self.SKha))
        self.Nf = xor(xor(Vf, hash(SKfa)), hash(str(self.Kfa) + str(Nm)))
        self.Qf = hash(str(hash(self.EID1new + str(self.S1) + Nm)) + self.Nf + str(SKfa))
        self.Snew = hash(str(self.EID1new) + str(hash(self.SKha))) 
        self.Vh = xor((self.EID1new + str(self.S1) + str(self.Snew)), hash(str(self.SKfa) + self.Nf))
        self.Qf = Qf

        return foreign_agent.aesk_step_4(self.Vh, self.Snew, Nf2, self)


    def password_altered_3(self, EID1new, mobile_user):
        self.Snew = hash(EID1new + str(hash(self.SKha)))

        return mobile_user.password_altered_4(self.Snew)

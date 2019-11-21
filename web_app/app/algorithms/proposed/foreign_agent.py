from time import time
import uuid
import hashlib
import random
from itertools import cycle
import base64


def xor(data, key):
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(str(data), cycle(str(key))))
    return xored


class ForeignAgent:

    def __init__(self):
        self.SKfa = 'SKfa'
        self.IDfa = 'IDfa'
        self.b = 'b'
        self.Kfa = 'Kfa'


    def agent_registration(self, home_agent):
        print('Agent Registration Phase:')

        start = time()
        self.Kfa = hash(self.IDfa + self.b)
        status = home_agent.agent_registration_2(self.IDfa, self.Kfa, self)

        end = time()
        time_taken = end - start
        print('Successful')

        return status, time_taken


    def agent_registration_3(self, SKfa):
        self.SKfa = SKfa

        return 0


    def aesk_step_2(self, EID1, Vm, Qm, Nm, Nf, Nf2, home_agent, mobile_user):        
        self.mobile_user = mobile_user;
        self.Qm = Qm
        self.EIDnew = EID1
        self.Nm = Nm
        self.Nf = Nf
        self.Qf = hash((str(Qm) + (self.Nf) + str(self.SKfa)))
        self.Vf = xor(xor(self.Nf, hash(self.SKfa)), hash(str(self.Kfa) + str(Nm)))
        
        return home_agent.aesk_step_3(EID1, Vm, self.Vf, self.Qf, Nm, self.IDfa, Nf2, self)


    def aesk_step_4(self, Vh, Snew, Nf2, home_agent):
        self.Snew = Snew

        if(self.Qm != str(hash(str(self.EIDnew) + str(Snew) + str(self.Nm)))):
            print('Failure at step 4')
            return 1

        self.Nf2 = Nf2
        self.Vf2 = xor(Snew, hash(str(Snew) + self.Nf2))
        self.Qf2 = hash(self.EIDnew + str(self.Snew) + self.Nf2)

        return self.mobile_user.aesk_step_5(self.Vf2, self.Qf2, self.Nf2, self)


    def aesk_step_6(self, Qmf):
        if(Qmf != hash(self.Nm + str(self.Snew) + self.Nf2 + str(self.Snew))):
            print('Qmf doesnt match')
            return 1

        self.Kmf = hash(self.Nm + self.Nf2 + str(self.Snew))

        return 0


    def sk_update_2(self, Um, Qstarm, Nstarf, mobile_user):
        self.Nstarm = xor(Um, hash(str(self.Snew) + self.Nm + self.Nf2))

        if(Qstarm != hash(xor(self.Nstarm, self.Snew))):
            print('Qstarm doesnt match')
            return 0

        self.Nstarf = Nstarf
        self.Uf = xor(self.Nstarf, hash(str(self.Snew) + self.Nf2 + self.Nstarm))
        self.Qstarf = hash(xor(self.Nstarf, self.Snew))

        return mobile_user.sk_update_3(self.Uf, self.Qstarf, self)


    def sk_update_4(self, Qstarmf, mobile_user):
        if(Qstarmf != hash(xor(xor(self.Nstarm, self.Nstarf), self.Snew))):
            print('Qstarmf doesnt match')
            return 1

        self.Kmf = mobile_user.Kmf
        
        return 0

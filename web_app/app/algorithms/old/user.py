from time import time
import uuid
import hashlib
import random
from itertools import cycle
import base64


def xor(data, key):
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x, y) in zip(str(data), cycle(str(key))))
    return xored


class MobileUser:

    def registration(self, IDmu, PWmu, s, home_agent, foreign_agent):
        print('User Registration Phase:')
        
        start = time()

        # Step 1
        self.IDmu = IDmu
        self.PWmu = PWmu
        self.s = s
        self.EID = xor(hash(xor(self.IDmu, self.PWmu)), self.s)
        status, self.S = home_agent.user_registration_2(self.EID)

        # Step 3

        if(status == 0):
            self.SPW = xor(self.S, hash(self.PWmu))

        end = time()
        time_taken = end - start
        print('Successful')

        return status, time_taken
        

    def aesk(self, PW1mu, snew, Nm, Nf, Nf2, home_agent, foreign_agent):
        start = time()

        self.PW1mu = PW1mu

        # IMPLEMENT MATCH PASSWORD

        self.snew = snew
        self.Nm = Nm
        self.EID1 = xor(hash(xor(self.IDmu, self.PW1mu)), self.s)
        self.S1 = xor(self.SPW, hash(self.PW1mu))
        self.EIDnew = xor(hash(xor((self.IDmu), self.PW1mu)), self.snew)
        self.Vm = xor(self.EIDnew, hash(str(self.S1) + self.Nm))
        self.Qm = str(hash(self.EIDnew + str(self.S1) + self.Nm))
        status = foreign_agent.a_step2(self.EID1, self.Vm, self.Qm, self.Nm, Nf, Nf2, home_agent, self)
        
        end = time()
        time_taken = end - start
        print('Successful')
        
        return status, time_taken


    def aesk_step_5(self, Vf2, Qf2, Nf2, foreign_agent):   
        self.Snew = xor(Vf2, hash(str(self.S) + Nf2))
        self.Nf2 = Nf2

        if(Qf2 != hash(self.EID + self.Snew + Nf2)):
            print('Error at aesk_step_5')
            return 1

        self.SPWnew = xor(self.Snew,(hash(self.PWmu)))
        self.Kmf = hash(self.Nm + Nf2 + str(self.S))
        self.Qmf = hash(self.Nm + str(self.S) + Nf2 + self.Snew)

        return foreign_agent.aesk_step_6(self.Qmf)


    def session_key_update(self, Nstarm, Nstarf, Kmf, home_agent, foreign_agent):
        start = time()

        self.Nstarm = Nstarm
        self.Um = xor(self.Nstarm, hash(str(self.S) + self.Nm + self.Nf2))
        self.Qstarm = hash(xor(self.Nstarm, self.S))
        self.Kmf_new = Kmf
        status = foreign_agent.sk_update_2(self.Um, self.Qstarm, Nstarf, self)

        end = time()
        time_taken = end - start

        return status, time_taken


    def sk_update_3(self, Uf, Qstarf, foreign_agent):
        self.Nstarf = xor(Uf, hash(str(self.S) + self.Nf2 + self.Nm))

        if(Qstarf != hash(xor(self.Nstarf, self.S))):
            print('Qstarf doesnt match')
            return 1

        self.Kmf = self.Kmf_new
        self.Qstarmf = hash(xor(xor(self.Nstarm, self.Nstarf), self.S))

        return foreign_agent.sk_update_4(self.Qstarmf, self)


    def password_altered(self, IDmu, PWmu, PWmu_new, home_agent, foreign_agent):
        print('password_altered phase')

        start = time()

        if(self.IDmu != IDmu or self.PWmu != PWmu):
            print('Credentials dont match')
            return 1

        self.PWmu = PWmu_new        
        self.EIDnew = xor(hash(xor(self.IDmu, PWmu)), self.s)
        self.SPW = xor(self.Snew, hash(self.PWmu))

        end = time()
        time_taken = end - start


        return 0, time_taken

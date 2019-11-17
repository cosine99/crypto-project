from utility import *

class HomeAgent:
    
    def __init__(self):
        self.SKha = 96
        #self.SKfa = 63

    def user_registration_2(self, EID):
        print('Step 2')

        S = hash(EID + str(hash(self.SKha)))
        print('S: ', S)

        return S

    def a_step3(self, EID1, Vm, Vf, Qf, Nm, IDfa, foreign_agent):
        print('Step 3')
        print('\nQf: ',Qf)
        self.S1 = hash(EID1 + str(hash(self.SKha)))
        self.EID1new = xor(Vm, hash(str(self.S1) + str(Nm)))
        self.SKfa = hash(xor(IDfa, self.SKha))
        self.Nf = xor(Vf, hash(self.SKfa))
        self.Qf = str(hash(str(hash(self.EID1new + str(self.S1) + Nm)) + self.Nf + str(self.SKfa)))
        print('self.qf : ', self.Qf)
        if self.Qf == Qf:
            print('\nQFs are Equal !!!!!!!!\n\n')
        else:
            print('\nQFs are Not Equal\n\n')
            self.Qf = Qf

        self.Snew = hash(str(self.EID1new) + str(hash(self.SKha)))
        self.Vh = xor((self.EID1new + str(self.S1) + str(self.Snew)), hash(str(self.SKfa) + self.Nf))

        foreign_agent.aesk_step_4(self.Vh, self.Snew, self)
        
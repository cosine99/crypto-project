from utility import *

class ForeignAgent:
    def __init__(self):
        self.SKfa = 'SKfa'
        self.IDfa = 'IDfa'
        self.b = 'b'
        self.Kfa = 'Kfa'

    def agent_registration_1(self, home_agent, mobile_user):
        self.mobile_user = mobile_user
        self.Kfa = hash(self.IDfa + self.b)
        home_agent.agent_registration_2(self.IDfa, self.Kfa, self)

    def agent_registration_3(self, SKfa):
        self.SKfa = SKfa

    def aesk_step_2(self, home_agent, EID1, Vm, Qm, Nm):
        print('Step 2')

        self.Qm = Qm
        self.EIDnew = EID1
        self.Nm = Nm
        self.Nf = input('Foreign Agent chooses a rand number : ')
        self.Qf = hash((str(Qm) + (self.Nf) + str(self.SKfa)))
        self.Vf = xor(xor(self.Nf, hash(self.SKfa)), hash(str(self.Kfa) + str(Nm)))
        
        print('Nf: ', self.Nf)
        print('Qf: ', self.Qf)
        print('Vf: ', self.Vf)
        
        home_agent.aesk_step_3(EID1, Vm, self.Vf, self.Qf, Nm, self.IDfa, self)

    def aesk_step_4(self, Vh, Snew, home_agent):
        self.Snew = Snew
        temp = xor(Vh, hash(str(self.SKfa) + self.Nf))
        print(str(temp))
        if(self.Qm == str(hash(str(self.EIDnew) + str(Snew) + str(self.Nm)))): #JUGAAD HERE
            print(' Qm matches')
        else:
            print('Failure at step 4')
            return 0

        self.Nf2 = input('Enter another random number')
        self.Vf2 = xor(Snew, hash(str(Snew) + self.Nf2))
        self.Qf2 = hash(self.EIDnew + str(self.Snew) + self.Nf2)

        self.mobile_user.aesk_step_5(self.Vf2, self.Qf2, self.Nf2, self)

    def aesk_step_6(self, Qmf):
        if(Qmf != hash(self.Nm + str(self.Snew) + self.Nf2 + str(self.Snew))):
            print('Qmf doesnt match')
            return 0

        self.Kmf = hash(self.Nm + self.Nf2 + str(self.Snew))

        return 1


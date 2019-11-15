from utility import *

class ForeignAgent:
    def __init__(self):
        self.SKfa = 63
        self.IDfa = 23
        self.b = 45

    def agent_registration_1(self, home_agent):
        self.Kfa = hash(orutil(self.IDfa, self.b))
        home_agent.agent_registration_2(IDfa, Kfa)

    def agent_registration_3(self, SKfa):
        self.SKfa = SKfa

    def aesk_step2(self, home_agent, EID1, Vm, Qm, Nm):
        print("\nStep 2")

        self.Nf = int(input('Foreign Agent chooses a rand number : '))
        self.Qf = hash(orutil(orutil(self.Nf,self.SKfa), Qm))
        self.Vf = xor(xor(self.Nf, hash(self.SKfa)), hash(orutil(self.Kfa, Nm)))
        
        print("Nf: \n", self.Nf)
        print("Qf: \n", self.Qf)
        print("Vf: \n", self.Vf)
        
        Vh = home_agent.aesk_step3(EID1, Vm, self.Qf, Nm, self.Vf, self.IDfa)

        self.aesk_step4(Vh)

    def aesk_step4(self, Vh):
        pass
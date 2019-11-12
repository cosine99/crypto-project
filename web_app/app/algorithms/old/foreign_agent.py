from utility import *

class ForeignAgent:
    def __init__(self):
        self.SKfa = 63
        self.IDfa = 23

    def a_step2(self, home_agent, EID1, Vm, Qm, Nm):
        print("\nStep 2")

        self.Nf = int(input('Foreign Agent chooses a rand number : '))
        self.Qf = hash(orutil(orutil(self.Nf,self.SKfa), Qm))
        self.Vf = xor(self.Nf, hash(self.SKfa))
        
        print("Nf: \n", self.Nf)
        print("Qf: \n", self.Qf)
        print("Vf: \n", self.Vf)
        
        home_agent.a_step3(EID1, Vm, self.Vf, self.Qf, Nm, self.IDfa)
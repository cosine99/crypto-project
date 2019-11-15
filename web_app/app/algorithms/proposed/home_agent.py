from utility import *

class HomeAgent:
    
    def __init__(self):
        self.SKha = 96


    def agent_registration_2(self, IDfa, Kfa, foreign_agent):
        self.SKfa = hash(xor(IDfa, self.SKha))
        self.Kfa = Kfa
        foreign_agent.agent_registration_3(self.SKfa)

    def user_registration_3(self, EID):
        print("\nStep 2")

        S = hash(orutil(EID, hash(self.SKha)))
        print("S: \n", S)
        return S

    def aesk_step3(self, EID1, Vm, Vf, Qf, Nm, IDfa):
        print("\nStep 3")

        self.S1 = hash(orutil(EID1, hash(self.SKha)))
        self.EID1new = xor(Vm, hash(orutil(self.S1, Nm)))
        self.SKfa = hash(xor(IDfa, self.SKha))
        self.Nf = xor(xor(Vf, hash(self.SKfa)), hash(orutil(self.Kfa, Nm)))
        self.Qf = hash(orutil(orutil(hash(orutil(self.EID1new,orutil(self.S1,Nm))), self.Nf), self.SKfa))
        
        print(self.Qf)
        if self.Qf==Qf:
            print("QFs are Equal")
        else:
            print("QFs are Not Equal")
            return 0

        self.Snew = hash(orutil(self.EID1new, hash(self.SKha))) #DOUBT
        self.Vh = xor(orutil(EID1new, orutil(self.S1, self.Snew)), hash(orutil(self.SKfa, self.Nf))) #DOUBT

        return self.Vh

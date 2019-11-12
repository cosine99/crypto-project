from utility import *

class HomeAgent:
    
    def __init__(self):
        self.SKha = 96

    def step2(self, EID):
        print("\nStep 2")

        S = hash(orutil(EID, hash(self.SKha)))
        print("S: \n", S)
        return S

    def a_step3(self, EID1, Vm, Vf, Qf, Nm, IDfa):
        print("\nStep 3")

        self.S1 = hash(orutil(EID1,hash(self.SKha)))
        self.EID1new = xor(Vm,hash(orutil(self.S1,Nm)))
        self.SKfa = hash(xor(IDfa,self.SKha))
        self.Nf = xor(Vf,hash(self.SKfa))
        self.Qf = hash(orutil(orutil(hash(orutil(self.EID1new,orutil(self.S1,Nm))), self.Nf), self.SKfa))
        
        print(self.Qf)
        if self.Qf==Qf:
            print("QFs are Equal")
        else:
            print("QFs are Not Equal")

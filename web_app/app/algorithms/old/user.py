from utility import *
from home_agent import HomeAgent
from foreign_agent import ForeignAgent

class MobileUser:

    def __init__(self):
        self.IDmu = 78

    def registration(self, home_agent, foreign_agent):
        print("\nStep 1")
        self.PWmu = int(input('MU chooses a password : '))
        self.s = int(input('MU chooses a random number : ')     )
        EID = xor(hash(xor(self.IDmu,self.PWmu,True)) ,self.s, True)
        print("EID: ")
        print(EID)

        S = home_agent.step2(EID)

        print("\nStep 3")
        self.SPW = xor(S,hash(self.PWmu))
        print("SPW: ")
        print(self.SPW)
        print('Registration Completed')
        

    def aesk(self, home_agent, foreign_agent):
        print("\nStep 1")
        print("pw of mu : \n", self.PWmu)

        self.PW1mu = int(input('MU inputs password : '))
        self.snew = int(input('MU selects a ran number : '))
        self.Nm = int(input('MU selects a ran number : '))
        self.EID1 = xor(hash(xor(self.IDmu,self.PW1mu)),self.s)

        print("EID1: \n", self.EID1)

        self.S1 = xor(self.SPW,hash(self.PW1mu))
        self.EIDnew = xor(hash(xor((self.IDmu),self.PW1mu)),self.snew)
        self.Vm = xor(self.EIDnew, hash(orutil(self.S1,self.Nm)))
        self.Qm = hash(orutil( (orutil(self.S1,self.Nm)), self.EIDnew))

        print("S1: \n", self.S1)
        print("EIDnew: \n", self.EIDnew)
        print("Vm: \n", self.Vm)
        print("Qm: \n", self.Qm)

        foreign_agent.a_step2(home_agent, self.EID1, self.Vm, self.Qm, self.Nm)

        print('AESK Phase Completed')

    def session_key_update(self, home_agent, foreign_agent):
        pass

    def password_altered(self, home_agent, foreign_agent):
        pass

if __name__ == '__main__':
    home_agent = HomeAgent()
    foreign_agent = ForeignAgent()
    user = MobileUser()
    print('Registration Phase \n')
    user.registration(home_agent, foreign_agent)
    print('AESK phase \n')
    user.aesk(home_agent, foreign_agent)
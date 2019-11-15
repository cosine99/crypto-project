from utility import *
from home_agent import HomeAgent
from foreign_agent import ForeignAgent

class MobileUser:

    def __init__(self):
        pass

    def registration(self, home_agent, foreign_agent):
        print('Agent Registration Phase:')
        foreign_agent.agent_registration_1(home_agent, self)

        print('User Registration Phase:')

        print('Step 1')
        self.IDmu = input('Enter IDmu: ')
        self.PWmu = input('Enter PWmu: ')
        self.s = input('Enter a random number: ')

        self.EID = xor(hash(xor(self.IDmu, self.PWmu)), self.s)
        print('EID: ', self.EID)
        self.S = home_agent.user_registration_2(self.EID)

        print('Step 3') 

        self.SPW = xor(xor(self.S, hash(self.PWmu)), hash(self.IDmu + self.s))
        print('SPW: ', self.SPW)
        self.s1 = xor(self.s, hash(self.IDmu + self.PWmu))
        print('Registration Completed')
        

    def aesk_step_1(self, home_agent, foreign_agent):
        print('AESK Phase')

        print('Step 1')

        print('pw of mu : ', self.PWmu)
        self.PW1mu = input('Enter password PW\'mu : ')
        self.snew = input('MU selects a ran number : ')
        self.Nm = input('MU selects a ran number : ')
        s = xor(self.s1, hash(self.IDmu + self.PW1mu))
        self.EID1 = xor(hash(xor(self.IDmu, self.PW1mu)), s)

        print('EID1: ', self.EID1)

        self.S1 = xor(xor(self.SPW, hash(self.PW1mu)), hash(self.IDmu + s))
        self.EIDnew = xor(hash(xor((self.IDmu), self.PW1mu)), self.snew)
        self.Vm = xor(self.EIDnew, hash(self.S1 + self.Nm))
        self.s1new = xor(self.snew, hash(self.IDmu + self.PW1mu))
        self.Qm = str(hash(str(self.EIDnew) + str(self.S1) + str(self.Nm)))

        print('S1: ', self.S1)
        print('EIDnew: ', self.EIDnew)
        print('Vm: ', self.Vm)
        print('Qm: ', self.Qm)

        foreign_agent.aesk_step_2(home_agent, self.EID1, self.Vm, self.Qm, self.Nm)

    def aesk_step_5(self, Vf2, Qf2, Nf2, foreign_agent):
        self.Snew = xor(Vf2, hash(str(self.S) + Nf2))

        if(Qf2 == hash(self.EID + self.Snew + Nf2)):
            print('Qf2 matches')
        else:
            print('Error at aesk_step_5')
            return 0

        self.SPWnew = xor(self.Snew, xor(hash(self.PWmu), hash(self.IDmu + self.s)))

        self.Kmf = hash(self.Nm + Nf2 + str(self.S))
        self.Qmf = hash(self.Nm + str(self.S) + Nf2 + self.Snew)

        foreign_agent.aesk_step_6(self.Qmf)

        print('AESK Phase Completed')

    def session_key_update(self, home_agent, foreign_agent):
        pass

    def password_altered(self, home_agent, foreign_agent):
        pass

if __name__ == '__main__':
    home_agent = HomeAgent()
    foreign_agent = ForeignAgent()
    user = MobileUser()
    user.registration(home_agent, foreign_agent)
    user.aesk_step_1(home_agent, foreign_agent)
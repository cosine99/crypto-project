from utility import *
from home_agent import HomeAgent
from foreign_agent import ForeignAgent

class MobileUser:

    def __init__(self):
        self.IDmu = 78

    def registration(self, home_agent, foreign_agent):
        print('User Registration Phase:')

        print('Step 1')
        self.PWmu = input('Enter PWmu: ')
        self.s = input('Enter a random number: ')

        self.EID = xor(hash(xor(self.IDmu, self.PWmu)), self.s)
        print('EID: ', self.EID)
        self.S = home_agent.user_registration_2(self.EID)

        print('Step 3')

        self.SPW = xor(self.S, hash(self.PWmu))
        print('SPW: ', self.SPW)
        #self.s1 = xor(self.s, hash(self.IDmu + self.PWmu))

        

    def aesk(self, home_agent, foreign_agent):
        print("\nStep 1")
        print("pw of mu : \n", self.PWmu)

        self.PW1mu = (input('MU inputs password : '))
        self.snew = (input('MU selects a ran number : '))
        self.Nm = (input('MU selects a ran number : '))
        self.EID1 = xor(hash(xor(self.IDmu,self.PW1mu)),self.s)
        print("EID1: \n", self.EID1)
        self.S1 = xor(self.SPW,hash(self.PW1mu))
        self.EIDnew = xor(hash(xor((self.IDmu),self.PW1mu)),self.snew)
        self.Vm = xor(self.EIDnew, hash(str(self.S1) + self.Nm))
        self.Qm = hash (str(self.S1)+ self.Nm + self.EIDnew)

        print("S1: \n", self.S1)
        print("EIDnew: \n", self.EIDnew)
        print("Vm: \n", self.Vm)
        print("Qm: \n", self.Qm)
        foreign_agent.a_step2(home_agent, self.EID1, self.Vm, self.Qm, self.Nm)
        print('AESK Phase Completed')

    def password_altered(self, home_agent, foreign_agent):
        pass

    def aesk_step_5(self, Vf2, Qf2, Nf2, foreign_agent):
        self.Snew = xor(Vf2, hash(str(self.S) + Nf2))
        self.Nf2 = Nf2

        if(Qf2 == hash(self.EID + self.Snew + Nf2)):
            print('Qf2 matches')
        else:
            print('Error at aesk_step_5')
            return 0

        self.SPWnew = xor(self.Snew,(hash(self.PWmu)))

        self.Kmf = hash(self.Nm + Nf2 + str(self.S))
        self.Qmf = hash(self.Nm + str(self.S) + Nf2 + self.Snew)

        foreign_agent.aesk_step_6(self.Qmf)
        print('AESK Phase Completed')

    def session_key_update(self, home_agent, foreign_agent):
        print('Session Key Update')
        self.Nstarm = input('New Random Number')
        self.Um = xor(self.Nstarm, hash(str(self.S) + self.Nm + self.Nf2))
        self.Qstarm = hash(xor(self.Nstarm, self.S))
        foreign_agent.sk_update_2(self.Um, self.Qstarm, self)

    def sk_update_3(self, Uf, Qstarf):
        self.Nstarf = xor(Uf, hash(str(self.S) + self.Nf2 + self.Nm))

        if(Qstarf != hash(xor(self.Nstarf, self.S))):
            print('Qstarf doesnt match')
            return 0

        self.Kmf = input('New Session Key:')
        self.Qstarmf = hash(xor(xor(self.Nstarm, self.Nstarf), self.S))

        foreign_agent.sk_update_4(self.Qstarmf, self)

        print('Successful')

if __name__ == '__main__':
    home_agent = HomeAgent()
    foreign_agent = ForeignAgent()
    user = MobileUser()
    print('Registration Phase \n')
    user.registration(home_agent, foreign_agent)
    print('\nRegistration Completed')
    print('\nAESK phase \n')
    user.aesk(home_agent, foreign_agent)
    print('\nAESK phase completed')
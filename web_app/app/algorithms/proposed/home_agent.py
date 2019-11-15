from utility import *



class HomeAgent:
    
    def __init__(self):
        self.SKha = 'SKha'



    def agent_registration_2(self, IDfa, Kfa, foreign_agent):
        self.SKfa = hash(xor(IDfa, self.SKha))
        self.Kfa = Kfa
        foreign_agent.agent_registration_3(self.SKfa)

    def user_registration_2(self, EID):
        print('Step 2')

        S = hash(EID + str(hash(self.SKha)))
        print('S: ', S)

        return S

    def aesk_step_3(self, EID1, Vm, Vf, Qf, Nm, IDfa, foreign_agent):
        print('Step 3')
        print(Qf)
        self.S1 = hash(EID1 + str(hash(self.SKha)))
        self.EID1new = xor(Vm, hash(str(self.S1) + str(Nm)))
        SKfa = hash(xor(IDfa, self.SKha))
        self.Nf = xor(xor(Vf, hash(SKfa)), hash(str(self.Kfa) + str(Nm)))
        self.Qf = hash(str(hash(self.EID1new + str(self.S1) + Nm)) + self.Nf + str(SKfa))

        if self.Qf==Qf:
            print('QFs are Equal')
        else:
            print('QFs are Not Equal')
            self.Qf = Qf

        self.Snew = hash(str(self.EID1new) + str(hash(self.SKha))) 
        self.Vh = xor((self.EID1new + str(self.S1) + str(self.Snew)), hash(str(self.SKfa) + self.Nf))

        foreign_agent.aesk_step_4(self.Vh, self.Snew, self)


    def password_altered_3(self, EID1new, mobile_user):
        self.Snew = hash(EID1new + str(hash(self.SKha)))

        mobile_user.password_altered_4(self.Snew)

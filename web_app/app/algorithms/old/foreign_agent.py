from utility import *

class ForeignAgent:
    def __init__(self):
        self.SKfa = 63
        self.IDfa = 23

    def a_step2(self, EID1, Vm, Qm, Nm, home_agent, mobile_user):
        self.mobile_user = mobile_user
        print("\nStep 2")

        self.Qm = Qm
        self.EIDnew = EID1
        self.Nm = Nm
        self.Nf = input('Foreign Agent chooses a rand number : ')
        self.Qf = hash(str(Qm) + str(self.Nf) + str(self.SKfa))
        self.Vf = xor(self.Nf, hash(self.SKfa))
        
        print('Nf: ', self.Nf)
        print('Qf: ', self.Qf)
        print('Vf: ', self.Vf)
        
        home_agent.a_step3(EID1, Vm, self.Vf, self.Qf, Nm, self.IDfa, self)

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

    def sk_update_2(self, Um, Qstarm, mobile_user):
        self.Nstarm = xor(Um, hash(str(self.Snew) + self.Nm + self.Nf2))
        if(Qstarm != hash(xor(self.Nstarm, self.Snew))):
            print('Qstarm doesnt match')
            return 0

        self.Nstarf = input('New Nstarf')

        self.Uf = xor(self.Nstarf, hash(str(self.Snew) + self.Nf2 + self.Nstarm))

        self.Qstarf = hash(xor(self.Nstarf, self.Snew))

        mobile_user.sk_update_3(self.Uf, self.Qstarf)

    def sk_update_4(self, Qstarmf, mobile_user):
        if(Qstarmf != hash(xor(xor(self.Nstarm, self.Nstarf), self.Snew))):
            print('Qstarmf doesnt match')
            return 0

        self.Kmf = mobile_user.Kmf
        return 1
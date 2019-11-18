from user import MobileUser
from home_agent import HomeAgent
from foreign_agent import ForeignAgent

def main():
    home_agent = HomeAgent()
    foreign_agent = ForeignAgent()
    user = MobileUser()

    foreign_agent.agent_registration(home_agent)

    print('Registration Phase \n')
    IDmu = input()
    PWmu = input()
    s = input()    
    user.registration(IDmu, PWmu, s, home_agent, foreign_agent)
    print('\nRegistration Completed')

    print('\nAESK phase \n')
    PW1mu = input()
    snew = input()
    Nm = input()
    Nf = input()
    Nf2 = input()
    user.aesk(PW1mu, snew, Nm, Nf, Nf2, home_agent, foreign_agent)
    print('\n AESK Completed')

    print('\n SK update phase \n')
    Nstarm = input()
    Nstarf = input()
    Kmf = input()    
    user.session_key_update(Nstarm, Nstarf, Kmf, home_agent, foreign_agent)
    print('Finished')

    print('\nAlter password \n')    
    IDmu = input()
    PWmu = input()
    PWmu_new = input()  
    user.password_altered(IDmu, PWmu, PWmu_new, home_agent, foreign_agent)
    print('Finished')

if __name__ == '__main__':
    main()
    
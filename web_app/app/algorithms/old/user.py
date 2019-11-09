from '../utility.py' import *
from 'home_agent.py' import 'HomeAgent'
from 'foreign_agent.py' import 'ForeignAgent'

class MobileUser:
	PWmu = 123
	s = 1234
	IDmu = 78

	def __init__(self):
		self.home_agent = HomeAgent()
		self.foreign_agent = ForeignAgent()

	def registration(self):
		print("\nStep 1")
		self.PWmu = int(input('MU chooses a password : '))
		self.s = int(input('MU chooses a random number : ')		)
		EID = xor(hash(xor(self.IDmu,self.PWmu,True)) ,self.s, True)
		print("EID: ")
		print(EID)

		S = home_agent.step2(EID)

		print("\nStep 3")
		self.SPW = xor(S,hash(self.PWmu))
		print("SPW: ")
		print(self.SPW)
		print('Registration Completed')
		

	def aesk(self):
		print("\nStep 1")
		print("pw of mu : ")
		print(self.PWmu)
		self.PW1mu = int(input('MU inputs password : '))
		self.snew = int(input('MU selects a ran number : '))
		self.Nm = int(input('MU selects a ran number : '))
		self.EID1 = xor(hash(xor(self.IDmu,self.PW1mu)),self.s)
		print("EID1:" )
		print(self.EID1)
		self.S1 = xor(self.SPW,hash(self.PW1mu))
		self.EIDnew = xor(hash(xor((self.IDmu),self.PW1mu)),self.snew)
		self.Vm = xor(self.EIDnew, hash(_or_(self.S1,self.Nm)))
		self.Qm = hash(_or_( (_or_(self.S1,self.Nm)), self.EIDnew))
		print("S1:" )
		print(self.S1)
		print("EIDnew:" )
		print(self.EIDnew)
		print("Vm" )
		print(self.Vm)
		print("Qm" )
		print(self.Qm)

		foreign_agent.a_step2(self.EID1, self.Vm, self.Qm, self.Nm)
		print('AESK Phase Completed')

	def session_key_update(self):
		pass

	def password_altered(self):
		pass
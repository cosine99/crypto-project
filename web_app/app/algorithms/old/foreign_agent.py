from 'utility.py' import *

class ForeignAgent: 
	SKfa = 63
	IDfa = 23

	def a_step2(self, home_agent, EID1, Vm, Qm, Nm):
		print("\nStep 2")
		self.Nf = int(input('ForeignAgent chooses a rand number : '))
		self.Qf = hash(_or_(_or_(self.Nf,self.SKfa), Qm))
		self.Vf = xor(self.Nf, hash(self.SKfa))
		print("Nf:")
		print(self.Nf)
		print("Qf:")
		print(self.Qf)
		print("Vf:")
		print(self.Vf)
		
		home_agent.a_step3(EID1, Vm, self.Vf, self.Qf, Nm, self.IDfa)
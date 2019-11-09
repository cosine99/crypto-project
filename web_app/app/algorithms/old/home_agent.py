from 'utility.py' import *

class HomeAgent:
	SKha = 96

	def step2(self, EID):
		print("\nStep 2")
		S = hash(_or_(EID,hash(self.SKha)))
		print("S: ")
		print(S)
		return S

	def a_step3(self, EID1, Vm, Vf, Qf, Nm, IDfa):
		print("\nStep 3")
		self.S1 = hash(_or_(EID1,hash(self.SKha)))
		self.EID1new = xor(Vm,hash(_or_(self.S1,Nm)))
		self.SKfa = hash(xor(IDfa,self.SKha))
		self.Nf = xor(Vf,hash(self.SKfa))
		self.Qf = hash(_or_(_or_(hash(_or_(self.EID1new,_or_(self.S1,Nm))), self.Nf), self.SKfa))
		print(self.Qf)
		if self.Qf==Qf:
			print("Equal")
		else:
			print("Not")

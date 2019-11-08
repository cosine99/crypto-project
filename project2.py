import uuid
import hashlib
import random
from itertools import cycle
import base64

def hash(password):
	return hashlib.sha256(password.encode()).hexdigest()

def xor(data, key, encode=False, decode=False):
	
	# if decode:
	#      data = base64.decodestring(data)

	xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
	return xored

def _or_(data, key):
	ored = ''.join(chr(ord(x) | ord(y)) for (x,y) in zip(data, cycle(key)))
	return ored

class ForeignAgent: 
	SKfa = 'skfa'
	IDfa = 'idfa'

	def a_step2(self,EID1, Vm, Qm, Nm):
		print("\nStep 2")
		self.Nf = input('ForeignAgent chooses a rand number : ')
		self.Qf = hash(_or_(_or_(self.Nf,self.SKfa), Qm))
		self.Vf = xor(self.Nf, hash(self.SKfa))
		print("Nf:")
		print(self.Nf)
		print("Qf:")
		print(self.Qf)
		print("Vf:")
		print(self.Vf)
		
		ha = HomeAgent()
		ha.a_step3(EID1, Vm, self.Vf, self.Qf, Nm, self.IDfa)

class HomeAgent:
	SKha = 'skha'

	def step2(self,EID):
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
class MobileUser:
	PWmu = ''
	s = 1234
	IDmu = 'abcd'

	def step1(self):
		print("\nStep 1")
		self.PWmu = input('MU chooses a password : ')
		self.s = input('MU chooses a random number : ')		
		EID = xor(hash(xor(self.IDmu,self.PWmu,True)) ,self.s, True)
		print("EID: ")
		print(EID)

		ha = HomeAgent()
		S = ha.step2(EID)

		print("\nStep 3")
		self.SPW = xor(S,hash(self.PWmu))
		print("SPW: ")
		print(self.SPW)
		

	def a_step1(self):
		print("\nStep 1")
		print("pw of mu : ")
		print(self.PWmu)
		self.PW1mu = input('MU inputs password : ')
		self.snew = input('MU selects a ran number : ')
		self.Nm = input('MU selects a ran number : ')
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

		fa = ForeignAgent()
		fa.a_step2(self.EID1, self.Vm, self.Qm, self.Nm)

mu = MobileUser()
print("\nREGISTRATION PHASE\n")
mu.step1()
print("\nREGISTRATION PHASE DONE\n")
print("\nAESK PHASE\n")
mu.a_step1()
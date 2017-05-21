import csv

index = []
rotor_wiring = []
reflector_wiring = []

# reads in rotor and reflector wiring
with open('rotor_wiring.csv') as wiring:
	data = csv.reader(wiring)
	
	next(data) # skips header
	index = next(data)

	next(data)
	for i in range(5):
		rotor_wiring.append(next(data))

	next(data)
	reflector_wiring = next(data)

class rotor:
	rotor_start = []
	rotor_curr = []

	def __init__(self, rotor_no, start_pos):
		self.rotor_start = rotor_wiring[rotor_no]
		print(self.rotor_start)
		self.rotor_curr = rotor_start[start_pos:] + rotor_start[:start_pos]

	def encrypt(self, char):
		return self

	def encrypt_reverse(self, char):
		pass
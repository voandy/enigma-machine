from string import ascii_lowercase as lower
import csv

index = []
rotor_wiring = []
reflector_wiring = []
letter_dict = {letter:i for i, letter in enumerate(lower, 1)}

# reads in rotor and reflector wiring
with open('rotor_wiring.csv') as wiring:
	data = csv.reader(wiring)
	
	next(data) # skips header
	index = next(data)

	next(data)
	rotor_wiring = [next(data) for i in range(5)]

	next(data)
	reflector_wiring = next(data)

class rotor:
	rotor_start = []
	rotor_curr = []

	def __init__(self, rotor_no, start_pos):
		self.rotor_start = rotor_wiring[rotor_no]
		self.rotor_curr = self.rotor_start[start_pos:] + \
			self.rotor_start[:start_pos]

	def encrypt(self, char):
		return self

	def encrypt_reverse(self, char):
		pass

def convert_char(char):
	pass
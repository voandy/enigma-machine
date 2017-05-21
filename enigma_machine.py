from string import ascii_uppercase as uper
import csv

# declare and import setting for the rotors and reflector
rotor_index = []
rotor_wiring = []
reflector_wiring = []
letter_dict = {letter:i for i, letter in enumerate(uper)}

with open('wiring.csv') as wiring:
	data = csv.reader(wiring)
	
	next(data) # skips header
	rotor_index = next(data)

	next(data)
	rotor_wiring = [next(data) for i in range(5)]

	next(data)
	reflector_wiring = next(data)

class plug_board:
	pass

class rotor:
	rotor_start = []
	rotor_curr = []
	index_curr = []

	def __init__(self, rotor_no, start_pos):
		self.rotor_start = rotor_wiring[rotor_no]
		self.rotor_curr = self.rotor_start[start_pos:] + \
			self.rotor_start[:start_pos]
		self.index_curr = rotor_index[start_pos:] + rotor_index[:start_pos]

	def encrypt(self, num):
		return self.rotor_curr.index(self.index_curr[num])

	def encrypt_reverse(self, char):
		pass

	def rotate(self):
		self.rotor_curr = self.rotor_curr[1:] + self.rotor_curr[:1]
		self.index_curr = self.index_curr[1:] + self.index_curr[:1]

class reflector:
	pass

def convert_char(char):
	return letter_dict[char.upper()]



class machine:
	pass

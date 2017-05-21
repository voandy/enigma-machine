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
	turnover_pos = 0

	def __init__(self, rotor_no, start_pos):
		# The first 26 numbers in rotor_wiring represent the wiring while 
		# the 27th number indicates its turnover position
		self.rotor_start = rotor_wiring[rotor_no][:26]
		self.turnover_pos = rotor_wiring[rotor_no][26]

		# rotor and index rotated to reflect starting position
		self.rotor_curr = self.rotor_start[start_pos:] + \
			self.rotor_start[:start_pos]
		self.index_curr = rotor_index[start_pos:] + rotor_index[:start_pos]

	# encrypts a single character in the forward direction
	def encrypt(self, num):
		return self.rotor_curr.index(self.index_curr[num])

	# encrypts a single character in the backward direction
	def encrypt_reverse(self, num):
		return self.index_curr.index(self.rotor_curr[num])

	# rotates entire rotor by 1 and returns true of the index has reached
	# the turnover pos
	def rotate(self):
		self.rotor_curr = self.rotor_curr[1:] + self.rotor_curr[:1]
		self.index_curr = self.index_curr[1:] + self.index_curr[:1]
		if self.index_curr[0] == self.turnover_pos:
			return True
		else:
			return False

class reflector:
	pass

def convert_char(char):
	return letter_dict[char.upper()]



class machine:
	pass

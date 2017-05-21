from string import ascii_uppercase as uper
import csv

# declare and import setting for the rotors and reflector
rotor_index = []
rotor_wiring = []
reflector_wiring = []
letter_dict = {letter:i for i, letter in enumerate(uper)}
number_dict = {i:letter for i, letter in enumerate(uper)}

with open('wiring.csv') as wiring:
	data = csv.reader(wiring)
	
	next(data) # skips header
	rotor_index = list(map(int,next(data)))

	next(data)
	rotor_wiring = [list(map(int,next(data))) for i in range(5)]

	next(data)
	reflector_wiring = list(map(int,next(data)))

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

	# encrypts a single character in the left direction
	def encrypt_left(self, num):
		return self.rotor_curr.index(self.index_curr[num])

	# encrypts a single character in the right direction
	def encrypt_right(self, num):
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

def reflect(num):
	return reflector_wiring[num]

def convert_char(char):
	return letter_dict[char.upper()]

def convert_num(num):
	return number_dict[num]

class machine:
	rotor_right = None
	rotor_middle = None
	rotor_left = None

	def __init__(self, rotor1, rotor2, rotor3):

		self.rotor_right = rotor(rotor1[0], rotor1[1])
		self.rotor_middle = rotor(rotor2[0], rotor2[1])
		self.rotor_left = rotor(rotor2[0], rotor2[1])

	def encode_message(self, text):
		# converts message to list of ints
		message = [convert_char(char) for char in list(text)]

		encoded_list = []
		encoded_message = ''

		# encrypts each num
		for num in message:
			num = self.encrypt_num(num)
			encoded_list.append(num)

			# rotates the rotors after each character
			if self.rotor_right.rotate():
				if self.rotor_middle.rotate():
					self.rotor_left.rotate()

		# converts encoded list back to string
		for num in encoded_list:
			encoded_message = encoded_message + convert_num(num)

		return encoded_message

	def encrypt_num(self, num):
		# first pass through the rotors
		num = self.rotor_right.encrypt_left(num)
		num = self.rotor_middle.encrypt_left(num)
		num = self.rotor_left.encrypt_left(num)

		# bounce off reflector
		num = reflect(num)
	
		#second pass through the rotors
		num = self.rotor_left.encrypt_right(num)
		num = self.rotor_middle.encrypt_right(num)
		num = self.rotor_right.encrypt_right(num)

		return num
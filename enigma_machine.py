from string import ascii_uppercase as uper
import csv

rotor_wiring = []
reflector_wiring = []
letter_dict = {letter:i for i, letter in enumerate(uper)}
number_dict = {i:letter for i, letter in enumerate(uper)}

# import setting for the rotors and reflector
with open('wiring.csv') as wiring:
	data = csv.reader(wiring)

	next(data)
	rotor_wiring = [list(map(int,next(data))) for i in range(5)]

	next(data)
	reflector_wiring = list(map(int,next(data)))

class plug_board:
	pass

class rotor:
	rotor_start = []
	turnover_pos = 0
	offset = []
	offset_rev = []

	def __init__(self, rotor_no, start_pos, ring_setting = 0):
		# The first 26 numbers in rotor_wiring represent the wiring while 
		# the 27th number indicates its turnover position
		self.rotor_start = rotor_wiring[rotor_no][:26]
		self.turnover_pos = rotor_wiring[rotor_no][26]

		# offset rotor's start position by the ring setting, similar effect
		# to rotating rotor but also offsets turnover position
		if ring_setting:
			self.rotor_start = self.rotor_start[ring_setting:] + \
				self.rotor_start[:ring_setting]

		# set rotor offset for right to left encryption
		self.offset = [(self.rotor_start.index(i) - i) % 26 for i in range(26)]

		# set rotor offset for left to right encryption
		self.offset_rev = [(self.rotor_start[i] - i) % 26 for i in range(26)]

		# offsets turnover position
		self.turnover_pos = self.offset[self.turnover_pos]

		# rotor rotated to reflect starting position
		self.offset = self.offset[start_pos:] + self.offset[:start_pos]
		self.offset_rev = self.offset_rev[start_pos:] + \
			self.offset_rev[:start_pos]

	# encrypts a single character right to left
	def encrypt(self, num):
		return (num + self.offset[num]) % 26

	# encrypts a single character left to right
	def encrypt_rev(self, num):
		return (num + self.offset_rev[num]) % 26

	def rotate(self):
		# rotates entire rotor by 1
		self.offset = self.offset[1:] + self.offset[:1]
		self.offset_rev = self.offset_rev[1:] + self.offset_rev[:1]

		# returns true of the index has reached the turnover position
		return self.offset[0] == self.turnover_pos

def reflect(num):
	return reflector_wiring[num]

def convert_char(char):
	return letter_dict[char.upper()]

def convert_num(num):
	return number_dict[num]

class enigma_machine:
	rotor_right = None
	rotor_middle = None
	rotor_left = None

	def __init__(self, rotor_r, rotor_m, rotor_l):
		self.rotor_right = rotor(rotor_r[0], rotor_r[1])
		self.rotor_middle = rotor(rotor_m[0], rotor_m[1])
		self.rotor_left = rotor(rotor_l[0], rotor_l[1])

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
		num = self.rotor_right.encrypt(num)
		num = self.rotor_middle.encrypt(num)
		num = self.rotor_left.encrypt(num)

		# bounce off reflector
		num = reflect(num)
	
		#second pass through the rotors
		num = self.rotor_left.encrypt_rev(num)
		num = self.rotor_middle.encrypt_rev(num)
		num = self.rotor_right.encrypt_rev(num)

		return num

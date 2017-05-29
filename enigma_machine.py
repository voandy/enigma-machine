from convert import *
import csv

# import setting for the rotors and reflector
rotor_wiring = []
reflector_wiring = []

with open('wiring.csv') as wiring:
	data = csv.reader(wiring)

	next(data)
	rotor_wiring = [list(map(convert_char,next(data))) for i in range(5)]

	next(data)
	reflector_wiring = list(map(convert_char,next(data)))

class plug_board:
	plug_board = [0 for i in range(26)]

	def __init__(self, num_pairs):
		for pair in num_pairs:
			if pair[0] > pair[1]:
				pair[0], pair[1] = pair[1], pair[0]
			offset = pair[1] - pair[0]

			self.plug_board[pair[0]] = offset
			self.plug_board[pair[1]] = -offset

	def encrypt(self, num):
		return num + self.plug_board[num]

class rotor:
	rotor_start = []
	turnover_pos = 0
	offset = []
	offset_rev = []

	def __init__(self, rotor_no, start_pos, ring_setting = 0):
		self.rotor_start = rotor_wiring[rotor_no]
		self.turnover_pos = ring_setting

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

class enigma_machine:
	rotor_right = None
	rotor_middle = None
	rotor_left = None
	plug_board = None

	def __init__(self, rotor_r, rotor_m, rotor_l, num_pairs):
		self.rotor_right = rotor(rotor_r[0], rotor_r[1], rotor_r[2])
		self.rotor_middle = rotor(rotor_m[0], rotor_m[1], rotor_m[2])
		self.rotor_left = rotor(rotor_l[0], rotor_l[1], rotor_l[2])
		self.plug_board = plug_board(num_pairs)

	def encode_message(self, num_list):
		encoded_list = []

		# encrypts each num
		for num in num_list:
			num = self.encrypt_num(num)
			encoded_list.append(num)

			# rotates the rotors after each character
			if self.rotor_right.rotate():
				if self.rotor_middle.rotate():
					self.rotor_left.rotate()

		return encoded_list


	def encrypt_num(self, num):
		# first pass through plug board
		num = self.plug_board.encrypt(num)

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

		# second pass through plug board
		num = self.plug_board.encrypt(num)

		return num

def encrypt_decrypt(enigma_machine, text):
	num_list = text_to_list(text)
	encoded_list = enigma_machine.encode_message(num_list)

	return list_to_text(encoded_list)
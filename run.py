from enigma_machine import *

rotors = []
start_positions = []

rotor_select = 0
start_pos = 0

run = True
answer = ''

def run_machine():
	rotor_select = int(input('Select first rotor (1-5): '))
	rotors.append(rotor_select - 1)
	start_pos = int(input('Choose the starting position (1-26): '))
	start_positions.append(start_pos - 1)

	rotor_select = int(input('\nSelect second rotor (1-5): '))
	rotors.append(rotor_select - 1)
	start_pos = int(input('Choose the starting position (1-26): '))
	start_positions.append(start_pos - 1)

	rotor_select = int(input('\nSelect second rotor (1-5): '))
	rotors.append(rotor_select - 1)
	start_pos = int(input('Choose the starting position (1-26): '))
	start_positions.append(start_pos - 1)

	enigma = machine(rotors, start_positions)

	text = input('\nEnter a message to encrypt/decrypt '\
	'(no spaces or punctuation): ')

	encoded_message = enigma.encode_message(text)
	print('\nYour encrypted/decrypted message is: \n', encoded_message, '\n')

while run:
	run_machine()
	answer = input('Play again (y/n)? ')
	print('\n')
	if answer == 'n':
		run = False

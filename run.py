from enigma_machine import *

rotor_r = []
rotor_m = []
rotor_l = []

rotor_select = 0
start_pos = 0

run = True
answer = ''

def run_machine():
	rotor_select = int(input('Select right rotor (1-5): '))
	rotor_r.append(rotor_select - 1)
	start_pos = int(input('Choose the starting position (1-26): '))
	rotor_r.append(start_pos - 1)

	rotor_select = int(input('\nSelect middle rotor (1-5): '))
	rotor_m.append(rotor_select - 1)
	start_pos = int(input('Choose the starting position (1-26): '))
	rotor_m.append(start_pos - 1)

	rotor_select = int(input('\nSelect left rotor (1-5): '))
	rotor_l.append(rotor_select - 1)
	start_pos = int(input('Choose the starting position (1-26): '))
	rotor_l.append(start_pos - 1)

	enigma = machine(rotor_r, rotor_m, rotor_l)

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

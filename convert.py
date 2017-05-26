from string import ascii_uppercase as uper

letter_dict = {letter:i for i, letter in enumerate(uper)}
def convert_char(char):
	return letter_dict[char.upper()]

number_dict = {i:letter for i, letter in enumerate(uper)}
def convert_num(num):
	return number_dict[num]

def text_to_list(text):
	return [convert_char(char) for char in list(text)]

def list_to_text(num_list):
	text = ''
	for num in num_list:
		text = text + convert_num(num)
	return text

def string_to_pairs(string):
	char_pairs = string.split()
	num_pairs = [[convert_char(pair[0]), convert_char(pair[1])] \
		for pair in char_pairs]
	return num_pairs

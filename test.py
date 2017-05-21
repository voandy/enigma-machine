from enigma_machine import *

# rotor_right = rotor(0, 3)

# # print(rotor_right.rotor_curr)
# # print(rotor_right.index_curr)

# # rotor_right.rotate()

# # print("\n")

# # print(rotor_right.rotor_curr)
# # print(rotor_right.index_curr)

# # print("\n")

# print(rotor_right.encrypt_left(0))
# print(rotor_right.encrypt_right(0))

# print("\n")

# print(reflect(5))

# text = "hitlerhasonlygotoneball"
# message = [convert_char(char) for char in list(text)]
# print(message)

# print("\n")

enigma = machine([0,1,2],[10,5,6])
test = enigma.encode_message("hitlerhasonlygotoneball")
print(test)

enigma = machine([0,1,2],[10,5,6])
test = enigma.encode_message("NLSJHBBUEGBNSEIEEPPSXWO")
print(test)
from enigma_machine import *

rotor_right = rotor(0, 3)

print(rotor_right.rotor_curr)
print(rotor_right.index_curr)

rotor_right.rotate()

print("\n")

print(rotor_right.rotor_curr)
print(rotor_right.index_curr)

print("\n")

print(rotor_right.encrypt(0))
print(rotor_right.encrypt_reverse(0))
# ENIGMA MACHINE
This python script simulates the 1938 German Wehrmacht and Luftwaffe Enigma machine, the most widely used variant of Enigma during the Second World War.

Like most computer science students I am a big fan of Alan Turing both for his research and for his work at Bletchley Park cracking the Nazi Enigma code.

Out of curiosity I started studying the inner workings of the Enigma machine and got to asking how fast would it take a modern day computer to crack the Enigma code?

To answer this question I first had to program this working Enigma machine simulator.

Thanks to Crypto Museum for their invaluable wiring charts.

http://www.cryptomuseum.com/crypto/enigma/wiring.htm

# UPDATE 23/5/17
I changed the rotor's encryption of single characters to use offset values rather than the search and index method seen in the original version. This has improved the time complexity of character encryption from O(n) to O(1). It makes no difference when encrypting/decrypting but when we attack the cipher it will matter a lot as the whole machine will have to iterate through many different permutations

# UPDATE 26/5/17
I have implemented the plugboard and ring settings. The Enigma machine is finished and we are ready to attack it.

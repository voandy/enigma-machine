# ENIGMA MACHINE
This python script simulates the 1938 German Wehrmacht and Luftwaffe Enigma machine, the most widely used variant of Enigma during the Second World War.

Like most computer science students I am a big fan of Alan Turing both for his research and for his work at Bletchley Park cracking the Nazi Enigma code. My original idea was to see how long it would take a modern computer to break the Enigma code. My reasoning was that the Bombe took 20 minutes to find the enigma setting so it stands to reason that since modern computers are many orders of magnitude faster it should take them no time at all.

As it turns out, even with modern technology cracking the enigma is still no mean feat. The key space is enormous even by today's standards. There are 158,962,555,217,826,360,000 permutations in the settings putting its complexity somewhere between DES and AES. This means a brute force attack was out of the question.

What if we just re-implemented the algorithms used by Bombe itself? Well the Bombe was not really a computer by the modern definition. It was a hugely complicated electrical, mechanical device purpose built for cracking enigma so emulating it would be a hugely complicated task. Additionally it was only designed to heuristically narrow down the possibilities for further analysis by cryptologist.

In all of my research I could only find one example of someone cracking the Enigma with modern technology. A very interesting program by Robert Weiss & Ben Gatti. Their implementation relied on frequency analysis and a hill-climb algorithm as unlike modern cryptographic techniques the Enigma would look increasingly like language as you approached the correct settings. I recommend watching this presentation if you are interested in the subject.

https://www.youtube.com/watch?v=gNXzMDulp7M

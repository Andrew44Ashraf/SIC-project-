import random
lines = open('sic-opcode.txt').readlines()
random.shuffle(lines)
open('sic-opcode-shuffled.txt', 'w').writelines(lines)

        
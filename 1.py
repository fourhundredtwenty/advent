import itertools
import math

with open("1.data") as datafile:
    elf_entries = [int(i) for i in datafile.readlines()]

print([math.prod(i) for i in itertools.permutations(elf_entries, 3) if sum(i) == 2020])

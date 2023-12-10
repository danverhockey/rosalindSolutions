import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--dna_string")

args = parser.parse_args()

a, c, g, t = 0, 0, 0, 0

for i in args.dna_string:
    if i == "A":
        a += 1
    if i == "C":
        c += 1
    if i == "G":
        g += 1
    if i == "T":
        t += 1

print(a, c, g, t)


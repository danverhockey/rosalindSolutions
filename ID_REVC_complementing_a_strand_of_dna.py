import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--dna_string")

args = parser.parse_args()

new_string = ""

for i in args.dna_string[::-1]:
    if i == "A":
        new_string += "T"
    if i == "T":
        new_string += "A"
    if i == "C":
        new_string += "G"
    if i == "G":
        new_string += "C"

print(new_string)
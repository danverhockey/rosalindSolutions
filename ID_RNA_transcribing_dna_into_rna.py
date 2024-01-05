import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--dna_string")

args = parser.parse_args()

rna_string = ""

for i in args.dna_string:
    if i == "T":
        rna_string += "U"
    else:
        rna_string += i

print(rna_string)

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s1", "--dna_string", help="dna string")
parser.add_argument("-s2", "--dna_sub_string", help="dna substring")

args = parser.parse_args()

start, end = 0, len(args.dna_sub_string)
index = 1
index_list = []

for i in args.dna_string:
    if args.dna_sub_string in args.dna_string[start:end]:
        index_list.append(index)
    start += 1
    end += 1
    index += 1

print(index_list)

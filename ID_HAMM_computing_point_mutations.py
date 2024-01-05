

# for this use case a file should only be two lines of equal length representing two dna strings
def file_reader(file):
    dna_string_1 = ""
    dna_string_2 = ""
    first_line = True
    count = 0
    with open(file) as f:
        for line in f:
            if first_line is True:
                dna_string_1 += line.strip()
                first_line = False
                count += 1
            elif count >= 2:
                return False
            else:
                dna_string_2 += line.strip()
                count += 1
    if len(dna_string_1) != len(dna_string_2):
        return False
    return dna_string_1, dna_string_2


def hamming_distance(dna_string_1, dna_string_2):
    mismatch_count = 0
    for i in range(len(dna_string_1)):
        if dna_string_1[i] != dna_string_2[i]:
            mismatch_count += 1
    return mismatch_count


file_name = "ID_HAMM_input_file.txt"
dna_strings = file_reader(file_name)

if dna_strings is False:
    print("File Error: Check that file only has two lines and that they are equal length!")
else:
    hamming_dist = hamming_distance(dna_strings[0], dna_strings[1])
    print(f"Hamming Distance = {hamming_dist}")
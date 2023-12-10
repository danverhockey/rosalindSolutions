
def calculate_gc_content(dna_string):
    char_count = len(dna_string)
    gc_count = 0
    for char in dna_string:
        if char == "G" or char == "C":
            gc_count += 1
    return (gc_count/char_count) * 100


def translate_file_to_list(file_name):
    dataset = []
    with open(file_name) as f:
        temp_data = []
        dna_string = ""
        first_visit = True
        while True:
            line = f.readline()
            # end of file, have to ensure the last string and temp data are added to the dataset
            if not line:
                temp_data.append(calculate_gc_content(dna_string))
                dataset.append(temp_data)
                break
            # add temp_data to dataset
            elif line[0] == ">":
                # start of the first FASTA label is unique because the dna string hasn't been formed
                if first_visit is True:
                    temp_data.append(line.strip())
                    first_visit = False
                else:
                    temp_data.append(calculate_gc_content(dna_string))
                    dataset.append(temp_data)
                    temp_data = [line.strip()]
                    dna_string = ""
            # sequence
            else:
                dna_string += line.strip()
    print(dataset)
    # sort dataset so the first entry is the one with the highest GC content
    dataset = sorted(dataset, key=lambda data: data[1], reverse=True)
    return dataset


def print_highest_gc_content(dataset):
    print(dataset[0][0], "\n", dataset[0][1])


def main():
    file = '05_input_file.txt'
    dataset = translate_file_to_list(file)
    print_highest_gc_content(dataset)


if __name__ == "__main__":
    main()
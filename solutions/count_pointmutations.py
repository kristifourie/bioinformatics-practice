#this function returns the hamming distance between two sequences
def hamming_distance(a, b):
    distance = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            distance = distance + 1
        else:
            continue
    print(distance)

#hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")

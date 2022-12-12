#this function counts the nucleotides of a DNA strand
def nucleotide_count(nucleotide):
    a = 0
    c = 0
    g = 0
    t = 0
    for letter in nucleotide:
        if letter == 'A':
            a = a + 1
        if letter == 'C':
            c = c + 1
        if letter == 'G':
            g = g + 1
        if letter == 'T':
            t = t + 1

    print(str(a) + " " + str(c) + " " + str(g) + " " + str(t))
    return str(a) + " " + str(c) + " " + str(g) + " " + str(t)

#open text file in read mode
text_file = open("rosalind_dna.txt", "r")
 
#read whole file to a string
data = text_file.read()
 
#close file
text_file.close()
nucleotide_count(data)
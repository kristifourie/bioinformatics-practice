#this function gets the reverse complement of a DNA strand
def reverse_complement(strand):
    reverse =  strand[::-1] #get reverse strand
    old_chars = "ACGT" #this translation needs to occur
    replace_chars = "TGCA"
    tab = str.maketrans(old_chars,replace_chars) #function that translates according to above
    reverse = reverse.translate(tab) #translate
    print(reverse)
        
from locale import currency
def Sequences():
    lines = open("demo.fsa").readlines()
    all = []
    sequence = []
    sequence_ID = []
    GC_count = 0
    flag = 0
    sequence_number = 0


    for line in lines:
        all.append(line)
        #print(all)
    
    for element in all:
        if (element[0] == '>'):
            sequence_ID.append(element[1:].replace("\n", ""))
            sequence_number =+ 1
            flag = 1
        
        #this is to add multiple line sequences
        if (flag == 1):
            sequence.append(line.replace("\n", ""))
            flag = 0
        else:
            add = line.replace("\n", "")
            current = sequence[sequence_number - 1]
            new = current + add
            sequence.insert(sequence_number -1 , new) 
    return sequence
            
def CG_percentages(sequece):
    CG_percentage = []
    for element in sequece:
        count = element.count('C') + element.count('G')
        total = len(element)

        perc = count/total * 100
        CG_percentage.append(perc)
    
    return CG_percentage

def max_CG(CG_percentages):
    max = 0
    for element in CG_percentages:
        if (element > max):
            max = element

    return max
    
Sequences()

print(max_CG(CG_percentages(Sequences())))
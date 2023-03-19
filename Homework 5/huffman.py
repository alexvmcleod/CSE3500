def textToFrequency(file):
    """reads a text file and returns a dictionary of each letter's frequency"""

    #opens file and converts its text to a string called text
    file = open(file, mode = 'r')
    text = file.readlines()[0]
    
    frequencydict = {}

    #parses through text and adds letters to dictionary
    for i in text:
        if i in frequencydict:
            frequencydict[i] += 1
        else:
            frequencydict[i] = 1
    
    return frequencydict

def encode(freqdict={}):
    





print(textToFrequency('dna.txt'))
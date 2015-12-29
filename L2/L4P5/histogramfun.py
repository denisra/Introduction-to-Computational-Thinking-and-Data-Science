import pylab

# You may have to change this path
WORDLIST_FILENAME = "/home/dra/work/edx/L2/L4P5/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(vowelsratio, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    pylab.hist(vowelsratio, numBins)
    pylab.title('Vowel proportion histogram')
    pylab.xlabel('proportion')
    pylab.ylabel('counts')
    pylab.show()
    
 
def stdDev(wordList):
    
    #t = 0
    #v = 0
    vowelsinwordlist = []
    vowelsratio = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for word in wordList:
        v = sum(word.lower().count(x) for x in vowels)
        vowelsinwordlist.append(v)
        vowelsratio.append(v/float(len(word)))
        
    mean = sum(vowelsinwordlist)/float(len(vowelsinwordlist))
    total = 0
    for v in vowelsinwordlist:
        total += (v - mean)**2
    std = (total/float(len(vowelsinwordlist)))**0.5
    return std, mean, vowelsratio

    #mean = sum(X)/float(len(X))
    #tot = 0.0
    #for x in X:
    #    tot += (x - mean)**2
    #return (tot/len(X))**0.5 
       

if __name__ == '__main__':
    wordList = loadWords()
    std, mean, vowelsratio = stdDev(wordList)
    print std
    plotVowelProportionHistogram(vowelsratio)

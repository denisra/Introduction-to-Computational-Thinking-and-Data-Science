def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    import random
    total = 0
    for i in range(numTrials):
        bucket = ['red', 'red', 'red', 'green', 'green', 'green']
        random.shuffle(bucket)
        ball = bucket.pop()
        for j in range(2):
            if ball != bucket.pop(random.randint(0, len(bucket) -1)):
                break
        else:
            total += 1
    #print bucket
    return total/float(numTrials)
    
    


noReplacementSimulation(300)
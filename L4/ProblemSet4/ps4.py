# 6.00.2x Problem Set 4

import numpy
import random
import pylab
#from ps3b import *
from ps3b_precompiled_27 import *

#
# PROBLEM 1
#        

class BadPatient(TreatedPatient):
    
    def __init__(self, viruses, maxPop):
        TreatedPatient.__init__(self, viruses, maxPop)
        self.drugs = []
    
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        if newDrug not in self.drugs:
            if random.random() < 0.5:
                self.drugs.append(newDrug)    


def simWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, steps):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """

    totalSteps = steps + 300
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb) for n in range(numViruses)]
    #virusPop = [[] for n in range(numTrials)]
    virusPop = []
    #resVirusPop = [[] for n in range(numTrials)]
    for trial in range(numTrials):        
        #virusAtTime = []
        if trial <= numTrials * 0.2:
            patient = BadPatient(viruses, maxPop)
        else:
            patient = TreatedPatient(viruses, maxPop)
        for i in range(totalSteps):
            #patient.update()
            #virusAtTime.append(patient.getTotalPop())
            if i == 150:
                patient.addPrescription('guttagonol')
            if i == steps + 150:
                patient.addPrescription('grimpex') 
            patient.update()
            #virusPop[trial].append(patient.update())
        else:
            virusPop.append(patient.getTotalPop())
    print virusPop
    count = 0
    for j in virusPop:
        if j <= 50:
            count += 1
    print 'Count: %s' % count
        #print 'Trial: %s | Total Pop: %s' % (trial, sum(virusPop[trial]))
            #resVirusPop[trial].append(patient.getResistPop(['guttagonol']))
            #if i == steps/2:
            #    patient.addPrescription('guttagonol')
#        virusPop.append(virusAtTime)
    #print virusPop
    #avgPop = [sum(pop)/float(numTrials) for pop in virusPop]
    #avgResPop = [sum(pop)/float(numTrials) for pop in resVirusPop]
    #totalPop = [sum(pop) for pop in virusPop]
    #totalResPop = [sum(pop) for pop in resVirusPop]
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('Final total virus population')
    pylab.ylabel('Number of trials')
    legend = pylab.legend(loc = 'upper center')
    pylab.hist(virusPop)
    #pylab.hist(totalResPop, bins = numTrials)    
    #xmin,xmax = pylab.xlim()
    #ymin,ymax = pylab.ylim()
    #pylab.figure()
    #pylab.plot(range(0, totalSteps), avgPop, label= legend)
    #pylab.plot(range(0, totalSteps), avgResPop, label= legend)
    pylab.show()
    #print avgResPop


def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    
    #for i in [300, 150, 75, 0]:
    #    print i
    #    simWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False},
    #                   0.005, numTrials, i)
    simWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False, 'grimpex': False},
                       0.005, numTrials, 150)


#simWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False},
#                       0.005, 100, 300)
#simWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False},
#                       0.005, 100, 150)
#simWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False},
#                       0.005, 100, 75)
simulationDelayedTreatment(100)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO

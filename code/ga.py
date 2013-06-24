import matplotlib.pyplot as plt
from numpy import *
import math
import random


def readFile(filename):
	datafile = open(filename,'r')
	for line in datafile:
		line = line.lstrip()
		line  = line.split()
		print line
		tset.append(float(line[0]))
		yset.append(float(line[1].strip()))



class Sinusoid(object):
	def __init__(self):
			self.freq = random.random()
			self.a = 200.0*random.random()
			self.b = 200.0*random.random()
			self.c = 200.0*random.random()
			self.offset = 200.0*random.random()
	
	def get(self,t):
		return (self.a*math.sin(self.freq*t - self.offset) + self.b*math.cos(self.freq*t - self.offset) + self.c) #so ugly...

	def score(self,tset,yset):
		err = []
		for i in range(0,SAMPLE_SIZE):
			i = random.randint(0,len(tset)-1)
			t = tset[i]
			y = yset[i]
			err.append(math.fabs(self.get(t) - y))
		return mean(err)

	def spawn(self, mate):
		baby = Sinusoid()
		baby.freq = (random.choice([self.freq,mate.freq])+random.gauss(MU,SIGMA))
		baby.a = (random.choice([self.a,mate.a])+random.gauss(MU,SIGMA))
		baby.b = (random.choice([self.b,mate.b])+random.gauss(MU,SIGMA))
		baby.c = (random.choice([self.c,mate.c])+random.gauss(MU,SIGMA))
		baby.offset = random.choice([self.offset,mate.offset])+random.gauss(MU,SIGMA)
		return baby


MU = 0
SIGMA = 10.0
POP_SIZE = 200
PARENT_SIZE = 10
FINAL_GEN  = 100
SAMPLE_SIZE = 10

population = []
parents = []

tset = [] #arange(0.0,2,0.01)
yset = [] #map(lambda t: math.sin(2*pi*t),tset)

readFile('yearssn.dat')

SAMPLE_SIZE = len(tset)
plt.plot(tset,yset,"o")







population = map(lambda x: Sinusoid(), range(0,POP_SIZE))
for i in range(0,FINAL_GEN):
	if SAMPLE_SIZE < len(yset):
		SAMPLE_SIZE +=1
	parents = sorted(population, key = lambda a: a.score(tset,yset))[0:PARENT_SIZE]
	population=parents[:]
	k = PARENT_SIZE
	while(k <POP_SIZE):
		population.append(random.choice(parents).spawn(random.choice(parents)))
		k += 1
	print parents[0].score(tset,yset)


s = parents[0]
print "~"+ str(s.freq**-1.0)
plt.plot(tset,map(lambda t: s.get(t),tset))

plt.show()



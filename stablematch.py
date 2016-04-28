import random

def generatePrefs(numberOfPairs):
	L = [] 
	for n in range(numberOfPairs):
		foo = random.sample(range(numberOfPairs),numberOfPairs) #make random preference list
		L.append(foo)
	return L



def stableMatch(numberOfPairs):
	Mp = generatePrefs(numberOfPairs) #initial male pref list
	Wp = generatePrefs(numberOfPairs) #initial female pref list

	print " --------------------------------------------------------------- "
	print " THE STORY OF %i COUPLES, ALL TRYING TO FIND THAT PERFECT SOMEONE" % numberOfPairs
	print " --------------------------------------------------------------- "

	Mf = range(numberOfPairs) #free men
	Wf = range(numberOfPairs) #free women

	engagements = [] # engagements

	MPro = [] # male proposals

	# while there is a man, m, who is free and hasn't proposed to every woman

	while len(Mf) > 0 and len([item for item in MPro if item[0] == Mf[0]]) < numberOfPairs*2:

		man = Mf[0] # choose such man m
		
		for item in Mp[man]:
			if (man, item) not in MPro:
				woman = item
				break
		
		if woman in Wf: # if w is free
			engagements.append((man,woman)) # m,w become engaged
			print "\n %s IS NOW ENGAGED TO %s!" % (man, woman)
			Wf.remove(woman) # w is no longer free
			Mf.remove(man) # m is no longer free
			MPro.append((man, woman)) #add proposal to tracker
		
		else: 
			if (Wp[woman].index([item[0] for item in engagements][[item[1] for item in engagements].index(woman)])) < (Wp[woman].index(man)):
				MPro.append((man, woman))
				print "\n %s PROPOSED TO %s, BUT SHE PREFERS TO STAY ENGAGED TO %s" % (man, woman, (Wp[woman].index([item[0] for item in engagements][[item[1] for item in engagements].index(woman)])))
			else:
				print "\n %s PROPOSED TO %s, AND SHE DUMPED %s FOR HIM!" % (man, woman, (Wp[woman].index([item[0] for item in engagements][[item[1] for item in engagements].index(woman)])))
				MPro.append((man, woman))
				Mf.append([item[0] for item in engagements][[item[1] for item in engagements].index(woman)])	
				engagements.remove(([item[0] for item in engagements][[item[1] for item in engagements].index(woman)],woman))
				engagements.append((man,woman))
				Mf.remove(man)		

	return engagements

import itertools

def getDistances(ListOfWords, GroupSize = 4):
	Concatenated = ''.join(ListOfWords)
	UniqueChars = set(Concatenated)
	
	Distances = []
	
	Groups = itertools.combinations(UniqueChars, GroupSize)
	for Group in Groups:
		MaxDist = 0
		AllDists = []
		
		CurrentDist = 0
		for Char in Concatenated:
			if Char in Group:
				if CurrentDist > MaxDist:
					MaxDist = CurrentDist
				AllDists.append(CurrentDist)
				CurrentDist = 0
			else:
				CurrentDist += 1
		# Check last distance too
		if CurrentDist > 0:
			AllDists.append(CurrentDist)
			if CurrentDist > MaxDist:
				MaxDist = CurrentDist
	
		AverageDist = round(sum(AllDists)/float(len(AllDists)), 3)
		Distances.append([str(Group), MaxDist, AverageDist])
		
	return Distances

def sortDistances(Distances):
	return sorted(Distances, key=lambda x: (x[1], x[2]))

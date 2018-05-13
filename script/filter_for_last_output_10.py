lines = []
percentage = 50
#openfile = open("last_metal_output_mock.fa", "r")
openfile = open("arabidopsis_metal_genes_aligned.fa", "r")
inputLines = openfile.readlines()
names = set()
numberOfResults = 0
i=0
while i < len(inputLines):
	if inputLines[i][0] == 'a':
		lines = []
		secondS = False	
		keep = False
		alignmentLengthFirst = 0
		sequenceLengthFirst = 0
		alignmentLength = 0
		sequenceLength = 0
		while inputLines[i] != "\n":
			lines += inputLines[i]
			if inputLines[i][0] == 's':
				line = inputLines[i].split()
				if secondS:
					#Get the numbers here
					alignmentLength = line[3]
					sequenceLength = line[5]
					if (int(sequenceLength) * int(percentage)) / 100 <= int(alignmentLength) and (int(sequenceLengthFirst) * int(percentage)) / 100 <= int(alignmentLengthFirst):
						numberOfResults += 1
						keep = True
				else:
					alignmentLengthFirst = line[3]
					sequenceLengthFirst = line[5]
					secondS = True
			i+=1
		i+=1
		if keep:
			names.add(line[1])
			#print("".join(line[1]))
	else:
#		print("".join(inputLines[i]))
		i+=1

print("\n".join(names))

lines = []
percentage = 10
#openfile = open("last_metal_output_mock.fa", "r")
openfile = open("data_keep_genes/last_nickel_output.fa", "r")
inputLines = openfile.readlines()
names = set()
numberOfResults = 0
i=0
while i < len(inputLines):
	if inputLines[i][0] == 'a':
		lines = []
		secondS = False	
		keep = False
		while inputLines[i] != "\n":
			lines += inputLines[i]
			if inputLines[i][0] == 's':
				if secondS:
					#Get the numbers here
					line = inputLines[i].split()
					alignmentLength = line[3]
					sequenceLength = line[5]
					if (int(sequenceLength) * int(percentage)) / 100 <= int(alignmentLength):
						numberOfResults += 1
						keep = True
				else:
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

lines = []
#percentage = input("Enter the %: ")
#openfile = open("last_metal_output_mock.fa", "r")
openfile = open("arabidopsis_gmelinii_aligned.fa", "r")
inputLines = openfile.readlines()
numberOfResults = 0
i=0
percentage = 90
similarity = 80
i=0
while i < len(inputLines):
	if inputLines[i][0] == 'a':
		lines = []
		line = inputLines[i].split()
		scoreline = line[1].split('=')
		score = scoreline[1]
		secondS = False	
		keep = False
		alignmentLengthFirst = 0
		sequenceLengthFirst = 0
		alignmentLength = 0
		sequenceLength = 0
		while inputLines[i] != "\n":
			lines += inputLines[i]
			line = inputLines[i].split()
			if inputLines[i][0] == 's':
				if secondS:
					#Get the numbers here
#					line = inputLines[i].split()
					alignmentLength = line[3]
					sequenceLength = line[5]
#					print (score + " " + alignmentLength + " " + str(similarity))
#					print ((int(sequenceLength) * percentage) / 100 <= int(alignmentLength))
#					print (((int(score) * similarity) / 100 <= int(alignmentLength)))
					if (int(alignmentLength) >=120) and (int(alignmentLength) * similarity) / 100 <= int(score): #and (int(sequenceLengthFirst) * percentage) / 100 <= int(alignmentLengthFirst):
						keep = True
				else:
#					line = inputLines[i].split()
					alignmentLengthFirst = line[3]
					sequenceLengthFirst = line[5]
					secondS = True
			i+=1
		i+=1
		if keep:
#			print("".join(lines))
			print (line[1] + " \nprobe alignment length: " + str(alignmentLength) + " out of " + str(sequenceLength) + 
			" \nmetal gene alignment length: " + str(alignmentLengthFirst) + " out of " + str(sequenceLengthFirst) + 
			" \nscore: " + score + " out of " + alignmentLength + " which makes " + str(int(int(score) / int(alignmentLength) * 100)) + "%\n")
	else:
#		print("".join(inputLines[i]))
		i+=1
openfile.close()

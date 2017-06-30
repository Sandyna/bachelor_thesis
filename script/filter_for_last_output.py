lines = []
#percentage = input("Enter the %: ")
#openfile = open("last_metal_output_mock.fa", "r")
openfile = open("data_keep_genes/last_metal_output.fa", "r")
inputLines = openfile.readlines()
numberOfResults = 0
i=0
percentage = 10
while percentage >= 10:
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
						if (int(sequenceLength) * percentage) / 100 <= int(alignmentLength):
							numberOfResults += 1
							keep = True
					else:
						secondS = True
				i+=1
			i+=1
			if keep:
#				print("".join(lines))
				print line[1]
				print "\n"
#		else:
#			print("".join(inputLines[i]))
#			i+=1


#	with open("results_metal.txt", "a") as myfile:
#		myfile.write(">")
#		myfile.write(str(percentage))
#		myfile.write(": ")
#		myfile.write(str(numberOfResults))
#		myfile.write("\n")
	percentage -= 5
myfile.close()

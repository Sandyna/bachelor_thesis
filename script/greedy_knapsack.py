


input_file_name = "output_target_enrichment_probe_sequences.fasta"
new_file_name = "selected_" + input_file_name
target_number_of_bases = 1000000
switch_to_knapsack_after = 990000

input_file = open(input_file_name, "r")

name_sequence = {}
length_name = []

for line in input_file:
#	print line
	if line[0] == '>':
		name = line
		sequence = next(input_file)
		length = (len(sequence) - 1)
#		print (name, length)
		name_sequence[name] = sequence
		length_name.append( (length, name) )
#	raw_input("Press enter to continue...")

length_name.sort(reverse=True)
#print (length_name[0], length_name[2])

number_of_bases = 0
output_file = open(new_file_name, "w+")
i = 0
while number_of_bases < switch_to_knapsack_after and i < len(length_name):
#	print (i)
	name = length_name[i][1]
	length = length_name[i][0]
	if (number_of_bases + length) > switch_to_knapsack_after:
#		print length
		i += 1
		continue
#	print name
	number_of_bases += length
	output_file.write( (str(name) + str(name_sequence[name])));
	i += 1
#	raw_input("Press enter to continue...")
print (str("So far selected: " + str(number_of_bases) + " bases"))

bases_to_fill = target_number_of_bases - number_of_bases
print (str(bases_to_fill))



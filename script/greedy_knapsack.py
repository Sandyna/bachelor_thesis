


input_file_name = "output_target_enrichment_probe_sequences.fasta"
#input_file_name = "test_data.fasta"
new_file_name = "selected_" + input_file_name
target_number_of_bases = 1000000
switch_to_knapsack_after = 990000
#target_number_of_bases = 10
#switch_to_knapsack_after = 5 

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
#	print (number_of_bases, switch_to_knapsack_after, i, len(length_name))
#	print (i)
	name = length_name[i][1]
	length = length_name[i][0]
#	if (number_of_bases + length) > switch_to_knapsack_after:
#		print length
#		i += 1
#		continue
#	print name
	number_of_bases += length
	output_file.write( (str(name) + str(name_sequence[name])));
	i += 1
#	raw_input("Press enter to continue...")
print (str("So far selected: " + str(number_of_bases) + " bases"))

bases_to_fill = target_number_of_bases - number_of_bases
print (str("Bases to fill: " + str(bases_to_fill)))
sequences_left = len(length_name) - i

sums = [-1] * (bases_to_fill + 1)
#print (len(sums))
sums[0] = 0

print (len(length_name), i)

#for each sequence 
for sequence_id in range(i, len(length_name)):
#	print ("sequence_id: ", sequence_id)
	for sum_id in range(len(sums)-1, -1, -1):
#		print ("sum: ", sum_id)
		if sums[sum_id] != -1:
			if sum_id + length_name[sequence_id][0] < len(sums) and sums[sum_id + length_name[sequence_id][0]] == -1:
				sums[sum_id + length_name[sequence_id][0]] = sequence_id

print (sums)
#finds the last achieved sum
last_achieved_sum = 0
for sum_id in range(bases_to_fill, -1, -1):
	if sums[sum_id] != -1:
		last_achieved_sum = sum_id
		break
print last_achieved_sum
bases_filled = 0
#traces back to see which sequences to print
while last_achieved_sum > 0:
#	print ("Sum: " + str(last_achieved_sum))
#	print (str(length_name[sums[last_achieved_sum]][1]) + str(length_name[sums[last_achieved_sum]][0]))
	used_sequence = sums[last_achieved_sum]
	sequence_length = length_name[used_sequence][0]
#	print("We used: " + str(used_sequence) + "-th sequence, which is of length " + str(sequence_length))
#	print("We are going to look into: " + str(last_achieved_sum - sequence_length))
	name = length_name[used_sequence][1]
	bases_filled += sequence_length
	output_file.write((str(name) + str(name_sequence[name])))
	new_id = (last_achieved_sum - sequence_length)
	last_achieved_sum = new_id

print ("Overall selected " + str(bases_filled + number_of_bases) + " bases")

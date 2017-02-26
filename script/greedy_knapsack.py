


input_file_name = "output_target_enrichment_probe_sequences.fasta"
new_file_name = "selected_" + input_file_name
target_number_of_bases = 1000000
switch_to_knapsack_after = 990000
#input_file_name = "test_data.fasta"
#target_number_of_bases = 10
#switch_to_knapsack_after = 5 

input_file = open(input_file_name, "r")

name_sequence = {}
length_name = []

for line in input_file:
	if line[0] == '>':
		name = line
		sequence = next(input_file)
		length = (len(sequence) - 1)
		name_sequence[name] = sequence
		length_name.append( (length, name) )

length_name.sort(reverse=True)

number_of_bases = 0
output_file = open(new_file_name, "w+")
i = 0
while number_of_bases < switch_to_knapsack_after and i < len(length_name):
	name = length_name[i][1]
	length = length_name[i][0]
#if we go greedy till the end, we use this part
#	if (number_of_bases + length) > switch_to_knapsack_after:
#		print length
#		i += 1
#		continue
#	print name
	number_of_bases += length
	output_file.write( (str(name) + str(name_sequence[name])));
	i += 1

bases_to_fill = target_number_of_bases - number_of_bases
print (str("So far selected: " + str(number_of_bases) + " bases"))
print (str("Bases to fill: " + str(bases_to_fill)))

sequences_left = len(length_name) - i
sums = [-1] * (bases_to_fill + 1)
sums[0] = 0

#for each sequence length find out, what sums can we make with it
for sequence_id in range(i, len(length_name)):
#	for each sum, find out what sums can we make with it and the sequence
	for sum_id in range(len(sums)-1, -1, -1):
#		if we can achieve the particular sum
		if sums[sum_id] != -1:
#			if we didn't already make the new sum we are trying to make now
			if sum_id + length_name[sequence_id][0] < len(sums) and sums[sum_id + length_name[sequence_id][0]] == -1:
				sums[sum_id + length_name[sequence_id][0]] = sequence_id

#print (sums)

#finds the biggest achieved sum
last_achieved_sum = 0
for sum_id in range(bases_to_fill, -1, -1):
	if sums[sum_id] != -1:
		last_achieved_sum = sum_id
		break
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

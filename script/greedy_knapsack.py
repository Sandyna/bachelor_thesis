target_enrichement_probes_file_name = "output_target_enrichment_probe_sequences.fasta"
sequences_to_remove_file_name = "remove_genes_names.txt";
sequences_to_keep_file_name = "keep_genes_names.txt";
new_file_name = "selected_" + target_enrichement_probes_file_name
target_number_of_bases = 1000000
switch_to_knapsack_after = 990000

#Matching name to sequence
name_sequence = {}
#Matching length to sequence name
length_name = []
#Inicialisation of the new output_target_probe_sequences_file
output_target_probe_sequences_file = open(new_file_name, "w+")

#List of sequences to remove
sequences_to_remove = {}
#Reading sequences to remove
sequences_to_remove_file = open(sequences_to_remove_file_name, "r")
#Reading sequences to remove and removing them
for line in sequences_to_remove_file:
	sequences_to_remove[line] = 1
sequences_to_remove_file.close()
print (str("Found " + str(len(sequences_to_remove)) + " sequences to remove.\n"))

#List of sequences to keep
sequences_to_keep = {}
#Reading sequences to keep
sequences_to_keep_file = open(sequences_to_keep_file_name, "r")
#Reading sequences to keep
for line in sequences_to_keep_file:
	sequences_to_keep[line] = 1
sequences_to_keep_file.close()
print (str("Found " + str(len(sequences_to_keep)) + " sequences to keep.\n"))

#Number of bases we already covered
number_of_bases = 0

#Opening the files
target_enrichement_probes_file = open(target_enrichement_probes_file_name, "r")
#Reading the target_enrichement_probes_file_name
for line in target_enrichement_probes_file:
#	If it is the line with the name and if it does not contain the sequence we want to remove
	if line[0] == '>' and not(line in sequences_to_remove.keys()):
#		Putting the sequence into the output
		if line in sequences_to_keep.keys():
			name = line
			sequence = next(target_enrichement_probes_file)
			length = (len(sequence) - 1)
			#Adding the sequence into processed number of bases
			number_of_bases += length
			output_target_probe_sequences_file.write((str(name) + str(sequence)))
#		Keeping the sequence for further processing
		else:
			name = line
			sequence = next(target_enrichement_probes_file)
			length = (len(sequence) - 1)
			name_sequence[name] = sequence
			length_name.append( (length, name) )
target_enrichement_probes_file.close()

#Sorting sequences by length
length_name.sort(reverse=True)

i = 0
#Greedy part
#Put these into the output till you hit the treshold for knapsack
while number_of_bases + length_name[i + 1][0] < switch_to_knapsack_after and i + 1 < len(length_name):
	name = length_name[i][1]
	length = length_name[i][0]
	number_of_bases += length
	output_target_probe_sequences_file.write( (str(name) + str(name_sequence[name])));
	i += 1

#Bases we still need to fill
bases_to_fill = target_number_of_bases - number_of_bases
print (str("So far selected: " + str(number_of_bases) + " bases"))
print (str("Bases to fill: " + str(bases_to_fill)))

#Sums we can achieve by using which sequence
sums = [-1] * (bases_to_fill + 1)
sums[0] = 0
#knapsack part
#For each sequence length find out, what sums can we make with it
for sequence_id in range(i, len(length_name)):
#	For each sum, find out what sums can we make with it and the current sequence
	for sum_id in range(len(sums)-1, -1, -1):
#		If we can achieve the particular sum
		if sums[sum_id] != -1:
#			if we didn't already make the new sum we are trying to make now
			if sum_id + length_name[sequence_id][0] < len(sums) and sums[sum_id + length_name[sequence_id][0]] == -1:
				sums[sum_id + length_name[sequence_id][0]] = sequence_id

#Finds the biggest achieved sum
last_achieved_sum = 0
for sum_id in range(bases_to_fill, -1, -1):
	if sums[sum_id] != -1:
		last_achieved_sum = sum_id
		break
bases_filled = 0
#traces back to see which sequences to print
while last_achieved_sum > 0:
	used_sequence = sums[last_achieved_sum]
	sequence_length = length_name[used_sequence][0]
	name = length_name[used_sequence][1]
	bases_filled += sequence_length
	output_target_probe_sequences_file.write((str(name) + str(name_sequence[name])))
	new_id = (last_achieved_sum - sequence_length)
	last_achieved_sum = new_id

print ("Overall selected " + str(bases_filled + number_of_bases) + " bases")

import random

metal_keep_genes_file_name = "metal_probes_mix.fasta"
aligned_probes_file_name = "arabidopsis_gmelinii_aligned.fa"
remove_genes_file_name = "probe_names_to_keep.fasta"
keep_genes_file_name = "probe_names_to_remove.fasta"


#all names should have > at the beginning
metal_keep_genes = []
potential_probes = {}
used_duplicates = set([])
to_remove = []
to_keep = []


#načítať súbory
#metalické keep genes
metal_keep_genes_file = open(metal_keep_genes_file_name, "r")


#metalické gény nahádzať do výsledku, nahádzať do "použitých"
for line in metal_keep_genes_file:
	if line[0] == '>' and line not in used_duplicates:
		to_keep.append(line.strip())
		used_duplicates.add(line.strip())

score_alignment = []
metal_keep_genes_file.close()

#zarovnané próby
aligned_probes_file = open(aligned_probes_file_name, "r")

#zarovnané próby usporiadať podľa similarity
for line in aligned_probes_file:
	if line[0] == 'a':
		score = float(line.split()[1].split('=')[1])
		firstS = True
	if line[0] == 's':
		if firstS:
			firstS = False
			firstName = str(">" + line.split()[1])
			firstAlignmentLength = int(line.split()[3])
		else:
			secondName = str(">" + line.split()[1])
			secondAlignmentLength = int(line.split()[3])
			score_ratio = int(score / ((firstAlignmentLength + secondAlignmentLength) / 2))
			score_alignment.append((int(score_ratio), firstName, secondName))

score_alignment.sort(reverse=True, key=lambda x:x[0])

aligned_probes_file.close()

#z každej dvojice zarovnaných prób vybrať jednu, dať ju do použitých (iba ak už ona alebo jej dvojica nie je v použitých)
#druhú dať do remove súboru aj do použitých

for seq in score_alignment:
	if seq[1] not in used_duplicates and seq[2] not in used_duplicates:
		if random.choice([True, False]):
			to_keep.append(seq[1])
			to_remove.append(seq[2])
		else:
			to_keep.append(seq[2])
			to_remove.append(seq[1])
	used_duplicates.add(seq[1])
	used_duplicates.add(seq[2])
#Add both aligned sequence into duplicates, if one of them is there already

for duplicate in used_duplicates:
	print (duplicate)

with open(remove_genes_file_name, "w+") as remove_genes_file:
	for remove_line in to_remove:
		remove_genes_file.write (remove_line + "\n")
remove_genes_file.close()

with open(keep_genes_file_name, "w+") as keep_genes_file:
	for keep_line in to_keep:
		keep_genes_file.write (keep_line + "\n")
keep_genes_file.close()


digraph { 
#/*Visual settings*/
	#/*Allowing this will make the edges bend at 90 degrees
	#/*splines=ortho*/
	graph [nodesep="0.75", ranksep="0.5"];
	splines=polyline 
#/*	size ="4.4";*/
	ratio="fill"
	size="8.3,11.7!"
	node [shape=box]
	rankdir=UD
#/*Macro settings*/
	define(`digraph',`subgraph')
	PartA [label="Sondovac script, part a"]
	Geneious [label="Geneious"]
	PartA -> Geneious;
	Geneious -> RemoveSmallContigs;

#/*Sondovac part b*/
	subgraph cluster_part_b {
		label = "Sondovac script, part b";
		RemoveSmallContigs [label="removing contigs that don't comprise exons >= bait length or don't have certain total locus length \nUNIX commands"]
		ProbesWithCertainLength [label="Length-filtered probe sequences"]
		RemoveSimilarCdHit [label="removing sequences sharing >=90% similarity \nCD-HIT"]
		SimFilteredProbeSequences [label="Similarity-filtered probe sequences"]
		RemoveShortExons [label="repeated removing contigs that don't comprise exons >= bait length or don't have certain total locus length \nUNIX commands"]
		SimLenFilteredProbeSequences [label="Similarity and length-filtered probe sequences"]
		RemovePlastidsAgain [label="additional removing of probe sequences that share >=90% similarity with plastome reference \nBLAT, UNIX commands"]
		FinalProbes [label="Final Probes"]
		RemoveSmallContigs -> ProbesWithCertainLength
		ProbesWithCertainLength -> RemoveSimilarCdHit
		RemoveSimilarCdHit -> SimFilteredProbeSequences
		SimFilteredProbeSequences -> RemoveShortExons
		RemoveShortExons -> SimLenFilteredProbeSequences
		SimLenFilteredProbeSequences -> RemovePlastidsAgain
		RemovePlastidsAgain -> FinalProbes
	}
}

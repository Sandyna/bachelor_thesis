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

#/*Sondovac part a*/
	subgraph cluster_part_a {
		label = "Sondovac script, part a";
	#/*Transcripts preprocessing*/
		Transcriptome [label="Transcriptome"]
		Remove90 [label="removing transcripts that share >=90% similarity \nBLAT"]
		UniqueTranscripts [label="Unique Transcripts"]
		Transcriptome -> Remove90;
		Remove90 -> UniqueTranscripts;

	#/*Genome data preprocessing*/
		PairedEndReads [label = "Raw paired-end genome data"]
		RemovePlaMit [label = "removing reads of plastid and mitochondrial origin \nBowtie2, SAMtools"]
		CombineReads [label = "combining the paired-end reads \nFLASH"]
		CombinedReads [label = "combined reads without plastids and mitochondrial reads"]
		PairedEndReads -> RemovePlaMit;
		RemovePlaMit -> CombineReads;
		CombineReads -> CombinedReads;

	#/*Matching reads and transcripts*/
		MatchingReadsandTranscripts [label="matching the combined genome skim reads and unique transcripts sharing >=85% similarity \nBLAT"]
		MatchedTranscriptsReads [label="Matched sequences"]
		CombinedReads -> MatchingReadsandTranscripts;
		UniqueTranscripts -> MatchingReadsandTranscripts;
		MatchingReadsandTranscripts -> MatchedTranscriptsReads;
		MatchedTranscriptsReads -> ChoosingTranscRead;

	#/*Filtering matched sequences*/
		subgraph cluster_filtering {
			label = "Filtering BLAT output"
			ChoosingTranscRead [label="choosing either transcript or genome skim sequences as basic sequences \nUNIX commands"]
			removeSequences [label="removing sequences with >1000 BLAT hits \nUNIX commands"]
			removeMaskedNuc [label="removing sequences with masked nucleotides \nUNIX commands"]
			ChoosingTranscRead -> removeSequences;
			removeSequences -> removeMaskedNuc;
		}

		FilteredSequences [label="Filtered sequences"]
		removeMaskedNuc -> FilteredSequences;
	}

	#/*Geneious/*
	subgraph cluster_geneious {
		label = "Geneious"
		Geneious [label="de novo assembly of BLAT hits into larger contigs \nGeneious"]
		AssembledSequences [label="Assembled sequences of filtered BLAT hits"]
		FilteredSequences -> Geneious;
		Geneious -> AssembledSequences;
	}
}

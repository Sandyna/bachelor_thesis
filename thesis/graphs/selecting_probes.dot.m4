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
	
	OProbes [label="Odontarrhena tortuosa \nprobes"]
	AProbes [label="Alyssum gmelinii \nprobes"]
	AMNGenes [label="Metal and nickel \nreference"]
	OMNGenes [label="Metal and nickel \nreference"]
	subgraph cluster_align {
		label="aligned using LAST"
		ASimAli [label=">=90% similarity \nand \n>=90% of probe aligned to reference"]
		OSimAli [label=">=90% similarity \nand \n>=90% of probe aligned to reference"]
		Aligned [label=">=90% similarity"]
	}
	EnoughBP [label=">=120pb length"]
	subgraph cluster_python {
		label="created using Python scripts"
		PriorityProbes [label="Prioritized probes"]
		AddRandom [label="Add probes from the rest of possible probes"]
	}
	milBP [label="1,000,000 base pairs of probes"]

	OProbes -> OSimAli;
	OMNGenes -> OSimAli;
	OProbes -> Aligned;
	AProbes -> ASimAli;
	AMNGenes -> ASimAli;
	AProbes -> Aligned;
	Aligned -> EnoughBP;
	
	EnoughBP -> PriorityProbes;
	ASimAli -> PriorityProbes;
	OSimAli -> PriorityProbes;
	PriorityProbes -> AddRandom;
	AddRandom -> milBP;
}

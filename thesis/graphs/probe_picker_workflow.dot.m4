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
	
	subgraph cluster_input {
		label="Input files"
		AllProbes [label="All possible probes"]
		KeepProbes [label="Probes we want \nin the result"]
		RemoveProbes [label="Probes we do not want \nin the result"]
	}

	subgraph cluster_param {
		label="Input parameters"
		TargetBP [label="Target number \nof base pairs"]
		Threshold [label="Threshold \nfor switching approach"]
	}

	subgraph cluster_probe_picker {
		label="Probe Picker";
		MatchingName [label="Creates a dictionary \nfor sequence name and sequence"]
#/*		SetKeep [label="Creates a set \nof sequence names to keep"]*/
#/*		SetRemove [label="Creates a set \nof sequence names to remove"]*/

		AllProbes -> MatchingName;
#/*		KeepProbes -> SetKeep;*/
#/*		RemoveProbes -> SetRemove;*/

		RemoveSeq [label="Removing probes \nwe don't want in the result"]
		FilteredProbes [label="Filtered probes"]
		RemoveProbes -> RemoveSeq;
		MatchingName -> RemoveSeq;
		RemoveSeq -> FilteredProbes;

		KeepSeq [label="Putting present sequences \n'to keep' into result"]
		RestOfSeq [label="Rest of the sequences"]
		KeepProbes -> KeepSeq;
		FilteredProbes -> KeepSeq;
		KeepSeq -> RestOfSeq;

		PickInOrder [label="Picking probes in order \n(longer sequences first)"]
		PickKnapsack [label="Filling the rest of space"]
		RestOfSeq -> PickInOrder;
		Threshold -> PickInOrder;
		PickInOrder -> PickKnapsack;
		TargetBP -> PickKnapsack;

	}
	subgraph cluster_output {
		label="Output data";
		result [label="Resulting probes with targer number of BP"]
		PickKnapsack -> result;
		KeepSeq -> result;
	}
}


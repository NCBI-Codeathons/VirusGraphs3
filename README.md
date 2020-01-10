# VirusGraphs3
Solidifying the VirusGraphs Infrastructure for Deployment

## Team

Alejandro Gener (lead)<br />
gener@bcm.edu; itspronouncedhenner@gmail.com<br />
Baylor College of Medicine, Houston, TX, USA<br />
MD Anderson Cancer Center, Houston, TX, USA<br />
Universidad Central del Caribe, Bayamón, PR, USA<br />

Nicolas Cooley<br />
npc19@pitt.edu<br />
Department of Biomedical Informatics, University of Pittsburgh, Pittsburgh PA, USA,15206<br />


Charles Scott Kirby<br />
ckirby4@jhmi.edu<br />
Johns Hopkins University School of Medicine, Baltimore, MD, USA<br />

Zhao Liu<br />
zhaol1@andrew.cmu.edu<br />
Computational Biology Department, Carnegie Mellon University, Pittsburgh, PA, USA<br />

Rahil Sethi<br />

Yutong Qiu<br />
yutongq@andrew.cmu.edu<br />
Computational Biology Department, Carnegie Mellon University, Pittsburgh, PA, USA<br />



## Linear reference genomes aren't great..

![](https://github.com/NCBI-Codeathons/VirusGraphs3/blob/master/limit_of_linear.png)
Linear references are the gold standard for genomics applications, including capturing viral genome information and viral sequence recovery. Examples include HIV sequence detection and HIV genome assembly. HIV genome assembly can be loosely classified into whole (reference) genome assebly and HIV genotyping (partial assembly).

## Workflow

![](https://github.com/NCBI-Codeathons/VirusGraphs3/blob/master/Virus_Graphs_3_Workflow_med_screen.tif)

## Implementation

### Reference graphs

For approximate k-mer graphs: [original SWIGG](https://github.com/NCBI-Codeathons/SWIGG), [implemented SWIGG](https://github.com/NCBI-Codeathons/Virus_Graphs).
For nucleobase graphs: [NovoGene](https://github.com/NCBI-Hackathons/NovoGraph)
[VG](https://github.com/vgteam/vg).

### Transcript modeling
For split-read mapping, [HISAT2](https://ccb.jhu.edu/software/hisat2/index.shtml) was used, and output .bam was pipped into
[StringTie](https://ccb.jhu.edu/software/stringtie/), both in [Galaxy](usegalaxy.eu).

### Visualization

SWIGG_shinny
IGV
SnapGene
Graphviz

## Results 

### for SWIGG

![SWIGG built for HIV2 (6 seqs)](https://github.com/NCBI-Codeathons/VirusGraphs3/blob/master/swigg_figure/HIV2_graph_merged.png)

The above figure contains 5 graphs built with different k-mer lengths. (a) k=16, (b) k=20, (c) k=32, (d) k=50, (e) k=90. Longer k-mers cover more repetitive regions. Therefore, longer k-mers result in simpler graphs. Red rectangles highlights the large loop topology in graphs made by small k-mers. The loops are the results of the repeititive k-mers in regions far apart. 



### for NovoGraph

Current NovoGraph script..

### for VG

### HIV-1 transcript model





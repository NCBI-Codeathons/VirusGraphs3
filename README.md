# VirusGraphs3
Solidifying the VirusGraphs Infrastructure for Deployment

## Team

Alejandro Gener (lead)<br />
gener@bcm.edu; itspronouncedhenner@gmail.com<br />
Baylor College of Medicine, Houston, TX, USA<br />
MD Anderson Cancer Center, Houston, TX, USA<br />
Universidad Central del Caribe, Bayamón, PR, USA<br />

Nicolas Cooley<br />

Charles Scott Kirby<br />
ckirby4@jhmi.edu<br />
Johns Hopkins University School of Medicine, Baltimore, MD, USA<br />

Zhao Liu<br />

Rahil Sethi<br />

Yutong Qiu<br />
yutongq@andrew.cmu.edu<br />
Computational Biology Department, Carnegie Mellon University, Pittsburgh, PA, USA<br />



## Limitations of virus graphs

(https://github.com/NCBI-Codeathons/VirusGraphs3/blob/master/limit_of_linear.pdf)

## Workflow

(https://github.com/NCBI-Codeathons/VirusGraphs3/blob/master/Virus_Graphs_3_Workflow_med_screen.tif)

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

## Results 

### for SWIGG

Current SWIGG script..

### for NovoGraph

Current NovoGraph script..

### for VG

### HIV-1 transcript model





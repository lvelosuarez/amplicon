# Snakemake_amplicon
<img src="pipeline.png" align="center" alt="Pipeline" />
This workflow is an implementation of the dada2 library. I followed the steps in the [Tutorial](https://benjjneb.github.io/dada2/tutorial.html). I use Silva for taxonomic annotation.

## Usage
### Install workflow
To use this workflow, download and extract the [latest release](https://github.com/snakemake-workflows/amplicon-seq-dada2/releases).
#### Dependencies:
The pipeline has some dependencies which can be installed with conda:

## Run
```bash
snakemake --use-conda -j15
```

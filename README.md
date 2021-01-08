# DSVifier
## What's the problem?
Mixed tissue samples contain a variety of variants.
While many of these variants are legitimate biological signal, not all variants should necessarily be implicated in the diease of interest.
The objective of this project is to take annotated variants from mixed tissue samples and identify variants that are likely associated with the disease being studied while accounting for confounding effects, such as population stratification.

## Why should we solve it?
Associating variants with a particular disease enhances our understanding of its genetic provenance.
More practically, variants from mixed samples can guide clinicians during diagnosis and treatment, and aid drug developers in the identification of gene targets.

## Workflow Diagram
![Workflow Diagram](images/workflow_v5.png "Workflow Diagram")

## How to use ?
This pipeline is conceived to be used with the data generated with the [Trinity CTAT pipeline](https://github.com/collaborativebioinformatics/expressed-variant-impact). The output data can then be used by the [viravate2 pipeline](https://github.com/collaborativebioinformatics/viravate2) and integrated in clinical reports with the [snpReportR](https://github.com/collaborativebioinformatics/expressed-variant-reporting). 

The `Somalier`can allow to identify sample swaps or duplicates in a file [@pedersenSomalierRapidRelatedness2020]. It will also give information on the ancestry or relatedness of the samples if the dataset is big enough >1000 samples.
GWAS need a relatively important set of data to give accurate results (>10000).



### Dependencies
* [GLnexus](https://github.com/dnanexus-rnd/GLnexus)
* [PLINK](http://zzz.bwh.harvard.edu/plink/)
* [somalier 0.2.12](https://github.com/brentp/somalier)
* [CAVIAR](http://genetics.cs.ucla.edu/caviar/manual.html)
* GWAS pipeline

### Installation
The DSVifier pipeline has not been implemented as a production pipeline, so a turn-key installation is not available.
However, the pipeline is composed of readily available bioinformatic tools/pipelines (see Dependencies).
Each tool's installation process can be found by following the provided links.
Additaionlly, these tools are available on the DNAnexus platform, which we used when developing the pipeline.

In the case of Somalier, the provided Jupyter notebook depends on DNAnexus.

In the case of CAVIAR, we leave it to users to use a GWAS pipeline that best fits their data/study.

### Inputs
Input data format is CVF format as it is the standard format for storing variation data (ref), because it is unambiguous, scalable and flexible.
For the `Somalier` analysis, the site file used in this example can be find here: [sites.hg38.rna.vcf.gz](https://github.com/brentp/somalier/files/4566475/sites.hg38.rna.vcf.gz).
* Data from [expressed-variant-impact](https://github.com/collaborativebioinformatics/expressed-variant-impact):
  * variant vcf files (fully annotated variant calls from HaplotypeCaller)
  * `cancer.vcf` and `cancer.tab` (a set of prioritized cancer-relevant variants detected in the sample)
* Data from [viravate2](https://github.com/collaborativebioinformatics/viravate2):
  * "A large table with DE results and associated variants. This would include things like gene names, logFC values, significance values, and then the variant information."

![Example of an input .vcf file](images/sample_vcf.png "sample of a .vcf file")

### Outputs
* Data for [expressed-variant-reporting](https://github.com/collaborativebioinformatics/expressed-variant-reporting):
  * See [inputs docs](https://docs.google.com/spreadsheets/d/1pcB_bI_83B__sJ_Qw3tYDUhAYTz7Bh9SBvxjMzd8L4U/edit#gid=0)
* Data for [viravate2](https://github.com/collaborativebioinformatics/viravate2):
  * VCF file containig variants associated with population stratification or tumors

### Validation dataset
**Somalier:**

The tool does not seem to resolve the ancestry and relatedness, but that is not surprising, because the genome sketch is based on the 1000 genomes project.
A possible resolution could be achieved by using a genome sketch based on cell lines. So finding the normal samples and using the instructions from the somalier github to generate the sketches as well as a set of labels for the cells associated with each sketch.
There are data sets that can be used to generate these genome sketches (https://www.ebi.ac.uk/ega/studies/EGAS00001000610 and https://www.nature.com/articles/nbt.3080 - not sure if this one contains our cells). 
Or, another option to test this method is to use another data set that would align to the 1000 genomes genome sketch.  I looked around but did not want to use any controlled data sets for this project because we are putting it out on github.  One intriguing option was to test the tool using files from the Personal Genome Project, but that would not be disease-related.



## References


## People/Team
James Baye  
Alan Cleary  
Virginie Grosboillot  
Sam Hokin  
Adelaide Rhodes  
Chaitanya Srinivasan  

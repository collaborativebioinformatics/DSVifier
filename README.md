# Disease Specific Variant identifier
![logo](DSVifier.png "DSVifier logo")


## What's the problem?
Mixed tissue samples contain a variety of variants.
While many of these variants are legitimate biological signal, not all variants should necessarily be implicated in the diease of interest.
The objective of this project is to take annotated variants from mixed tissue samples and identify variants that are likely associated with the disease being studied while accounting for confounding effects, such as population stratification.


## Why should we solve it?
Associating variants with a particular disease enhances our understanding of its genetic provenance.
More practically, variants from mixed samples can guide clinicians during diagnosis and treatment, and aid drug developers in the identification of gene targets.


## Workflow diagram
![Workflow Diagram](images/workflow_v5.png "Workflow Diagram")


## How to use?
This pipeline performs two different analyses: one with Somalier and one with CAVIAR.
Both tools consume VCF files output by the [Trinity CTAT pipeline](https://github.com/collaborativebioinformatics/expressed-variant-impact).
The data output by Somalier can be used to extract informative sites, evaluate relatedness of variants, and perform quality-control.
It can also be integrated in clinical reports with the [snpReportR](https://github.com/collaborativebioinformatics/expressed-variant-reporting).
The data output by CAVIAR can be used to evaluate which variants are likely casual and can be used in downstream analyses, such as the [viravate2 pipeline](https://github.com/collaborativebioinformatics/viravate2).

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

A Somalier example is provided as a Jupyter notebook, which depends on DNAnexus and uses the site file [sites.hg38.rna.vcf.gz](https://github.com/brentp/somalier/files/4566475/sites.hg38.rna.vcf.gz).

In the case of CAVIAR, we leave it to users to use a GWAS pipeline that best fits their data/study.

### Inputs
* PLINK is used to determine LD across the samples, generating an LD file for input into CAVIAR, which looks like this:
```
 CHR_A         BP_A SNP_A  CHR_B         BP_B SNP_B           R2 
     1      6634453    .      1      6634454    .            1 
     1      6635063    .      1      6635184    .            1 
     1      6635063    .      1      6888144    .            1 
     1      6888144    .      1      7780866    .            1 
     1     10413143    .      1     10419734    .     0.315315 
     1     10413143    .      1     10430824    .         0.25 
     1     10413143    .      1     10431152    .          0.2 
     1     10419734    .      1     10430824    .         0.25 
     1     10419734    .      1     10431152    .          0.2 
     1     20650728    .      1     20650956    .     0.333333 
     ...
```
(vcf-merge was used to create a single VCF from the many individual-sample VCFs).
* Both Somalier and CAVIAR require files derived from the [Trinity CTAT pipeline](https://github.com/collaborativebioinformatics/expressed-variant-impact)
* CAVIAR also requires haplotype information for the population being studied, such as HapMap data from the 1000 genomes project

An example input VCF file:
![Example of an input .vcf file](images/sample_vcf.png "sample of a .vcf file")

### Outputs
**Somalier:**
* HTML files describing various relationships among the input variants
* TSV files containing the data visualized in the HTML files

**CAVIAR:**
* Our pipeline annotates the input VCF files statistics generated from CAVIAR (see the [CAVIAR GitHub](https://github.com/fhormoz/caviar) for a complete list our output files

## Evaluation

### Validation dataset
The VCF data used for this project were taken from the study "Characterization of cancer omics and drug perturbations in panels of lung cancer cells" (https://doi.org/10.1038/s41598-019-55692-9).

**Somalier:**

**CAVIAR:**

The VCF data represents samples taken from a Japanese population, so we used the Japanese HapMap available from the 1000 Genomes Project.

### Results
**Somalier:**

Somalier does not seem to resolve the ancestry and relatedness, but that is not surprising, because the genome sketch is based on the 1000 genomes project.
A possible resolution could be achieved by using a genome sketch based on cell lines, so finding the normal samples and using the instructions from the Somalier GitHub to generate the sketches as well as a set of labels for the cells associated with each sketch.
There are data sets that can be used to generate these genome sketches (https://www.ebi.ac.uk/ega/studies/EGAS00001000610 and https://www.nature.com/articles/nbt.3080 - not sure if this one contains our cells). 
Or, another option to test this method is to use another data set that would align to the 1000 genomes genome sketch.
However, we did not want to use any controlled data sets for this project because we are putting it out on GitHub.
One intriguing option was to test the tool using files from the Personal Genome Project, but that would not be disease-related.

**CAVIAR:**
Unfortunately we were not able to obtain CAVIAR results for this study.
This is because the samples in the dataset correspond to cell cultures, rather than individuals within the population.
Subsequently, there was no phenotypic information available on which to build a GWAS anlysis.
Additionally, the samples corresponded to a variety of different treatments, meaning there was no subpopulation that could be used as a control.
Lastly, the number of samples was too small for any GWAS summary statistics to have any significance.

## Future work
The validation dataset was chosen as part of a "Bringing Pivotal SNPs for Differential RNAseq Profiles to the Clinic!" hackathon.
While it wasn't ideal for our pipeline, it accommodated other teams, such as the team working on the [viravate2 pipeline](https://github.com/collaborativebioinformatics/viravate2).
Specifically, the dataset represented mixed tissue samples from patients with lung cancer that had been administered different treatments.
This makes the data ammenable to eQTL analysis.
Interestingly, there is a variant of CAVIAR called eCAVIAR that, in addition to GWAS statistics, takes eQTL data into consideration when identifying causal variants.
If GWAS analysis could have also been performed on this dataset (as discuessed in the CAVIAR results) then this could've been used to create a feedback loop between DSVifier and viravate2 to rapidly assess treatments in a clincial environment, perhaps even on a personalized level.

We would like to note the the CAVIAR pipeline could be further enhanced using [LD score regression](https://doi.org/10.1038/ng.3211).
Such techniques would help remove confounding biases from the samples, which could help further refine the set of variants that should be targeted by downstream analyses and clinical trials.

## References


## People/Team
James Baye  
Alan Cleary  
Virginie Grosboillot  
Sam Hokin  
Adelaide Rhodes  
Chaitanya Srinivasan  

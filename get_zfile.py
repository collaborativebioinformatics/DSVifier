import glob

'''
Description : parse each UNFILTERED vcf-format file of variants and output a .Z file of rsids and Z scores for input to caviar

Usage: 

    python3 get_zfile.py

Requirements:
    - Script is in the same folder as the PRJDB6952 directory
    - glob

Output: For each *.cancer.vcf file, the output is of form *.cancer.Z with two tabulated columns containing the RSID and z-score.
'''

def make_z_file(file):
    # read in data
    with open(file, "r") as f:
        contents = f.read().splitlines()
    f.close()
    # search for SNPs with valid rsid and z-score
    with open(file[:-3]+"Z", "w") as z:
        for line in contents:
            if line[0] == "#":
                # ignore line
                continue
            else:
                try:
                    rsid = "rs"+(line.split("\t")[7].split("RS=")[1].split(";")[0])
                    z_score = (line.split("\t")[7].split("ReadPosRankSum=")[1].split(";")[0])
                    z.write(rsid + "\t" + z_score + "\n")
                except:
                    # no rsid or z score found
                    continue
    
    z.close()
    return

def main():
    for file in glob.glob("PRJDB6952/*.cancer.vcf"):
        make_z_file(file)

if __name__ == "__main__":    
    main()

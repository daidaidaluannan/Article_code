import csv
import os
import numpy as np
import pandas as pd

eqtl_path = "/home/wcy/data/Tool_Data/smr/eqtls/"
gwas_path = "/home/wcy/data/UKB/test_data/eye_gwas/cgwas/result_0720/C-GWAS_hg38.txt"
save_path = "/home/wcy/data/UKB/test_data/eye_gwas/coloc/GTex/"
loci_path = "/home/wcy/data/UKB/test_data/eye_gwas/coloc/GenomicRiskLoci.txt"
file_list = "/home/wcy/data/UKB/test_data/eye_gwas/coloc/GTex/file_list.txt"


gwas = pd.read_csv(gwas_path,'\t')
gwas = gwas.drop(columns=['STATUS'])
gwas.rename(columns={'P': 'snp_p','EAF': 'maf_snp', 'rsID': 'SNP'}, inplace=True)
gwas['variant_id'] = gwas.apply(lambda row: f"chr{row['CHR']}_{row['POS']}_{row['NEA']}_{row['EA']}_b38", axis=1)

loci = pd.read_csv(loci_path,'\t')
file_list = pd.read_csv(file_list,header=None)
target_snps = loci['rsID']

for folder_name in file_list[0]:
    result_folder = save_path + folder_name + "/"
    eqtl_file = eqtl_path + folder_name + ".v8.EUR.signif_pairs.txt"
    os.makedirs(result_folder, exist_ok=True)

    eqtl = pd.read_csv(eqtl_file,'\t')
    eqtl = eqtl.drop(columns=["tss_distance", "pval_nominal_threshold", "min_pval_nominal", "pval_beta"])
    eqtl.rename(columns={"phenotype_id": 'gene_id',"pval_nominal": 'p_gene',"slope": 'gene_slope',"slope_se": 'gene_slope_se'}, inplace=True)
    
    
    for  target_snp in target_snps:
        target_row = gwas[gwas['SNP'] == target_snp]
        traget_chr = target_row['CHR'].values[0]
        target_bp = target_row['POS'].values[0]
        chr_condition = gwas['CHR'] == traget_chr
        pos_condition = (gwas['POS'] >= target_bp - 500000) & (gwas['POS'] <= target_bp + 500000)

        result = gwas[chr_condition & pos_condition]
        merge_data = pd.merge(result,eqtl,on="variant_id")
        merge_lead = merge_data.sort_values('p_gene').drop_duplicates(subset='SNP', keep='first')

        result_path = result_folder + target_snp + ".txt"
        merge_lead.to_csv(result_path,'\t',index=False,header=True)

    print(folder_name," complete")

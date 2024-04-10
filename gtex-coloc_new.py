import csv
import os
import numpy as np
import pandas as pd
import dask.dataframe as dd

eqtl_path = "/home/wcy/data/Tool_Data/smr/test/"
gwas_path = "/home/wcy/data/UKB/test_data/eye_gwas/cgwas/result_0720/C-GWAS_hg38.txt"
save_path = "/home/wcy/data/UKB/test_data/eye_gwas/coloc/GTex_new/"
loci_path = "/home/wcy/data/UKB/test_data/eye_gwas/coloc/GenomicRiskLoci.txt"
file_list = "/home/wcy/data/UKB/test_data/eye_gwas/coloc/GTex/file_list_new.txt"

selected_columns = ['variant', 'rsid', 'pvalue', 'maf', 'gene_id']


gwas = pd.read_csv(gwas_path,sep='\t')
gwas = gwas.drop(columns=['STATUS'])
gwas.rename(columns={'P': 'snp_p','EAF': 'maf_snp', 'rsID': 'rsid'}, inplace=True)
gwas['variant_id'] = gwas.apply(lambda row: f"chr{row['CHR']}_{row['POS']}_{row['NEA']}_{row['EA']}_b38", axis=1)

loci = pd.read_csv(loci_path,sep='\t')
file_list = pd.read_csv(file_list,header=None)
target_snps = loci['rsID']

for folder_name in file_list[0]:
    result_folder = save_path + folder_name + "/"
    eqtl_file = eqtl_path + folder_name + ".tsv"
    os.makedirs(result_folder, exist_ok=True)

    eqtl = pd.read_csv(eqtl_file,sep='\t',usecols=selected_columns)
   


    for  target_snp in target_snps:
        target_row = gwas[gwas['rsid'] == target_snp]
        traget_chr = target_row['CHR'].values[0]
        target_bp = target_row['POS'].values[0]
        chr_condition = gwas['CHR'] == traget_chr
        pos_condition = (gwas['POS'] >= target_bp - 500000) & (gwas['POS'] <= target_bp + 500000)

        result = gwas[chr_condition & pos_condition]
        merge_data = pd.merge(result,eqtl,on="rsid")
        merge_lead = merge_data.sort_values('pvalue').drop_duplicates(subset='rsid', keep='first')

        result_path = result_folder + target_snp + ".txt"
        merge_lead.to_csv(result_path,sep='\t',index=False,header=True)
    
    print(folder_name," complete")

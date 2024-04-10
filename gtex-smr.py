import csv
import os
import numpy as np
import pandas as pd

eqtl_path = "/home/wcy/data/Tool_Data/smr/eQTL_besd_lite/"
gwas_path = "/home/wcy/data/UKB/test_data/eye_gwas/smr/0721/C-GWAS_hg19.ma"
bfile_path = "/home/wcy/data/UKB/test_data/eye_gwas/gene/eye_gene"
save_path = "/home/wcy/data/UKB/test_data/eye_gwas/smr/0721/result/"
file_list = "/home/wcy/data/UKB/test_data/eye_gwas/smr/0721/file_list.txt"


file_list = pd.read_csv(file_list,header=None)


for file_name in file_list[0]:
    eqtl_file = eqtl_path + file_name + ".lite"
    save_file = save_path + file_name
    
    cmd = f"~/python_code/smr_linux_x86_64 --bfile {bfile_path} --gwas-summary {gwas_path} --beqtl-summary {eqtl_file} --out {save_file} --thread-num 70"
    os.system(cmd)
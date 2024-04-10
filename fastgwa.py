import csv
import os
import numpy as np
import pandas as pd


file = "/home/wcy/data/UKB/test_data/eye_gwas/after_deepnull/replace/pheno/file_new.txt"
input_path = "/home/wcy/data/UKB/test_data/eye_gwas/after_deepnull/replace/pheno/"
out_path = "/home/wcy/data/UKB/test_data/eye_gwas/after_deepnull/replace/fastgwa_result/"
qcovar = "/home/wcy/data/UKB/test_data/eye_gwas/after_deepnull/replace/cov_data/qcovar_new.txt"
covar = "/home/wcy/data/UKB/test_data/eye_gwas/after_deepnull/replace/cov_data/covar_new.txt"
bfile = "/home/wcy/data/UKB/test_data/eye_gwas/gene/eye_gene"
grm_sparse = "/home/wcy/data/UKB/test_data/0702/deepnull/sp_grm"

file_list = pd.read_csv(file,header=None)


for file_name in file_list[0]:
    input = input_path + file_name
    new_filename = file_name.replace(".txt", "")
    save_file = out_path + new_filename
    
    cmd = f"~/python_code/gcta/gcta-1.94.1 --bfile {bfile}  --grm-sparse {grm_sparse}  --fastGWA-mlm  --pheno {input} --qcovar {qcovar}  --covar {covar} --thread-num 70 --out {save_file}"
    os.system(cmd)
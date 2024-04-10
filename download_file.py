import csv
import os
import numpy as np
import pandas as pd
import dask.dataframe as dd

file_list = "/home/wcy/data/UKB/test_data/eye_gwas/coloc/GTex/file_list.txt"
save_dir = "/home/wcy/data/Tool_Data/smr/test/"
web = "ftp://ftp.ebi.ac.uk/pub/databases/spot/eQTL/imported/GTEx_V8/ge/"

file_list = pd.read_csv(file_list,header=None)


for file_name in file_list[0]:
    eqtl_file = web + file_name + ".tsv.gz"
    cmd = f"wget -P {save_dir}  {eqtl_file}"
    os.system(cmd)

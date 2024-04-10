import csv
import os
import numpy as np
import pandas as pd

bfile = "/home/wcy/data/UKB/test_data/eye_gwas/gene/eye_gene"
pheno = "/home/wcy/data/UKB/test_data/eye_gwas/bolt_lmm/pheno_new.txt"
save_path = "/home/wcy/data/UKB/test_data/eye_gwas/bolt_lmm/"
#file_list = ['Artery_Fractal_dimension', 'Artery_Vessel_density',
#       'Artery_Average_width', 'Artery_Distance_tortuosity',
#       'Artery_Squared_curvature_tortuosity', 'Artery_Tortuosity_density',
#       'Vein_Fractal_dimension', 'Vein_Vessel_density', 'Vein_Average_width',
#       'Vein_Distance_tortuosity', 'Vein_Squared_curvature_tortuosity',
#       'Vein_Tortuosity_density', 'CDR_vertical']

file_list = ['CRVE_Hubbard', 'AVR_Hubbard',
       'CRAE_Knudtson', 'CRVE_Knudtson','AVR_Knudtson']


for file_name in file_list:
    save_file = save_path + file_name + ".stats"
    cmd = f" ~/python_code/BOLT-LMM_v2.4.1/bolt --bfile {bfile} --phenoFile {pheno} --phenoCol {file_name} --covarFile {pheno} --covarCol 31-0.0 --covarCol 20116-0.0 --covarCol 20117-0.0 --qCovarCol pca1 --qCovarCol pca2 --qCovarCol pca3 \
        --qCovarCol pca4 --qCovarCol pca5 --qCovarCol pca6 --qCovarCol pca7 --qCovarCol pca8 --qCovarCol pca9 --qCovarCol pca10 \
        --qCovarCol 21001-0.0 --qCovarCol 21003-0.0 --lmm --LDscoresFile /home/wcy/python_code/BOLT-LMM_v2.4.1/tables/LDSCORE.1000G_EUR.tab.gz --numThreads=70 --statsFile={save_file}  --maxModelSnps 6000000"
    os.system(cmd)
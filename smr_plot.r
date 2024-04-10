rm(list=ls())
source("/home/wcy/data/Tool_Data/smr/plot/plot_SMR.r") 
# Read the data file in R:
SMRData = ReadSMRData("/home/wcy/data/UKB/test_data/eye_gwas/smr/0716/plot/Artery_Tibial_eqtl.ENSG00000182612.txt")
# Plot the SMR results in a genomic region centred around a probe:
SMRLocusPlot(data=SMRData, smr_thresh=8.4e-6, heidi_thresh=0.05, plotWindow=1000, max_anno_probe=16)

SMREffectPlot(data=SMRData, trait_name="BMI") 
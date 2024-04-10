library(coloc)

#gwas_data <- read.table("/home/wcy/data/UKB/test_data/eye_gwas/coloc/eye_gwas.txt", header=T)
etql_data <- read.table("/home/wcy/data/UKB/test_data/eye_gwas/coloc/eye_eqtl.txt", header=T)

#result <- coloc.abf(dataset1 = list(pvalues=eqtl_data$snp_p,type="quant",N=26181,snp = eqtl_data$SNP),
#dataset2 = list(pvalues=eqtl_data$gene_p,type="quant",N=523),MAF = eqtl_data$maf)
#head(eqtl_data)
dataset1 <- list(pvalues=gwas_data$snp_p,type="quant",N=26181,snp = gwas_data$SNP, MAF = gwas_data$maf)
dataset2 <- list(pvalues=etql_data$gene_p,type="quant",N=523,snp = etql_data$SNP, MAF = gwas_data$maf)
check_dataset(dataset2, req = c("type", "snp", "pvalues"), warn.minp = 1e-06)
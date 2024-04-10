library(argparser,quietly = TRUE)
require(stringr)

p <- arg_parser("QC pipline")
p <- add_argument(p, "--input_dir", help = "input_dir", type = "character")
p <- add_argument(p, "--output_dir", help = "output_dir", type = "character")
argv <- parse_args(p)

input_dir <- argv$input_dir
output_dir <- argv$output_dir

data <- read.delim(input_dir, header = T, stringsAsFactors = F)
fdr <- p.adjust(data$p_SMR , method='BH')
result <- data.frame(data, p_adjust = fdr)
write.csv(result, output_dir, row.names = F)
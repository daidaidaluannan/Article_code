import os

input_folder = '/home/wcy/data/UKB/test_data/eye_gwas/fastgwa_result/'
output_folder = '/home/wcy/data/UKB/test_data/eye_gwas/ldsc_data/'

# 获取文件夹中的所有 TSV 文件路径
tsv_files = [f for f in os.listdir(input_folder) if f.endswith('.fastGWA')]

# 循环处理每个 TSV 文件
for tsv_file in tsv_files:
    target = tsv_file.split('.fastGWA')[0]
    input_path = os.path.join(input_folder, tsv_file)
    output_path = os.path.join(output_folder, target)
    
    # 构建命令行参数
    cmd = f"python ~/python_code/ldsc/munge_sumstats.py --sumstats={input_path}  --N 26181 --out={output_path}  --merge-alleles ~/python_code/ldsc/tool_data/w_hm3.snplist"
    
    # 执行命令
    os.system(cmd)

import os
import json
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

#print("Wait 3 hours...")
#time.sleep(3*60*60)

os.chdir("/home/wcy/data/Tool_Data/smr/eye_qtl_new/result")

# 假设基因列表为以下内容
gene_list_file = '/home/wcy/data/Tool_Data/smr/eye_qtl_new/error_log_0813_2.txt'
with open(gene_list_file, 'r') as file:
    gene_list = [line.strip() for line in file]

# 定义保存数据的函数
def save_data():
    # 将总数据列表存储为CSV文件
    csv_file_name = f"{gene}.csv"
    with open(csv_file_name, "w", newline="") as csvfile:
        fieldnames = all_data_list[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in all_data_list:
            writer.writerow(item)
    print(gene, "has been processed.")




# 循环遍历基因列表
for index, gene in enumerate(gene_list):
    try:
        # 创建一个ChromeOptions实例
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")

        # 创建一个Chrome驱动服务
        service = Service('/home/wcy/chmod/chromedriver')

        # 创建一个参数字典，包括service和chrome_options
        driver = webdriver.Chrome(service=service, options=chrome_options)


        # 等待页面加载
        driver.implicitly_wait(40)  # 等待10秒钟

        # 打开目标网站
        url = 'http://eye-eqtl.com/'
        driver.get(url)

        # 构建一个总的数据列表
        all_data_list = []

        # 找到具有id为"gene_search"的输入框
        gene_search_input = driver.find_element(By.ID, 'gene_search')

        # 在输入框中输入基因名
        gene_search_input.clear()  # 清空输入框内容
        gene_search_input.send_keys(gene)

        if index == 0:
            # 第一次循环点击class为'btn-primary'的按钮
            search_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
        else:
            # 后续循环点击class为'btn'的按钮
            search_button = driver.find_element(By.CLASS_NAME, 'btn')

        # 模拟点击按钮
        search_button.click()

        # 获取搜索结果页面内容
        search_result_content = driver.page_source

        data_div = driver.find_element(By.ID, 'div-data')

        # 获取data属性的值
        data_attr_value = data_div.get_attribute('data')

        # 将字符串转换为Python字典或列表（根据实际情况）
        data_list = json.loads(data_attr_value)

        # 将当前基因的数据添加到总的数据列表中
        all_data_list.extend(data_list)
        save_data()
        driver.quit()
        time.sleep(1)
    
    except Exception as e:
        with open("error_log.txt", "a") as error_log:
                error_log.write(f"{gene}\n")
        print(f"Error for gene {gene}: {str(e)}. Skipping...")


    

    



import pandas as pd
import os

# 定义文件夹路径和文件命名格式
input_folder_path = "D:\\Intelligent_ecommerce\\filter_data\\split_on_category"
output_folder_path = "D:\\Intelligent_ecommerce\\filter_data\\split_on_category_csv"
file_prefix = "filtered_data2_category"
file_extension = ".xlsx"
output_extension = ".csv"

# 确保输出文件夹存在
os.makedirs(output_folder_path, exist_ok=True)

# 遍历每个文件，去掉第一行并转成csv格式
for i in range(1, 32):
    file_name = f"{file_prefix}{i}{file_extension}"
    file_path = os.path.join(input_folder_path, file_name)
    
    # 加载Excel文件并去掉第一行
    data = pd.read_excel(file_path, skiprows=1)
    
    # 保存为CSV文件
    output_file_name = f"{file_prefix}{i}{output_extension}"
    output_file_path = os.path.join(output_folder_path, output_file_name)
    data.to_csv(output_file_path, index=False)
    
print("所有文件已处理并保存为CSV格式。")

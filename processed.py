import pandas as pd

# 加载Excel文件
file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2_merged.xlsx"
data = pd.read_excel(file_path)

# 删除第6列和第33列
data.drop(data.columns[[5, 32]], axis=1, inplace=True)

# 保存修改后的数据到新的Excel文件
output_file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2_processed1.xlsx"
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    data.to_excel(writer, index=False, sheet_name='Sheet1')

    # 获取XlsxWriter workbook和worksheet对象
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # 设置格式以避免科学计数法
    number_format = workbook.add_format({'num_format': '0'})
    
    # 遍历所有列，应用格式
    for col_num, col in enumerate(data.columns):
        max_len = max(data[col].astype(str).map(len).max(), len(col)) + 1
        worksheet.set_column(col_num, col_num, max_len, number_format)

print(f"修改后的文件已保存到: {output_file_path}")

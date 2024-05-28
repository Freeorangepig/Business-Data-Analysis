import pandas as pd

# 加载Excel文件
file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2_processed3.xlsx"
data = pd.read_excel(file_path)

# 将第8列的唯一值映射为整数，包括空值
category_mapping = {str(name): idx+1 for idx, name in enumerate(data.iloc[:, 7].astype(str).fillna("空值").unique())}
data[data.columns[7]] = data[data.columns[7]].astype(str).map(category_mapping)

# 保存修改后的数据到新的Excel文件
output_file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2_processed4.xlsx"
with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
    data.to_excel(writer, index=False, sheet_name='Sheet1')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 设置格式以避免科学计数法
    number_format = workbook.add_format({'num_format': '0'})
    
    # 遍历所有列，应用格式
    for col_num, col in enumerate(data.columns):
        max_len = max(data[col].astype(str).map(len).max(), len(col)) + 1
        worksheet.set_column(col_num, col_num, max_len, number_format)

# 输出对应表，注意包括空值
category_df = pd.DataFrame(list(category_mapping.items()), columns=['类目', '编号'])

# 保存映射表到新的Excel文件
mapping_output_file_path = "D:\\Intelligent_ecommerce\\filter_data\\mapping_tables_category_processed3.xlsx"
with pd.ExcelWriter(mapping_output_file_path, engine='xlsxwriter') as writer:
    category_df.to_excel(writer, index=False, sheet_name='类目映射')

print("数据处理和映射表生成完成。")

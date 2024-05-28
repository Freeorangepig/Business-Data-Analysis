import pandas as pd

# 加载Excel文件
file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2_processed1.xlsx"
data = pd.read_excel(file_path)

# 将第三列的市场名称列，相同的市场名称赋予1、2以此类推这样的标号
market_name_mapping = {name: idx+1 for idx, name in enumerate(data.iloc[:, 2].unique())}
data[data.columns[2]] = data[data.columns[2]].map(market_name_mapping)

# 保存修改后的数据到新的Excel文件
output_file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2_processed2.xlsx"
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

# 输出对应表
market_name_df = pd.DataFrame(list(market_name_mapping.items()), columns=['市场名称', '编号'])

# 保存映射表到新的Excel文件
mapping_output_file_path = "D:\\Intelligent_ecommerce\\filter_data\\mapping_tables_market_name.xlsx"
with pd.ExcelWriter(mapping_output_file_path, engine='xlsxwriter') as writer:
    market_name_df.to_excel(writer, index=False, sheet_name='市场名称映射')

print("数据处理和映射表生成完成。")

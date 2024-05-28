import pandas as pd

# 加载Excel文件
file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2.xlsx"
data = pd.read_excel(file_path)

# 定义类目合并规则
category_mapping = {
    '茄果类': '总茄果类',
    '自营茄果类': '总茄果类',
    '根茎类': '总根茎类',
    '自营根茎类': '总根茎类',
    '叶菜类': '总叶菜类',
    '自营叶菜类': '总叶菜类'
}

# 应用映射规则，将小类目合并到目标类目
data['类目'] = data['类目'].apply(lambda x: category_mapping.get(x, x))

# 统计合并后的类目数量
merged_category_counts = data['类目'].value_counts()

# 输出合并后的类目总数和各自名称和数量
total_merged_categories = merged_category_counts.shape[0]
category_counts_df = pd.DataFrame(merged_category_counts).reset_index()
category_counts_df.columns = ['Category', 'Count']

# 输出结果
print(f"Total Merged Categories: {total_merged_categories}")
print(category_counts_df.to_string(index=False))

# 保存修改后的数据到新的Excel文件
output_file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2_merged.xlsx"
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

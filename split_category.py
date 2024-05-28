import pandas as pd

# 加载Excel文件
file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2_processed5.xlsx"
data = pd.read_excel(file_path)

# 获取第5列的类目列
category_column = data.columns[4]

# 按类目列分组
groups = data.groupby(category_column)

# 为每个类目创建一个单独的Excel文件
for category, group in groups:
    output_file_path = f"D:\\Intelligent_ecommerce\\filter_data\\split_on_category\\filtered_data2_category{category}.xlsx"
    
    with pd.ExcelWriter(output_file_path, engine='xlsxwriter') as writer:
        group.to_excel(writer, index=False, sheet_name='Sheet1')

        # 获取XlsxWriter workbook和worksheet对象
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # 设置格式以避免科学计数法
        number_format = workbook.add_format({'num_format': '0'})
        
        # 遍历所有列，应用格式并自动调整列宽
        for col_num, col in enumerate(group.columns):
            max_len = max(group[col].astype(str).map(len).max(), len(col)) + 1
            worksheet.set_column(col_num, col_num, max_len, number_format)

print("数据分割完成。")

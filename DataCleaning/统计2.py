import pandas as pd

# 定义文件路径
file_path = r"D:\Intelligent_ecommerce\DataCleaning\data\top_100_products.xlsx"
output_path = r"D:\Intelligent_ecommerce\DataCleaning\data\category_statistics_100.xlsx"

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 获取第3列类目
category_column = df.iloc[:, 2]

# 统计有多少种类目和各类目的数量
category_counts = category_column.value_counts()

# 将结果保存到DataFrame中
category_df = category_counts.reset_index()
category_df.columns = ['类目', '数量']

# 保存统计信息到新的Excel文件
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    category_df.to_excel(writer, index=False, sheet_name='Category Statistics')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Category Statistics']

    # 动态调整列宽
    for col_num, col in enumerate(category_df.columns):
        max_len = max(category_df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(col_num, col_num, max_len)

print(f"统计信息已保存到 {output_path}")

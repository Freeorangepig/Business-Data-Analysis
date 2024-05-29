import pandas as pd

# 定义文件路径
file_path = r"D:\Intelligent_ecommerce\DataCleaning\data\top_100_products.xlsx"
output_path = r"D:\Intelligent_ecommerce\DataCleaning\data\grouped_by_category_100.xlsx"

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 统计各类目的数量
category_counts = df.iloc[:, 2].value_counts()

# 初始化一个新的DataFrame用于存储分组后的数据
grouped_df = pd.DataFrame()

# 按类目数量由大到小进行排序，并将相同类目的数据放在一起
for category in category_counts.index:
    category_df = df[df.iloc[:, 2] == category]
    grouped_df = pd.concat([grouped_df, category_df])

# 重置索引
grouped_df.reset_index(drop=True, inplace=True)

# 保存分组后的数据到新的Excel文件
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    grouped_df.to_excel(writer, index=False, sheet_name='Grouped by Category')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Grouped by Category']

    # 动态调整列宽
    for col_num, col in enumerate(grouped_df.columns):
        max_len = max(grouped_df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(col_num, col_num, max_len)

print(f"分组后的数据已保存到 {output_path}")

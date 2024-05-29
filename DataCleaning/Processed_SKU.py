import pandas as pd

# 定义文件路径
file_path = r"D:\Intelligent_ecommerce\DataCleaning\data\data2_cleaning2.xlsx"
output_path = r"D:\Intelligent_ecommerce\DataCleaning\data\top_100_sku.xlsx"

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 获取第6列SKU值列
sku_column = df.iloc[:, 5]

# 统计出现次数最多的前100个SKU
top_100_sku = sku_column.value_counts().head(100)

# 筛选SKU值在Top100的行
filtered_df = df[df.iloc[:, 5].isin(top_100_sku.index)].copy()

# 明确将第一列的数据转换为字符串格式以避免科学计数法
filtered_df.loc[:, filtered_df.columns[0]] = filtered_df.iloc[:, 0].astype(str)

# 保存修改后的数据到新的Excel文件
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    filtered_df.to_excel(writer, index=False, sheet_name='Sheet1')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 设置文本格式
    text_format = workbook.add_format({'num_format': '@'})

    # 设置第一列的文本格式和列宽
    max_len = max(filtered_df.iloc[:, 0].astype(str).map(len).max(), len(filtered_df.columns[0])) + 1
    worksheet.set_column(0, 0, max_len, text_format)

    # 自动调整其他列宽
    for col_num, col in enumerate(filtered_df.columns[1:], start=1):
        max_len = max(filtered_df[col].astype(str).map(len).max(), len(col)) + 1
        worksheet.set_column(col_num, col_num, max_len)

print(f"处理后的数据已保存到 {output_path}")

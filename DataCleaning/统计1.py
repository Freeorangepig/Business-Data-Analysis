import pandas as pd

# 定义文件路径
file_path = r"D:\Intelligent_ecommerce\DataCleaning\data\data2_cleaning1.xlsx"
output_path = r"D:\Intelligent_ecommerce\DataCleaning\data\top_100_products.xlsx"

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 获取第6列商品名称列
product_column = df.iloc[:, 5]

# 统计出现次数最多的前200个商品
top_200_products = product_column.value_counts().head(100)

# 获取商品名称和出现次数
top_200_df = top_200_products.reset_index()
top_200_df.columns = ['商品名称', '出现次数']

# 获取第7列（类目）
category = df.iloc[:, [5, 6]].drop_duplicates().set_index('商品名称')

# 合并统计数据和类目数据
result_df = top_200_df.join(category, on='商品名称')

# 保存统计信息到新的Excel文件
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    result_df.to_excel(writer, index=False, sheet_name='Top 100 Products')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Top 100 Products']

    # 动态调整列宽
    for col_num, col in enumerate(result_df.columns):
        max_len = max(result_df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(col_num, col_num, max_len)

print(f"统计信息已保存到 {output_path}")

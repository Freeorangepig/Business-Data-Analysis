import pandas as pd

# 定义文件路径
file_path = r"D:\Intelligent_ecommerce\DataCleaning\data\top_100_sku.xlsx"
output_path = r"D:\Intelligent_ecommerce\DataCleaning\data\mapped_top_100_sku.xlsx"
mapping_folder = r"D:\Intelligent_ecommerce\DataCleaning\data"

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 定义要映射的列
columns_to_map = [2, 4, 6]  # 第3列、第5列和第7列

# 初始化映射表字典
mappings = {}

# 映射列值为数字
for col in columns_to_map:
    unique_values = df.iloc[:, col].unique()
    mapping_dict = {value: idx for idx, value in enumerate(unique_values)}
    mappings[col] = mapping_dict
    df.iloc[:, col] = df.iloc[:, col].map(mapping_dict)

# 明确将第一列的数据转换为字符串格式以避免科学计数法
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# 保存映射后的数据到新的Excel文件
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Mapped Data')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Mapped Data']

    # 动态调整列宽
    for col_num, col in enumerate(df.columns):
        max_len = max(df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(col_num, col_num, max_len)

# 保存映射表到单独的Excel文件
for col in columns_to_map:
    mapping_df = pd.DataFrame(list(mappings[col].items()), columns=['Original Value', 'Mapped Value'])
    mapping_output_path = f"{mapping_folder}/mapping_col_{col+1}.xlsx"
    with pd.ExcelWriter(mapping_output_path, engine='xlsxwriter') as writer:
        mapping_df.to_excel(writer, index=False, sheet_name='Mapping')

print(f"映射后的数据已保存到 {output_path}")
print("映射表已生成：")
for col in columns_to_map:
    print(f"  {mapping_folder}/mapping_col_{col+1}.xlsx")

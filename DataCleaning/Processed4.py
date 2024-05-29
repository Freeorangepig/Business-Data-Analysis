import pandas as pd
import os

# 定义文件路径
file_path = r"D:\Intelligent_ecommerce\DataCleaning\data\mapped_top_100_sku.xlsx"
output_folder = r"D:\Intelligent_ecommerce\DataCleaning\data\data_on_category"

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 按第5列（类目）进行分组
groups = df.groupby(df.columns[4])

# 初始化类目统计表
category_summary = []

# 遍历每个组，保存到单独的Excel文件
for group_name, group_df in groups:
    output_path = os.path.join(output_folder, f"category_{group_name}.xlsx")

    # 将第一列的数据转换为字符串格式以避免科学计数法
    group_df.iloc[:, 0] = group_df.iloc[:, 0].astype(str)

    # 保存修改后的数据到新的Excel文件
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        group_df.to_excel(writer, index=False, sheet_name='Sheet1')

        # 获取XlsxWriter workbook和worksheet对象
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # 设置文本格式
        text_format = workbook.add_format({'num_format': '@'})

        # 设置第一列的文本格式和列宽
        max_len = max(group_df.iloc[:, 0].astype(str).map(len).max(), len(group_df.columns[0])) + 1
        worksheet.set_column(0, 0, max_len, text_format)

        # 自动调整其他列宽
        for col_num, col in enumerate(group_df.columns[1:], start=1):
            max_len = max(group_df[col].astype(str).map(len).max(), len(col)) + 1
            worksheet.set_column(col_num, col_num, max_len)

    # 添加类目名称和数量到统计表
    category_summary.append([group_name, len(group_df)])

# 将类目统计表保存到Excel文件
summary_df = pd.DataFrame(category_summary, columns=['类目', '数量'])
summary_output_path = os.path.join(output_folder, "category_summary.xlsx")

with pd.ExcelWriter(summary_output_path, engine='xlsxwriter') as writer:
    summary_df.to_excel(writer, index=False, sheet_name='Summary')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Summary']

    # 动态调整列宽
    for col_num, col in enumerate(summary_df.columns):
        max_len = max(summary_df[col].astype(str).map(len).max(), len(col)) + 2
        worksheet.set_column(col_num, col_num, max_len)

print(f"按类目拆分后的数据已保存在 {output_folder} 文件夹下")
print(f"类目统计表已保存到 {summary_output_path}")

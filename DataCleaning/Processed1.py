import pandas as pd
"""
将原始数据data2中的空数据去除,并且将第1订单编号、8SKU值和最后一列门店ID设置成了文本格式
"""


# 定义文件路径
file_path = "D:\\Intelligent_ecommerce\\DataCleaning\\data\\data2.xlsx"
output_path = "D:\\Intelligent_ecommerce\\DataCleaning\\data\\data2_cleaning1.xlsx"

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 删除第16列为空的行
df_cleaned = df.dropna(subset=[df.columns[15]]).copy()

# 明确将第1、8和最后一列的数据转换为字符串格式以避免科学计数法
df_cleaned.iloc[:, 0] = df_cleaned.iloc[:, 0].astype(str)
df_cleaned.iloc[:, 7] = df_cleaned.iloc[:, 7].astype(str)
df_cleaned.iloc[:, -1] = df_cleaned.iloc[:, -1].astype(str)

# 保存修改后的数据到新的Excel文件
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    df_cleaned.to_excel(writer, index=False, sheet_name='Sheet1')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 设置文本格式
    text_format = workbook.add_format({'num_format': '@'})

    # 设置列宽和格式
    for col_num, col in enumerate(df_cleaned.columns):
        max_len = max(df_cleaned[col].astype(str).map(len).max(), len(col)) + 1
        if col_num == 0 or col_num == 7 or col_num == len(df_cleaned.columns) - 1:
            worksheet.set_column(col_num, col_num, max_len, text_format)
        else:
            worksheet.set_column(col_num, col_num, max_len)

print("数据处理完成，结果保存在 'data2_cleaning1.xlsx' 文件中。")

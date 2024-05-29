import pandas as pd

# 定义文件路径
file_path = "D:\\Intelligent_ecommerce\\DataCleaning\\data\\data2_cleaning1.xlsx"
output_path = "D:\\Intelligent_ecommerce\\DataCleaning\\data\\data2_cleaning2.xlsx"

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 去除第4、6和最后一列（注意列的索引是从0开始）
df.drop(df.columns[[3, 5, -1]], axis=1, inplace=True)

# 明确将第一列的数据转换为字符串格式以避免科学计数法
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# 保存修改后的数据到新的Excel文件
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # 获取XlsxWriter workbook和worksheet对象
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # 设置文本格式
    text_format = workbook.add_format({'num_format': '@'})

    # 设置第一列的文本格式和列宽
    max_len = max(df.iloc[:, 0].astype(str).map(len).max(), len(df.columns[0])) + 1
    worksheet.set_column(0, 0, max_len, text_format)

    # 自动调整其他列宽
    for col_num, col in enumerate(df.columns[1:], start=1):
        max_len = max(df[col].astype(str).map(len).max(), len(col)) + 1
        worksheet.set_column(col_num, col_num, max_len)

print("数据处理完成，结果保存在 'data2_cleaning2.xlsx' 文件中。")

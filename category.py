import pandas as pd

# 加载Excel文件
file_path = "D:\\Intelligent_ecommerce\\filter_data\\filtered_data2.xlsx"
data = pd.read_excel(file_path)

# 从第二行开始统计第7列类目
category_counts = data.iloc[1:, 6].value_counts()  # 第7列为类目列

# 输出类目总数
total_categories = category_counts.shape[0]
print(f"Total Categories: {total_categories}")

# 输出每种类目的名称和数量
category_counts_df = pd.DataFrame(category_counts).reset_index()
category_counts_df.columns = ['Category', 'Count']

# 格式化输出
output = category_counts_df.to_string(index=False)
print(output)

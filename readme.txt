2024年5月28日晚

data2.xlsx：去除了一些无关的列，比如门店性质之类的，手动去除。但是还有空值。

filtered_data2.xlsx：相比上一个去除了空数据。

filtered_data2_merged.xlsx：相比上一个根据类目信息进行了合并，由文件category_merged.py执行。

filtered_data2_processed1.xlsx：删除了第6列商品名称和第33列门店ID，由文件processed.py执行。

filtered_data2_processed2.xlsx：将市场名称列映射成了数字，由文件processed1.py执行。映射表保存在mapping_tables_marketname.xlsx文件中。

filtered_data2_processed3.xlsx：将类目列映射成了数字，由文件processed2.py执行。映射表保存在mapping_tables_category.xlsx文件中。

filtered_data2_processed4.xlsx：将商品属性列映射成了数字，由文件processed4.py执行。映射表保存在mapping_tables_attributes.xlsx文件中。

filtered_data2_processed5.xlsx：去掉了下单时间列，手动去除。

split_on_category文件夹中的各excel文件都是按照类目来分开的，31个类目。由文件split_category.py执行。

split_on_category_csv文件夹中的各csv文件由split_on_category文件夹中的各excel文件去掉第一行而成，由文件to_csv.py执行

更新：2024年5月59日晚
以上的数据不再使用了！昨天处理的时候出了一点差错，今天又想了一天，重新处理了，就用文件夹0529下的的文件吧！




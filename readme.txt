更新：2024年5月28日  周二晚

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

更新：2024年5月29日晚  周三晚

以上的数据不再使用了！昨天处理的时候出了一点差错，今天又想了一天，重新处理了，就用文件夹DataCleaning下的的文件吧！
今天就到这里了，现在是晚上22：33分，这些数据就暂时这样分类。
对于数据文件的解释说明，明天我会发布在readme上。
明天的任务转成csv格式，然后直接建模训练下试试。

更新：2024年5月30日  周四下午

现在正在答辩现场，先总结一下昨天的思路：昨天对于数据，首先筛选出了SKU值Top100的数据，感觉Top200还是种类有些多。
原始数据一共8万多条数据，Top200有6万多条，Top100有5万多条，先来Top100吧，类目还能少一些，暂时先建立一个哪怕不太准确的模型，
有个能操作的方向是目前初步分析阶段需要做到的。
根据SKU值筛选出Top100之后，又根据类目信息进行了分类。在这Top100的商品中，有27个类目。目前打算在这27个类目里进行预测和优化。
但是问题是，哪怕相同的一个类目里的商品差距可能较大，比如在根茎类里有胡萝卜🥕和白萝卜，红薯和紫薯这种东西价格会有差距。
但是目前先根据这些来吧，先找个建模思路，预测和优化暂时不要求准确。

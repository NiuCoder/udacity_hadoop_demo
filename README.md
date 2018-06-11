# udacity_hadoop_demo
[课程网站](https://classroom.udacity.com/courses/ud617)<br>
三个例子均来自Udacity的免费课程**Intro to Hadoop and MapReduce**，其中数据集均是课程提供的，由于github有文件大小限制，因此只上传了这些数据集中的一部分，三个例子均采用map&reduce，**代码的实现均由本人完成**。<br>
三个demo对应的数据集分别是销售数据、网站请求日志以及论坛帖子数据库。下面分别就每个项目进行说明<br>

# [sales](https://github.com/NiuCoder/udacity_hadoop_demo/tree/master/sales)
待处理的数据见purchase_samples.txt，数据结构为：日期|时间|商店名|物品种类|金额|支付方式，例如{2012-01-01}\t{09:00}\t{San Jose}\t{Men's Clothing}\t{214.05}\t{Visa}<br>
本数据集有三个目标，分别是：<br>
- 统计每个物品种类的总交易额，输出格式为<category,cost>，代码见：mapper.py以及reducer.py
- 统计每个商店的单笔最大交易额，输出格式为<store_name,max_cost>，代码见：mapper2.py以及reducer_max.py
- 统计每个商店的总交易额，输出格式为<store_name,total_cost>,代码见：mapper2.py以及reducer_total.py

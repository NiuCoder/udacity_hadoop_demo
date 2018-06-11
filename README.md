# udacity_hadoop_demo
[课程网站](https://classroom.udacity.com/courses/ud617)<br>
三个例子均来自Udacity的免费课程**Intro to Hadoop and MapReduce**，其中数据集均是课程提供的，由于github有文件大小限制，因此只上传了这些数据集中的一部分，三个例子均采用map&reduce，**代码的实现均由本人完成**。<br>
三个demo对应的数据集分别是销售数据、网站请求日志以及论坛帖子数据库。下面分别就每个项目进行说明。<br>

# [sales](https://github.com/NiuCoder/udacity_hadoop_demo/tree/master/sales)
数据集见[purchase_samples.txt](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/purchase_sample.txt)，数据结构为：<br>
日期|时间|商店名|物品种类|金额|支付方式，例如{2012-01-01}\t{09:00}\t{San Jose}\t{Men's Clothing}\t{214.05}\t{Visa}<br>
本例有三个目标，分别是：<br>
- 统计每个物品种类的总交易额，输出格式为<category,cost>，代码见：[mapper.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/mapper.py)以及[reducer.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/reducer.py)，结果见[result.txt](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/result.txt)
- 统计每个商店的单笔最大交易额，输出格式为<store_name,max_cost>，代码见：[mapper2.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/mapper2.py)以及[reducer_max.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/reducer.py)，结果见[result_max.txt](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/result_max.txt)
- 统计每个商店的总交易额，输出格式为<store_name,total_cost>,代码见：：[mapper2.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/mapper2.py)以及[reducer_total.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/reducer_total.py)，结果见[result_total.txt](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/sales/result_total.txt)

# [web_logs](https://github.com/NiuCoder/udacity_hadoop_demo/tree/master/web_logs)
数据集见[access_log.rar](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/access_log.rar)，需要先解压为.txt文件。数据结构为：<br>
ip|client_id(or -)|client_name(or -)|request_time|request|response_status|byte_size，例如10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469<br>
本例有三个目标，分别是：<br>
- 统计访问网站各文件的次数，输出格式为<path,request_times>，代码见：[mapper.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/mapper.py)以及[reducer.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/reducer.py)，结果见[hits_path_result.txt](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/hits_path_result.txt)
- 统计来自每个ip地址的请求，输出格式为<ip,request_times>，代码见：[mapper2.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/mapper2.py)以及[reducer2.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/reducer2.py)，结果见[hits_ip_result.txt](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/hits_ip_result.txt)
- 统计被访问最多的文件及对应的访问次数，输出格式为<path,max_request_times>，代码见：[mapper3.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/mapper3.py)以及[reducer3.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/reducer3.py)，结果见[hits_max_path_result.txt](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/web_logs/hits_max_path_result.txt)

# [forums](https://github.com/NiuCoder/udacity_hadoop_demo/tree/master/forms)
数据集见[forum_node_sample.tsv](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/forms/forum_node_sample.tsv)。数据结构为：<br>
ip|title|tagnames|author_id|body|node_type|parent_id|abs_parent_id|added_at|score|state_string|last_edited_id|last_activity_by_id|last_activity_at|active_revision_id|extra|extra_ref_id|extra_count|marked，这是表头，后边数据按照这个表头排列。需要注意的是body字段存储了很多一些html标签，所以在处理的时候如果需要将这些标签替换为转义字符，这样能够保证一条数据在一行。本例不包含处理代码。<br>
本例的目标只有一个：<br>
- 统计每个author_id在发帖最多的时间段，输出格式为：<author_id,hour>，代码见：[mapper.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/forms/mapper.py)以及[reducer.py](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/forms/reducer.py)，[student_test_posts.csv](https://github.com/NiuCoder/udacity_hadoop_demo/blob/master/forms/student_test_posts.csv)包含较少的数据用于测试代码。

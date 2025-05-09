#进行数据需求的逻辑计算
from file_define import FileReader,TextFileReader,JsonFilereader
from data_define import Record
text_file_reader=TextFileReader("E:/Desktop/2011年1月销售数据.txt")
json_file_reader=JsonFilereader("E:/Desktop/2011年2月销售数据JSON.txt")

jan_data=text_file_reader.read_data()
feb_data=json_file_reader.read_data()
#将两个月份的数据合并成1个list来存储
all_data=jan_data+feb_data

#开始进行数据计算
data_dict={}
for record in all_data:
    if record.date in data_dict.keys():
        #当前日期已经有记录了，所以和老记录做累加即可
        data_dict[record.date]+=record.money
    else:
        data_dict[record.date]=record.money
print(data_dict)

#数据的可视化分析
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys())) #添加X轴的数据
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))#添加Y轴数据
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)
bar.render()

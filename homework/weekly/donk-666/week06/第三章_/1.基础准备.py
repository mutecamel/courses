#导包
from pyspark import SparkConf,SparkContext
#创建SparkConf类对象
conf=SparkConf().setMaster("lacal[*]").setAppName("test_spark_app") #链式调用
sc=SparkContext(conf=conf)
print(sc.version)
sc.stop()




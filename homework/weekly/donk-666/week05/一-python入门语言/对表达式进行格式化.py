print("1*1结果是：%d"%(1*1))
print(f"1*2的结果是{1*2}")
print("string在python中的类型名是：%s"%type("字符"))

#练习题
name="传智播客"
stovk_prive=19.99
stovk_vode="003032"
stovk_prive_daily_growth_favtor=1.2
growth_days=7
stovk_prive_7days=stovk_prive*stovk_prive_daily_growth_favtor**7
print(f"公司:{name},股票代码{stovk_vode},当前股价{stovk_prive}")
print("每日增长系数:%3.2f,经过%s天增长，最终的股价为：%.2f"%(stovk_prive_daily_growth_favtor,growth_days,stovk_prive_7days))
num = 10
if num > 0:
    print("这是一个正数")
else:
    print("这不是一个正数")

score = 99
if score >= 90:
    print("成绩等级:A")
elif score >= 80:
    print("成绩等级:B")
elif score >= 70:
    print("成绩等级:C")
elif score >= 60:
    print("成绩等级:D")
else:
    print("成绩等级:F")

age = 22
has_license = True
if age >= 18:
    print("你已成年")
    if has_license:
        print("你可以合法开车")
    else:
        print("你还不能开车，需要先考取驾照")
else:
    print("你还未成年，不能开车")


year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} 年是闰年")
else:
    print(f"{year} 年不是闰年")

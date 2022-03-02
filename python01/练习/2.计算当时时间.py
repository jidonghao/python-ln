"""
    输入一个秒值，算出距离当日午夜的时间
    格式：HH:MM:SS
"""


class TimeStruct:
    def __init__(self):
        self.hour = 11
        self.minute = 59
        self.second = 60


inTime = TimeStruct()
inTime.second = int(input("请输入秒："))
# 计算格式化后的时间
inTime.hour = inTime.second // 3600  # 地板除得小时
inTime.second -= inTime.hour * 3600
inTime.minute = inTime.second // 60  # 地板除得分钟
inTime.second -= inTime.minute * 60

nowTime = TimeStruct()
if inTime.hour > 0:
    nowTime.hour -= inTime.hour
if inTime.minute > 0:
    nowTime.minute -= inTime.minute
if inTime.second > 0:
    nowTime.second -= inTime.second

# 最后整理该时间
if nowTime.second == 60:
    nowTime.second = 0
    nowTime.minute += 1
if nowTime.minute == 60:
    nowTime.minute = 0
    nowTime.hour += 1
print("现在的时间是：%02d:%02d:%02d" % (nowTime.hour, nowTime.minute, nowTime.second))

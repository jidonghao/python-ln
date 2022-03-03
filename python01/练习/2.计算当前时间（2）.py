"""
    输入一个秒值，算出距离当日午夜的时间
    格式：HH:MM:SS
    方式2
"""
inSecond = int(input("请输入秒："))
s = inSecond % 60  # 得出秒数
m = (inSecond - s) / 60 % 60  # 得出分钟
h = (inSecond - m) / 60 // 60  # 得出小时
print("%02d:%02d:%02d" % (h, m, s))




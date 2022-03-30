import math

weight, flag = input("请输入重量和是否加急（y/n）:").split();
weight = int(weight);
# 初始圆子为13块 默认加急
yuanzi = 13
# 如果不加急 给减去5块
if flag == "n":
    yuanzi -= 5
# 如果重量多于 1000 则将weight - 1000（超过的部分）除500并向上取整
if weight > 1000:
    yuanzi += (math.ceil((weight - 1000) / 500) * 4)

print(yuanzi)

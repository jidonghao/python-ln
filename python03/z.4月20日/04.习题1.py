# 输入城市
def inCityAndProvince():
    displayCityAndProvince(input("请输入省份："), input("请输入城市："))


# 显示
def displayCityAndProvince(Province, City):
    print("省份：" + Province + ";城市：" + City)


inCityAndProvince()

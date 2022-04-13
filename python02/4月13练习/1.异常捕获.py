while True:
    try:
        name = input("姓名:")
        if name.strip() == "":
            raise Exception("无效的姓名")
        gender = input("性别:")
        if gender != "男" and gender != "女":
            raise Exception("无效的性别")
        age = float(input("年龄:"))
        if age < 18 or age > 30:
            raise Exception("无效的年龄")
        print(name, gender, age)
    except Exception as err:
        print(err)
    print("---------")

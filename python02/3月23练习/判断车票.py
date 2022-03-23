# his_ticket = True


his_ticket = input("有票吗?：")
if "没" in his_ticket or "n" in his_ticket or "F" in his_ticket or "f" in his_ticket:
    his_ticket = False
if his_ticket:
    print("允许安检")
    knife_length = float(input("你滴刀多少CM？："))
    if knife_length > 20:
        print("不允许上车")
    else:
        print("允许上车")
else:
    print("不允许进门")

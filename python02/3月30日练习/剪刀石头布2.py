import random

arr = ["石头", "剪刀", "布"]
player = int(input("请输入您要出的拳-石头(1)/剪刀(2)/布(3):"))
computer = random.randint(1, 3)
print("你出的是：" + arr[player - 1] + ",电脑出的是：" + arr[computer - 1])

if computer == player:
    print("平局了!")
elif computer - player == 2 or computer - player == -1:
    print("电脑胜!")
else:
    print("你赢了！")

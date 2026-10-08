import random
#生成一个1到100之间的随机整数
target=random.randint(1,100)
#初始化猜测次数计数器
count=0
print("欢迎来到猜数字游戏！")
print("我已经选择了一个1到100之间的整数。你能猜到它是什么吗？")
#使用无限循环
while True:
    #获取用户输入
    guess=int(input("请输入你猜测的数字："))
    #每次猜测后，次数+1
    count+=1
    #判断猜测结果
    if guess == target:
        # f字符串格式化,把变量count的值嵌入输出文字
        print(f"恭喜你！你猜对了！总共猜了{count}次。")
        break     #猜中后跳出循环
    elif guess < target:
        print("你猜的数字太小了，请再试一次。")
    else:
        print("你猜的数字太大了，请再试一次。")

       
        
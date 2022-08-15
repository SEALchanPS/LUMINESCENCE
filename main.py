# LUMINESCENCE.

"""进行游戏初始化"""
import json
import time
from tkinter import messagebox
import random

global status_json
global status_dict
global result
global result2


# 调用函数

def printfile(filename):
    """该函数将传入文件打印出来。若无法找到文件，则会打印出提示语。"""
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"未找到文件 {filename} 。")


def write2dict():
    """该函数将 JSON 文件转换成字典形式。"""
    global status_json
    global status_dict
    status_dict = ''
    with open("status.json", 'r') as status_json:
        status_dict = json.loads(status_json.read())


def write2json():
    """该函数将字典转换并保存至 JSON 文件。"""
    global status_json
    global status_dict
    with open("status.json", 'w') as status_json:
        status_json.write(json.dumps(status_dict))


# 状态修改函数


# 主要活动函数

def halfday1():
    """2100 年 4 月 6 日上午，主线共同进行部分"""
    global result
    status_dict["time"] = 1
    write2json()
    printfile("text/halfday1.1.txt")
    print("4 月 6 日上午，你只能选择进入主线 1 (心中的姜夏黎) (输入 1) 或不活动 (输入 q)。")
    print("但在之后的日子里，你将无法主动对姜夏黎发起主要活动。")
    active = True
    while active:
        result = input("请做出选择：")
        if result == '1':
            active = False
            print("你已经选择了推进主线 1 “心中的姜夏黎”")
        if result == 'q':
            active = False
            print("你已经选择了在当前时间段不活动。")
        else:
            print("你似乎做出了错误的选择。请重试")
    if result == '1':
        print("你选择了主动前去寻找姜夏黎聊天。姜夏黎对你的来访似乎十分乐意。")
        status_dict["level"]["loving_level"] += 20
        write2json()
        print("心动程度 +20%")
        print("你已使用早上的活动时间。")
    if result == 'q':
        print("你继续坐在座位上复习。对你而言，什么也没有发生。")


def halfday2():
    """2100 年 4 月 6 日中午/下午"""
    global result, result2
    status_dict["time"] = 2
    printfile("text/halfday1.2.txt")
    print("4 月 6 日下午，你可以选择不活动 (输入 q)，主线 2 (冷光中学的一切) (输入 2)。")
    active = True
    while active:
        result = input("请做出选择：")
        if result == 'q':
            active = False
            print("你已经选择了在当前时间段不活动。")
        if result == '2':
            active = False
            print("你已经选择了进行主线 2 “冷光中学的一切”。接下来，请做出具体选择。")
        else:
            print("你似乎做出了错误的选择。请重试")
    if result == '2':
        print(
            "请在以下三个选项里做出具体选择。\n"
            "输入 1：待在食堂。在下午上课前一直待在食堂里，去观察食堂内部的情况。\n"
            "输入 2：询问班主任。询问班主任有关于中午食堂的事情。\n"
            )
        active = True
        while active:
            result2 = input("请做出选择。")
            if result2 == "1":
                active = False
                print("你已经选择待在食堂。")
            if result2 == "2":
                active = False
                print("你已经选择询问班主任。")
            else:
                print("你似乎做出了错误的选择。请重试")
    if result2 == "1":
        print("不幸地，食堂里没有任何有用的情报。")
    if result2 == "2":
        status_dict["level"]["doubting_level"] += 30
        print("你班没有食物中毒的情况。并且，因为你的贸然询问，班主任的怀疑程度 +30%。")
        write2json()


def halfday3():
    """2100 年 4 月 7 日上午"""
    global result
    print("4 月 7 日上午，你看到政府领导来到学校进行审查。你必须选择进入主线 2。")
    print(
        "你可以选择：\n"
        "1. 询问班主任。询问班主任有关食堂的事情。\n"
        "2. 拦截领导。你将会尝试拦截政府领导，并询问相关内容。\n"
        "3. 询问当事学生。你将尝试询问当事学生。\n"
        "另外：在做出选择时，请务必确保你已经深思熟虑了。")
    active = True
    while active:
        result = input("请做出选择。")
        if result == "1":
            active = False
            print("不幸地，班主任 99.9% 不会直接回答你的问题。但是有可能你是那唯一的 0.1%。")
            print("正在为你寻找 1 到 1000 之内的一个随机数。若随机数=1，则班主任会直接告诉你问题。")
            randomnum = random.randint(1, 1000)
            if randomnum == 1:
                print(f"恭喜你，随机数值为 {randomnum}。班主任会直接告诉你这一切。")
                printfile("text/halfday3.1.txt")
            else:
                print(f"不幸的，你所抽到的随机数为 {randomnum}。班主任的怀疑程度增加了 20%.")
                status_dict["level"]["doubting_level"] += 20
                write2json()
        if result == "2":
            active = False
            print("你选择了拦截领导！请选择你是否需要热身（Y/N）。")
            while active:
                yourchoice = input("请做出选择。")
                if yourchoice.upper() == 'Y':
                    active = True
                    print("热身需要耗费 40 点潜力值，但会让潜行能力增加 30%。")
                    if status_dict["potential"] <= 40:
                        status_dict["potential"] -= 40
                        status_dict["ability"]["stalking"] += status_dict["ability"]["stalking"] * 0.3
                        write2json()
                    else:
                        print("你的潜力值不够进行热身。请选择 N。")
                if yourchoice.upper() == 'N':
                    active = True
                    print("你不选择热身。")
                else:
                    print("你似乎做出了错误的选择。请重试")
            print("即将开始难度 4 的潜行。")
            ability = True
            for trytime in range(4):
                stalking = status_dict["ability"]["stalking"]
                this_value = random.randint(0, 80)
                print(f"校验第 {trytime} 次潜行中：程序随机数 {this_value}，潜行能力 {stalking}")
                if this_value > stalking:
                    ability = False
            if ability:
                print("你本次潜行成功了！你成功潜行到了领导面前。但你没有问到任何有价值内容。")


"""加载 JSON File"""
write2dict()

# 欢迎用户
# This will be extended soon.
print("WELCOME TO LUMINESCENCE WORLD.")
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
print("LOADING YOUR LAST PLAY...")

if not status_dict["first_run"]["first_started"]:
    # WELCOME NEW USER, EXTENDED SOON
    status_dict["first_run"]["first_started"] = True
    if not status_dict["first_run"]["already_read_license"]:
        printfile("LICENSE")
        status_dict["first_run"]["already_read_license"] = True
        write2json()
    if not status_dict["first_run"]["already_read_info"]:
        printfile("INFO.md")
        status_dict["first_run"]["already_read_info"] = True
        write2json()

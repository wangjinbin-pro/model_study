import random
import unittest
def myself():
    name = "wangjinbin"
    age = "26"
    height = "172.5"

    print(f"{name} is {age} years old and {height} cm tall")

def score_num():
    score = int(input("请输入你的成绩："))

    if score >= 90:
        print(f"优秀，你的成绩是{score}")
    elif score >= 80:
        print(f"良好，你的成绩是{score}")
    else:
        print(f"不合格，你的成绩是{score}")


def random_num():
    num = random.randint(1, 5)
    if num == 1:
        print("宇宙无敌大天才")
    elif num == 2:
        print("稳居第二")
    elif num == 3:
        print("勉强拿下第三")
    elif num == 4:
        print("奋力拿下及格")
    else:
        print("一拖垃圾！！！")



random_num()


name = "wangjinbin"
age = "26"
height = "172.5"

print(f"{name} is {age} years old and {height} cm tall")


score = int(input("请输入你的成绩："))

if score >= 90:
    print(f"优秀，你的成绩是{score}")
elif score >= 80:
    print(f"良好，你的成绩是{score}")
else:
    print(f"不合格，你的成绩是{score}")
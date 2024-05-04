import time

# 定义工作和休息时间（以秒为单位）
work_time = 25 * 60
break_time = 5 * 60
cycles = 4

for cycle in range(cycles):
    print("开始工作...")
    time.sleep(work_time)
    print("休息中...")
    time.sleep(break_time)
    print("休息结束，下一个工作周期")

print("番茄工作法周期完成！")

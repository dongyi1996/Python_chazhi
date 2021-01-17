import arcpy, time

n = 5
p = 1

readTime = 1.5  # 停顿时间
loopTime = 0.3  # 循环迭代延时

#  首先显示的是默认的进度条显示形式
#  time sleep() 函数推迟调用线程的运行，可通过参数（指秒数），表示进程挂起的时间。
arcpy.SetProgressor("default", "This is the default progressor")
time.sleep(readTime)

# 模拟显示执行多个任务时进度条及进度标签

for i in xrange(1, 5):
    arcpy.SetProgressorLabel("Working on 'phase' {0}".format(i))
    arcpy.AddMessage("Messages for phase {0}".format(i))
    time.sleep(readTime)

#  设置进度条为步进显示形式
arcpy.SetProgressor("step",
                    "Step progressor: Counting from 0 to {0}".format(n),
                    0, n, p)
time.sleep(readTime)

#  通过循环模拟进度条步进显示

for i in range(n):
    if (i % p) == 0:
        arcpy.SetProgressorLabel("Iteration: {0}".format(i))
        arcpy.SetProgressorPosition(i)
        time.sleep(loopTime)

# 更新进度显示的最后部分（上面的range只是到4，进度不能到100%）
#
arcpy.SetProgressorLabel("Iteration: {0}".format(i + 1))
arcpy.SetProgressorPosition(i + 1)
#  信息框中添加进度向上显示完成消息
#
arcpy.AddMessage("Done counting up\n")
time.sleep(readTime)

# 只是为了有趣，让进度条再倒回去
#
arcpy.SetProgressor("default", "Default progressor: Now we'll do a countdown")
time.sleep(readTime)
arcpy.AddMessage("Here comes the countdown...")
arcpy.SetProgressor("step",
                    "Step progressor: Counting backwards from {0}".format(n),
                    0, n, p)
time.sleep(readTime)
arcpy.AddMessage("Counting down now...\n")

for i in range(n, 0, -1):
    if (i % p) == 0:
        arcpy.SetProgressorLabel("Iteration: {0}".format(i))
        arcpy.SetProgressorPosition(i)
        time.sleep(loopTime)

#  更新剩余进度显示
arcpy.SetProgressorLabel("Iteration: {0}".format(0))
arcpy.SetProgressorPosition(0)
time.sleep(readTime)
arcpy.AddMessage("All done")
arcpy.ResetProgressor()

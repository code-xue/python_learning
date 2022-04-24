#在线安装方式： 控制台命令：pip install 第三方模块名字
#使用：import 模块名

import schedule
import time

def job():
    print("哈哈---------")

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
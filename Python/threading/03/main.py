# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 11:50:30 2017
@author: Moondra
"""

# Daemon 的意思是 main process结束的时候 True 线程退出， False 线程不退出（继续执行）
# Daemon 的默认值是 False

# daemon 的解释: 守护进程(daemon)是一类在后台运行的特殊进程，用于执行特定的系统任务。
# 很多守护进程在系统引导的时候启动，并且一直运行直到系统关闭。另一些只在需要的时候才启动，完成任务后就自动结束

import threading
import time

total = 4

def creates_items():
    global total
    for i in range(10):
        time.sleep(2)
        print('Creator 1 added item', ' Items total:', total)
        total += 1
    print('Creator 1 creation is done')


def creates_items_2():
    global total
    for i in range(7):
        time.sleep(1)
        print('Creator 2 added item', ' Items total:', total)
        total += 1
    print('Creator 2 creation is done')


def limits_items():
    
    #print('finished sleeping')
    
    global total
    while True:
        if total > 5:

            print ('Consumer overload', ' Items total:', total)
            total -= 3
            print('Consumer subtracted 3', ' Items total:', total)
        else:
            time.sleep(1)
            print('Consumer waiting', ' Items total:', total)


creator1 = threading.Thread(target  = creates_items)
creator2 = threading.Thread(target = creates_items_2)
limitor = threading.Thread(target = limits_items)
limitor.daemon = True
# limitor.setDaemon(True)

print(limitor.isDaemon())


creator1.start()
creator2.start()
limitor.start()


creator1.join()
creator2.join()
# limitor.join() # while True 一直阻塞，回不到主进程
# 如果耶不佳 daemon 的话，那么主进程结束了（下面的语句输出），但是limitor线程还在跑,进程结束不了

print('our ending value of total is' , total)
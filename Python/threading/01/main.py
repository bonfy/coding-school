# coding: utf-8

import threading
import time

# 必须要有一个函数
def sleeper(n, name):
    print('Hi, I am {} Going to sleep for {} seconds'.format(name, n))
    while(n):
        time.sleep(1)
        print('{}: Sleep 1 second'.format(name))
        n -= 1
    print('{} has woken up from sleep'.format(name))


# without join: 主进程运行 不必等待 线程运行完成
def without_join():
    # threading.Thread 创建 thread, target 传函数， args 传参数
    t = threading.Thread(target=sleeper, name='thread-1',args=(5, 'thread1'))
    t.start()


    # 主进程, 线程不影响主进程
    print('This is main process-1')
    n = 2
    while n:
        time.sleep(1)
        print('main process-1 sleep 1 second')
        n -= 1
    print('This is main process-1')

# with join： 主进程 等待 线程运行完成才执行，通常是主进程依赖 线程请求的资源
def with_join():
    # threading.Thread 创建 thread, target 传函数， args 传参数
    t = threading.Thread(target=sleeper, name='thread-2',args=(5, 'thread2'))
    t.start()

    # t.join() 阻塞(Block)进程执行
    t.join()

    # 主进程, 线程不影响主进程
    print('This is main process-2')
    n = 2
    while n:
        time.sleep(1)
        print('main process-2 sleep 1 second')
        n -= 1
    print('This is main process-2')

if __name__ == '__main__':
    print('Without Join:')
    without_join()
    print('#'*8)
    print('With join')
    with_join()

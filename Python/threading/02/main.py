# coding: utf-8

import threading
import time

def sleeper(n, name):
    print('Hi, I am {}. Going to sleep for {} seconds.'.format(name, n))
    while n:
        time.sleep(1)
        print('{} sleep 1 second'.format(name))
        n -= 1
    print('{} has woken up from sleep.'.format(name))

# t = threading.Thread(target = sleeper, name = 'thread-1', args =(5, 'thread1') )

thread_list = []

for i in range(5):
    t = threading.Thread(target=sleeper, 
                        name='thread-{}'.format(i),
                        args=(5, 'thread{}'.format(i)))

    t.start()
    thread_list.append(t)
    # t.join() # 不能放这里， thread0 就会阻塞 thread1    
    print('{} has started.'.format(t.name))

for t in thread_list:
    t.join() # 放这里可以让所有线程都运行了，然后阻塞外面的进程    


print('hello')
print('what is going on')

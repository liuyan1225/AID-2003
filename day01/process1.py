__Author__ = "Yan Liu"

import multiprocessing as mp
import time

a = 1

def func():
    global a
    print("这里是子进程")
    a = 100
    print("a>>:",a)
    time.sleep(2)
    print("子进程结束")
    print(b)

#创建子进程对象
p = mp.Process(target=func)

b = 2

#启动子进程
p.start()

# b = 2


#主进程执行
print("主进程执行a>>:",a)

#等待子进程结束，回收子进程
# p.join()

print("这里是主进程的a>>:",a)



__Author__ = "Yan Liu"

import multiprocessing as mp

import time

def func01(i):
    time.sleep(1)
    print("这里是子进程",i)

pool = mp.Pool(4) #创建进程池对象

for i in range(10):
    pool.apply_async(func = func01,args=(i,)) #将事件对象加入进程池队列中

pool.close()

pool.join()
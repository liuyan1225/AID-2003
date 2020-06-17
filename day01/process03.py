"""
给进程函数传参
"""
import multiprocessing as mp
import time

def func(name,age):
    print("姓名为：",name)
    time.sleep(1)
    print("年龄为：",age)

# p = mp.Process(target=func,args=("lily",25))
# p = mp.Process(target=func,kwargs={"name":"lily","age":25})
p = mp.Process(target=func,args=("lily",),kwargs={"age":25})

p.start()
p.join()

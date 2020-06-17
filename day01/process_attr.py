__Author__ = "Yan Liu"
import multiprocessing as mp
import time

def func():
    time.sleep(3)
    print("这里是子进程")

p = mp.Process(target=func,name="p01")

p.start()


print(p.pid)

print(p.name)

p.name = "subprocess-1"
print(p.name)
p.join()

print(p.is_alive())
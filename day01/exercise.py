__Author__ = "Yan Liu"
"""
    使用两个子进程（process）分别复制
     一个文件的上下半部分，将内容各自复制到
     一个新的文件中。

     获取文件字节数，使用os.path模块的getsize方法

"""
import multiprocessing as mp
import os

file_path = r"/month02/CONCURRENT/day01/1"

file_bytes = os.path.getsize(file_path)


def copy_file_front():
    f1 = open("file1.txt", "wb")
    try:
        f = open(file_path, "rb")
    except Exception as e:
        print(e)
    else:
        data = f.read(file_bytes // 2)
        f1.write(data)
        f.close()
    f1.close()


def copy_file_rear():
    f2 = open("file2.txt", "wb")
    try:
        f = open(file_path, "rb")
    except Exception as e:
        print(e)
    else:
        f.seek(file_bytes // 2 + 1)
        data = f.read()
        f2.write(data)
        f.close()
    f2.close()


list_task = [copy_file_front, copy_file_rear]
list_process = []

for item in list_task:
    p = mp.Process(target=item)
    list_process.append(p)
    p.start()

for item in list_process:
    item.join()








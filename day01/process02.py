import multiprocessing as mp


def func01():
    print("func01")


def func02():
    print("func02")


def func03():
    print("func03")


list_func = [func01, func02, func03]

list_process = []

for item in list_func:
    p = mp.Process(target=item)
    list_process.append(p)
    p.start()

for item in list_process:
    p.join()

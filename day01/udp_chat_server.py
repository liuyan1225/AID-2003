__Author__ = "Yan Liu"
"""
    功能 ： 类似qq群功能
	【1】 有人进入聊天室需要输入姓名，姓名不能重复（创建列表存姓名）
	【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室（广播）
	【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx （广播）
	【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室（广播）
	【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx（广播）

"""
import socket, os

# 创建套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 允许广播地址发送和接收消息
sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 绑定ip和port
sockfd.bind(("127.0.0.1", 8989))

# 创建列表，用于存放用户姓名
list_name = []


# 接收消息
def recv_data():
    """
    接收数据
    :return: 用户信息，元组形式
    """
    while True:
        data, addr = sockfd.recvfrom(1024)
        return (data,addr)



# 发送消息
def send_data(addr,msg):
    """
    发送数据
    :return:
    """
    while True:
        sockfd.sendto(msg.encode(),addr)


# 创建子进程，用于发送消息
pid = os.fork()

# 子进程执行的部分
if pid == 0:
    # send_data()
    pass
# 父进程执行的部分
else:
    while True:
        #判断用户名是否已经存在
        if recv_data()[0].decode() not in list_name:
            msg = "欢迎进入聊天室。。。"
            send_data(recv_data()[1],msg)
            break
        msg = "用户名已经存在，请重新输入："
        send_data(recv_data()[1], msg)

    sockfd.sendto("欢迎%s,%d进入聊天室。。。"%recv_data()[1],("1217.168.244.255",8989))




# while True:
#     while True:
#         # 接收进入聊天室的用户姓名
#         data, addr = sockfd.recvfrom(1024)
#
#         # 如果姓名已经存在，重新输入
#         if data in list_name:
#             sockfd.sendto("用户名已经存在，请重新输入：".encode(), addr)
#             continue
#
#         sockfd.sendto("欢迎进入聊天室。。。".encode(), addr)
#
#         # 向广播地址发送：xxx 进入了聊天室
#         sockfd.sendto("用户%s进入聊天室" % addr.encode(), ("192.168.244.255", 8989))
#
#         # 接收用户发送的消息
#         data, addr = sockfd.recvfrom(1024)

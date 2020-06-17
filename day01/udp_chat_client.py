__Author__ = "Yan Liu"
import socket

sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

while True:

    name = input("请输入姓名：")

    #向服务端发送姓名
    sockfd.sendto(name.encode(),("127.0.0.1",8989))

    #接收服务端信息
    recv_data, addr = sockfd.recvfrom(1024)

    if recv_data.decode() != "欢迎进入聊天室。。。":
        continue

    while True:
        #开始发送信息
        send_data = input("请输入要发送的信息：")
        sockfd.sendto(send_data.encode(),("127.168.244.255",8989))



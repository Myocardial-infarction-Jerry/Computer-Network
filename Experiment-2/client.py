import socket
import threading
import sys

# 进程终止标志
running = True

# 创建TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置服务器IP和端口
server_ip = 'localhost'
server_port = 12345
server_address = (server_ip, server_port)

# 连接服务器
client_socket.connect(server_address)
print('已连接到服务器:', server_address)

# 输入昵称
nickname = None
while True:
    nickname = input('请输入昵称: ')
    if nickname != 'server':
        break
    print('昵称不能为\'server\'')
client_socket.sendall(nickname.encode())


# 接收服务器消息的函数
def receive_message():
    global running
    while running:
        try:
            # 接收服务器消息
            message = client_socket.recv(1024).decode()
            if message == '':
                running = False
                break
            print(message)
        except Exception as e:
            print(e)
            break


# 发送消息的函数
def send_message():
    global running
    while running:
        try:
            # 输入消息
            message = input()
            if message == 'quit':
                running = False
                client_socket.sendall(message.encode())
                break
            # 判断消息类型（广播或私聊）
            if message.startswith('@'):
                # 私聊消息
                client_socket.sendall(f'{message}'.encode())
            else:
                # 广播消息
                client_socket.sendall(message.encode())
        except Exception as e:
            print(e)
            break


# 创建线程接收消息和发送消息
receive_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)

# 启动线程
receive_thread.start()
send_thread.start()

# 等待发送线程结束
send_thread.join()

# 关闭连接
client_socket.close()

# 退出整个进程，包括所有线程
sys.exit()
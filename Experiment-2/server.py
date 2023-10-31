import socket
import threading
import sys


# 处理客户端连接的函数
def handle_client(client_socket, client_address):
    # 接收客户端昵称
    nickname = client_socket.recv(1024).decode()
    print('客户端已连接:', nickname)

    # 存储客户端信息
    clients[nickname] = client_socket

    # 向所有客户端广播新客户端上线消息
    broadcast_message(f'{nickname} 上线了！')

    while True:
        try:
            # 接收客户端消息
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # 判断消息类型（广播或私聊）
            if data.startswith('@'):
                # 私聊消息
                recipient, message = data.split(' ', 1)
                if recipient in clients:
                    send_private_message(nickname, recipient[1:], message)
                else:
                    send_private_message('server', nickname, '用户不存在！')
            else:
                # 广播消息
                broadcast_message(f'{nickname}: {data}')

        except Exception as e:
            print(e)

    # 客户端断开连接后的处理
    del clients[nickname]
    client_socket.close()
    print('客户端已断开连接:', nickname)
    broadcast_message(f'{nickname} 下线了！')


# 向所有客户端广播消息
def broadcast_message(message):
    for client_socket in clients.values():
        client_socket.sendall(message.encode())


# 向指定客户端发送私聊消息
def send_private_message(sender, recipient, message):
    if recipient in clients:
        client_socket = clients[recipient]
        client_socket.sendall(f'私聊消息 from {sender}: {message}'.encode())


# 处理多个客户端连接
def message_handler():
    while True:
        # 接受客户端连接
        client_socket, client_address = server_socket.accept()

        # 创建线程处理客户端连接
        client_thread = threading.Thread(target=handle_client,
                                         args=(client_socket, client_address))
        client_thread.start()


# 创建TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置服务器IP和端口
server_ip = 'localhost'
server_port = 12345
server_address = (server_ip, server_port)

# 绑定服务器地址
server_socket.bind(server_address)

# 监听连接
server_socket.listen(5)
print('等待客户端连接...')

# 存储在线客户端的信息
clients = {}

# 消息处理线程
message_thread = threading.Thread(target=message_handler, args=())
message_thread.start()

while True:
    command = input()
    if command == 'exit':
        print('再见！')
        broadcast_message('服务器关闭!')
        sys.exit()
    elif command == 'list':
        print('目前在线用户有（%d）：' % (len(clients)))
        print(clients, sep='\n')

message = input()
recipient, message = message.split(' ', 1)
print(f'@{recipient} {message}')
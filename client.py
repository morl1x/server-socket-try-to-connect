import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "localhost"  # Замените на реальный внешний IP-адрес сервера
port = 11111

client_socket.connect((server_ip, port))

# Получить запрос на ввод имени от сервера
name_request = client_socket.recv(1024).decode()
print(name_request, end=" ")

# Ввести имя и отправить серверу
name = input()
client_socket.send(name.encode())

# Получить и вывести приветственное сообщение
welcome_message = client_socket.recv(1024).decode()
print(welcome_message)

# Добавьте код для обработки других операций с сервером

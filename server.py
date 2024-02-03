import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 11111

server_socket.bind((host, port))
server_socket.listen(5)

print(f"Сервер слушает на {host}:{port}")

clients = {}  # Словарь для хранения соединений и имен клиентов


def handle_client(client_socket):
    # Запросить имя у клиента
    client_socket.send("Введите ваше имя: ".encode())
    client_name = client_socket.recv(1024).decode()

    # Приветствовать клиента
    welcome_message = f"Привет, {client_name}!"
    client_socket.send(welcome_message.encode())

    # Сохранить соединение и имя клиента
    clients[client_socket] = client_name

    # Добавить код для обработки других операций с клиентом


while True:
    client_socket, addr = server_socket.accept()
    print(f"Получено подключение от {addr}")

    # Обработать клиента в отдельном потоке или процессе
    handle_client(client_socket)

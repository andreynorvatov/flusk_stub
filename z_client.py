import socket
import time


def main():
    """
    Клиент отправляет запросы серверу и ожидает вычисление простых математических действий
    """
    while 1:
        try:
            operator = str(input('Enter operator(give, take): '))
            break
        except:
            print("Reinput")
            continue

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(('127.0.0.1', 9998))

        while True:

            client.send(operator.encode("utf-8"))
            data = client.recv(1024)
            data_new = data.decode("utf-8")
            time.sleep(1)
            print(f"The result has been calculated. Answer: {data_new}")
            break


if __name__ == '__main__':
    main()

import socket
# from urllib import response
# from views import *

# curl --http0.9 localhost:5000

def get_next():
    l = ['first', 'second', 'third']
    res = l[2]

    return res


def generate_response(request):
    body = get_next()

    return body.encode()


def run():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()



    while True:

        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)

        response = generate_response(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()


if __name__ == "__main__":
    run()

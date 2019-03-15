from handler import handler


def job(socket, root):
    while True:
        conn, addr = socket.accept()
        handler(conn, root)

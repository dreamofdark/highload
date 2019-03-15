from response import Response


def handler(connection, root):
    while True:
        data = connection.recv(1024)
        if not data:
            break

        response = Response(data)
        r = response.get(root)

        connection.send(r)
        connection.close()
        break
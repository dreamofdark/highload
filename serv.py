import socket
from parser import parse_conf
from job import job
from pool import Pool


cpu, thread_number, root = parse_conf()

sock = socket.socket()

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('', 80))

p = Pool(thread_number, job, (sock, root))

sock.listen(1)

p.start()






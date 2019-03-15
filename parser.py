def parse_conf():

    try:
        f = open('/etc/httpd.conf', 'r')
    except FileNotFoundError:
        exit('conf is not found')

    data = f.read()
    f.close()

    if not data:
        exit('no data')

    conf = data.split('\n')

    cpu = int(conf[0].split(' ')[1])
    thread = int(conf[1].split(' ')[1])
    root = str(conf[2].split(' ')[1])

    return cpu, thread, root






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


    result = {}
    for str in conf:
        pair = str.split(' ')
        if len(pair) < 2:
            continue
        result[pair[0]] = pair[1]

    cpu = int(result['cpu_limit'])
    thread = int(result['thread_limit'])
    root = result['document_root']

    return cpu, thread, root






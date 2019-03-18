def parse_conf():

    try:
        f = open('/etc/httpd.conf', 'r')
        print('cfg opened')
    except FileNotFoundError:
        print('cfg not found')
        exit('conf is not found')

    data = f.read()
    f.close()

    print(data)

    if not data:
        exit('no data')

    conf = data.split('\n')
    print('parse conf ', conf)


    result = {}
    for str in conf:
        pair = str.split(' ')
        print(pair)
        if len(pair) < 2:
            print('<2')
            continue
        result[pair[0]] = pair[1]

    cpu = int(result['cpu_limit'])
    thread = int(result['thread_limit'])
    root = result['document_root']

    return cpu, thread, root






from datetime import datetime
import pytz
import os
from urllib import parse


status = {
    200: '200 OK',
    403: '403 Forbidden',
    404: '404 Not Found',
    405: '405 Method Not Allowed',
}

content_type = {
    'html': 'text/html',
    'css': 'text/css',
    'js': '	application/javascript',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'gif': 'image/gif',
    'swf': 'application/x-shockwave-flash',
}


class Response:
    date = datetime.now(tz=pytz.timezone('GMT')).strftime('%a, %d %b %Y %X %Z')
    server = 'server/1.0'
    connection = 'closed'
    status_code = 404
    content_length = 0
    file_type = ''
    index = False

    def __init__(self, req):
        self.req = req.decode()

    def __parse_req(self):
        return self.req.split('\r\n')[0].split(' ')

    def __bad_req(self):
        st = status[self.status_code]
        return ('HTTP/1.1 %s\r\nDate: %s\r\nServer: %s\r\n' % (st, self.date, self.server)).encode()

    def __content_type(self):
        if self.file_type in content_type.keys():
            return content_type[self.file_type]
        else:
            return 'text/plain'

    def __ok_req(self, data):
        st = status[self.status_code]
        file = self.__content_type()
        return ('HTTP/1.1 %s\r\nDate: %s\r\nServer: %s\r\nContent-Type: %s\r\nContent-Length: %d\r\n\r\n' %
                (st, self.date, self.server, file, self.content_length)).encode() + data

    def __ok_req_head(self):
        st = status[self.status_code]
        file = self.__content_type()
        return ('HTTP/1.1 %s\r\nDate: %s\r\nServer: %s\r\nContent-Type: %s\r\nContent-Length: %d\r\n\r\n' %
                (st, self.date, self.server, file, self.content_length)).encode()

    def __get_path(self, root, path):
        path = path[1:]
        path = parse.unquote(path)

        q = path.find('?')
        if q != -1:
            path = path[0:q]

        file = os.path.join(root, path)

        if os.path.isdir(file):
            file = os.path.join(file, 'index.html')
            self.index = True

        return file

    def get(self, root):
        param = self.__parse_req()

        if not (param[0] == 'GET' or param[0] == 'HEAD'):
            self.status_code = 405
            return self.__bad_req()

        file = self.__get_path(root, param[1])

        if file.find('../') != -1:
            self.status_code = 403
            return self.__bad_req()

        if os.path.exists(file):
            f = open(file, 'rb')
        else:
            if self.index:
                self.status_code = 403
            else:
                self.status_code = 404
            return self.__bad_req()

        data = f.read()
        f.close()

        self.status_code = 200
        self.content_length = len(data)
        self.file_type = str(file.split('.')[-1])

        if param[0] == 'HEAD':
            return self.__ok_req_head()

        return self.__ok_req(data)

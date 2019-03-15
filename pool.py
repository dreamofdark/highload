from threading import Thread


class Pool:
    def __init__(self, size, target, args):
        self.pool = []
        self.size = size
        self.target = target
        self.args = args

    def start(self):
        for i in range(self.size):
            thread = Thread(target=self.target, args=self.args)
            self.pool.append(thread)

        for i in self.pool:
            i.start()

from threading import Thread


class ThreadedWebServer(Thread):

    def __init__(self, web_server):
        super().__init__()
        self.web_server = web_server
        self.daemon = True
        self.start()

    def run(self):
        self.web_server.run_forever()






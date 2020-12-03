from homework3.threaded_webserver import ThreadedWebServer
from homework3.webserver import Webserver

web_server = Webserver(6790, 5)

thread1 = ThreadedWebServer(web_server)
thread2 = ThreadedWebServer(web_server)
thread3 = ThreadedWebServer(web_server)
thread4 = ThreadedWebServer(web_server)
while True:
    pass

from threading import Thread

import requests


def http_get(id_, shot, port):
    for i in range(shot):
        response = requests.get(f'http://localhost:{port}/static/index.html')
        print(f'#{id_}의 {i} 번 째 요청 {response.status_code}')


t1 = Thread(target=http_get, args=['1', 10, 6790])
t2 = Thread(target=http_get, args=['2', 10, 6790])
t3 = Thread(target=http_get, args=['3', 10, 6790])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()



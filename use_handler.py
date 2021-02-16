from configparser import ConfigParser, ExtendedInterpolation
from common.httphander import HttpHandler
import time
import asyncio

httphandler = HttpHandler()

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('./config/config.ini')

url = config['url']['photo_domain']

print(url)

print('=========================================동기=========================================')
start = time.time()  # 실행시간 체크 

# 동기
for i in range(1, 30):
    print(httphandler.call_url(url, i))

print(f'동기 sec: {str(time.time() - start)}')
print('')

print('=========================================비동기=========================================')
start = time.time() 

# 비동기
tasks = [httphandler.async_call_url(url, i) for i in range(1, 30)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

print(f'비동기 sec: {str(time.time() - start)}')

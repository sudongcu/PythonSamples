import requests
import aiohttp
import asyncio

class HttpHandler:
    
    def init(self):
        pass

    # 동기
    def call_url(self, url, count):
        res = requests.get(f'{url}/{count}')
        return res.text

    # 비동기
    async def async_call_url(self, url, count):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{url}/{count}') as res:
                response = await res.text()
                return response

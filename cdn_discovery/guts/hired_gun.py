import confidential
import moon
import itertools

def URL_iterator():
    for i in range(0,128):
        for j in itertools.combinations_with_replacement(moon.search_space, i):
            payload = ''.join(j)
            yield ''.join((confidential.preamble,payload))



import asyncio
import aiohttp
from aiohttp import ClientSession, ClientConnectorError

async def fetch_html(url: str, session: ClientSession, **kwargs) -> tuple:
    try:
        resp = await session.request(method="GET", url=url, **kwargs)
    except ClientConnectorError:
        return (url, 404)
    return (url, resp.status)

async def make_requests(urls, **kwargs) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                fetch_html(url=url, session=session, **kwargs)
            )
        results = await asyncio.gather(*tasks)

    for result in results:
        print(f'{result[1]} - {str(result[0])}')

if __name__ == "__main__":
    import pathlib
    import sys

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    
    urls = URL_iterator()

    asyncio.run(make_requests(urls=urls))
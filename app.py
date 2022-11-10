import aiohttp
import asyncio

async def scraper(session,url):
    data = await session.get(url)
    return data

async def main(urls: list= []):
    error_urls= []
    final_result = []
    task_list = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.create_task(scraper(session,url))
            task.url = url
            task_list.append(task)
        done, _pending =await asyncio.wait(task_list)
        for item in done:
            if item.exception() is None:
                data = await (await item).text()
                final_result.append(data)
            else:
                error_urls.append(item.url)
    return len(final_result),error_urls

if __name__ == "__main__":
    urllist = ['https://www.arsenal.com','https://www.goal.com','','https://www.goaaksdhkajsn.com']
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    data = asyncio.run(main(urllist))
    print(data)
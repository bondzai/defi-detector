import os
import asyncio
from pyppeteer import launch
from dotenv import load_dotenv


async def scrape_data(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url, {'timeout': 60000})

    body_content = await page.evaluate('''() => {
        return document.querySelector('body').innerHTML;
    }''')

    await browser.close()
    return body_content

async def main():
    load_dotenv()
    url = os.getenv("BEEFY_URL")
    body_content = await scrape_data(url)
    print(body_content)

asyncio.get_event_loop().run_until_complete(main())

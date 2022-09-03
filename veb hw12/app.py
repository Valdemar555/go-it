import asyncio
import sys

from aiohttp import web
import aiohttp_jinja2
import jinja2
from src.routes import setup_routes

app = web.Application()

setup_routes(app)
aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('src', 'templates'))

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


if __name__ == "__main__":
    web.run_app(app, host='127.0.0.1', port=8080)
from aiohttp_jinja2 import template
from models import BoxingResults, InternationalMatches, db_session


@template('index.html')
async def index(requests):
    return {'title': 'text'}

@template('boxing.html')
async def boxing_matches(requests):
    matches = db_session.query(BoxingResults).all()
    return {'matches': matches}

@template('football.html')
async def football_matches(requests):
    matches = db_session.query(InternationalMatches).all()
    return {'matches': matches}


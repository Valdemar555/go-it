import aiohttp
import asyncio
from bs4 import BeautifulSoup
from models import BoxingResults, InternationalMatches, db_session


async def boxing_matches(session):
    async with session.get('https://vringe.com/results/', ssl=False) as response:
            soup = BeautifulSoup(await response.text(), "lxml")
            left_b = soup.find_all("td", class_="boxer_1")
            right_b = soup.find_all("td", class_="boxer_2")
            score = soup.find_all("td", class_="vs")
                        
            box_matches = []
            step = 0
            for i in range(len(left_b)):
                box_matches.append({
                    'boxer_1': left_b[step].text.strip(),
                    'boxer_2': right_b[step].text.strip(),
                    'result': score[step].text.strip()
                    })
                step += 1  
                        
            for item in box_matches:
                match = BoxingResults(vs=f'{item.get("boxer_1")}-{item.get("boxer_2")}',
                                                result=item.get('result'))
                db_session.add(match)
                db_session.commit()
                db_session.close()

async def football_matches(session):
    async with session.get('https://football.ua/default.aspx?menu_id=scoreboard&champ_id=92', ssl=False) as response:
            soup = BeautifulSoup(await response.text(), "lxml")
            left_t = soup.find_all('td', class_='left-team')
            right_t = soup.find_all('td', class_='right-team')
            score = soup.find_all('td', class_='score ended')
            friendly_matches = []
            count = 0
            for i in range(len(left_t)):
                friendly_matches.append({
                    'home': left_t[count].text.strip(),
                    'away': right_t[count].text.strip(),
                    'score': score[count].text.strip()
                })
                count += 1
    
            for item in friendly_matches:
                match = InternationalMatches(f_match=f'{item.get("home")}-{item.get("away")}',
                                                 score=item.get('score'))
                db_session.add(match)
                db_session.commit()
                db_session.close()


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(boxing_matches(session), football_matches(session))
        
        
if __name__ == "__main__":
    asyncio.run(main())


        

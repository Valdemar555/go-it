from datetime import datetime,timedelta
from time import strftime

users = [
    {
        "name":"Bill", 
        "birthday":datetime(year=1998, month=3, day=9)
    },
    {
        "name":"Giil", 
        "birthday":datetime(year=1995, month=3, day=6)
    },
    {
        "name":"Till",
        "birthday":datetime(year=1985, month=3, day=8)
    }
]


def get_birthdays_per_week (list):
    birthday_week = {
                    'Monday': [],
                    'Tuesday': [],
                    'Wednesday': [],
                    'Thursday': [],
                    'Friday': [],
                  }
    new_date = []

    for i in range(0, len(users)):
        birthday_str = (users[i]['birthday'].strftime('%d %B')).split()
        #print (birthday_str)  
        current_date = datetime.now()
        start = datetime.now() - timedelta(days=current_date.weekday() + 2)      
        #print(start)
        week_range = [start + timedelta(days=day) for day in range(0, 7)]
        #print(week_range)
        now_week = [day.strftime('%d') for day in week_range]
        #print(now_week)
        
        current_date_str = (current_date.strftime('%d %B')).split()
        #print (current_date_str)
        if birthday_str[0] in now_week:
            new_date.append(users[i])
            #print(new_date)
                   
            for birsday in range(0, len(new_date)):
                #print(birsday)
                if new_date[birsday]['birthday'].strftime('%d') in now_week[0:3]:
                    birthday_week['Monday'].append(new_date[birsday]['name'])
                    
                elif new_date[birsday]['birthday'].strftime('%d') in now_week[3]:
                    birthday_week['Tuesday'].append(new_date[birsday]['name'])
                elif new_date[birsday]['birthday'].strftime('%d') in now_week[4]:
                    birthday_week['Wednesday'].append(new_date[birsday]['name'])
                elif new_date[birsday]['birthday'].strftime('%d') in now_week[5]:
                    birthday_week['Thursday'].append(new_date[birsday]['name'])
                elif new_date[birsday]['birthday'].strftime('%d') in now_week[6]:
                    birthday_week['Friday'].append(new_date[birsday]['name'])
                else:
                    print ("Don't have birthdays for this week")
                #print(birthday_week)
                for key,value in birthday_week.items():
                    print(f'{key}:{value}')
                   
if __name__ == '__main__':       
    get_birthdays_per_week(users)
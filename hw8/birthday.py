from datetime import datetime,timedelta


users = [
    {
        "name":"Oleg", 
        "birthday":datetime(year=1998, month=4, day=14)
    },
    {
        "name":"Dima", 
        "birthday":datetime(year=1995, month=4, day=15)
    },
    {
        "name":"Vova",
        "birthday":datetime(year=1985, month=4, day=16)
    },
    {
        "name":"Vlad", 
        "birthday":datetime(year=1998, month=4, day=17)
    },
    {
        "name":"Olga", 
        "birthday":datetime(year=1995, month=4, day=18)
    },
    {
        "name":"Julia",
        "birthday":datetime(year=1985, month=4, day=19)
    }

    ]


def get_birthdays_per_week (users:list):

    birthday_week = {
                    'Monday': [],
                    'Tuesday': [],
                    'Wednesday': [],
                    'Thursday': [],
                    'Friday': [],
                  }

    current_date = datetime.now()
    for i in range(0, len(users)):
        new_birthday = (users[i]['birthday'].replace(year=current_date.year))
        if current_date > new_birthday:
            new_birthday = new_birthday.replace(year=current_date.year + 1)  
        delta = new_birthday-current_date
        if delta.days < 8:
            day_bth = new_birthday.weekday()
            if day_bth == 1:
                birthday_week['Tuesday'].append(users[i]['name'])
            elif day_bth == 2:
                birthday_week['Wednesday'].append(users[i]['name'])
            elif day_bth == 3:
                birthday_week['Thursday'].append(users[i]['name'])
            elif day_bth == 4:
                birthday_week['Friday'].append(users[i]['name'])
            else:
                birthday_week['Monday'].append(users[i]['name'])
        print(birthday_week)
        
            
                   
if __name__ == '__main__':       
    get_birthdays_per_week(users)


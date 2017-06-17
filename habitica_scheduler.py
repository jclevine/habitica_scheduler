import requests
from DayOfWeek import DayOfWeek
from my_dailies import my_dailies


def create_request(dailies_by_day_of_week):
    dailies = []
    for day_of_week, daily in dailies_by_day_of_week.items():
        dailies.extend(create_day_of_week_dailies(day_of_week, daily))
    return dailies


def create_day_of_week_dailies(day_of_week, dailies):
    return [
       create_daily(day_of_week, daily) for daily in dailies
    ]


def create_daily(day_of_week, daily):
    return {
        'text': '{} {}'.format(day_of_week.value, daily['text']),
        'type': 'daily',
        'repeat': create_repeat(day_of_week),
        'priority': daily['difficulty'].value
    }


def create_repeat(day_of_week):
    return {
        'su': day_of_week == DayOfWeek.SUNDAY,
        'm': day_of_week == DayOfWeek.MONDAY,
        't': day_of_week == DayOfWeek.TUESDAY,
        'w': day_of_week == DayOfWeek.WEDNESDAY,
        'th': day_of_week == DayOfWeek.THURSDAY,
        'f': day_of_week == DayOfWeek.FRIDAY,
        's': day_of_week == DayOfWeek.SATURDAY
    }


def schedule(dailies_by_day_of_week):
    headers = {
        'x-api-user': 'X',
        'x-api-key': 'X'
    }

    url = 'https://habitica.com/api/v3/tasks/user'

    response = requests.post(url, json=create_req(dailies_by_day_of_week), headers=headers)
    print(response)

schedule(my_dailies)



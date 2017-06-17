import requests
from DayOfWeek import DayOfWeek
from Difficulty import Difficulty


my_dailies = [
    {
        'text': 'This is a test!!!!',
        'day_of_week': DayOfWeek.TUESDAY,
        'difficulty': Difficulty.HARD
    },
{
        'text': 'This is also a test!!!!',
        'day_of_week': DayOfWeek.THURSDAY,
        'difficulty': Difficulty.TRIVIAL
    }
]


def create_request(dailies):
    return [create_daily(daily) for daily in dailies]


def create_daily(daily):
    return {
        'text': '{} {}'.format(daily['day_of_week'].value, daily['text']),
        'type': 'daily',
        'repeat': create_repeat(daily['day_of_week']),
        'priority': daily['difficulty'].value
    }

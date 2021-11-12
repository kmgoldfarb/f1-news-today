import time
from base.scrapers import get_autosport, get_planet_f1, get_sky_sports, get_racer, get_racefans, get_racingnews365, get_wtf1, get_driver_standings, get_constructor_standings, get_upcoming_races


def get_news():
    get_autosport()
    get_planet_f1()
    get_racer()
    get_racefans()
    get_racingnews365()
    get_sky_sports()
    get_wtf1()


def get_standings():
    get_driver_standings()
    get_constructor_standings()


def get_races():
    get_upcoming_races()